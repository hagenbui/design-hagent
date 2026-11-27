"""Build the design review HTML from a small JSON file, so the agent never writes or reads HTML.

Usage: python3 -I review_html.py <folder>/review.json
Screenshots are PNG files at <folder>/img/<node id with : as ->.png (or the screen's "image"), or one PNG per
section ("sheets") that each screen is cropped from by its "at" position, so a review needs one screenshot call.
Writes <folder>/review-<date>.html with the images embedded, and compares it with the newest earlier
review-*.html in the same folder: each issue is New or Still open, and earlier issues on screens in
this scope that are gone are Solved. The data is embedded in the page for the next comparison.
Standard library only. Format of the JSON: references/review-report.md, "HTML report".
"""
import base64, glob, html, json, os, re, sys

SEV = ['P1', 'P2', 'P3', 'UX']
L = {
    'en': dict(title='Design review', scope='Scope', date='Date', prev='Compared with', first='First review',
               new='New', open='Still open', solved='Solved', all='All', nr='Issues on screens not in this scope (not rechecked)',
               rule='Rule', ev='Evidence', imp='Impact', fix='Fix', conf='Confidence', ux='UX suggestion',
               solved_list='Solved since the previous review', none='No issues on this screen.'),
    'vi': dict(title='Đánh giá thiết kế', scope='Phạm vi', date='Ngày', prev='So với', first='Lần đánh giá đầu',
               new='Mới', open='Còn mở', solved='Đã sửa', all='Tất cả', nr='Vấn đề trên màn hình ngoài phạm vi lần này (chưa kiểm tra lại)',
               rule='Quy tắc', ev='Bằng chứng', imp='Ảnh hưởng', fix='Cách sửa', conf='Độ tin cậy', ux='Góp ý UX',
               solved_list='Đã sửa từ lần đánh giá trước', none='Không có vấn đề trên màn hình này.'),
}
CSS = """body{font:14px/1.5 system-ui,sans-serif;margin:0;background:#f6f6f4;color:#1d1d1b}
header{padding:20px 24px;background:#fff;border-bottom:1px solid #e3e3df}h1{margin:0 0 4px;font-size:20px}
.meta{color:#666}.chips{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}
.chip{border:1px solid #d6d6d0;border-radius:99px;padding:2px 10px;background:#fff;cursor:pointer}
.chip.on{background:#1d1d1b;color:#fff;border-color:#1d1d1b}
main{padding:16px 24px;display:grid;gap:16px}
.screen{background:#fff;border:1px solid #e3e3df;border-radius:10px;padding:16px;display:grid;grid-template-columns:minmax(200px,320px) 1fr;gap:20px}
.screen h2{grid-column:1/-1;margin:0;font-size:16px}.shot{position:relative;align-self:start}
.shot img,.crop{width:100%;display:block;border-radius:6px;border:1px solid #e3e3df;background-repeat:no-repeat}
.box{position:absolute;border:2px solid var(--c);border-radius:3px;pointer-events:none}
.dot{position:absolute;transform:translate(-50%,-50%);min-width:22px;height:22px;border-radius:11px;color:#fff;font:600 12px/22px system-ui;text-align:center;box-shadow:0 0 0 2px #fff;background:var(--c)}
.P1{--c:#d92d20}.P2{--c:#e8730c}.P3{--c:#2e6fd8}.UX{--c:#6b6b66}.solved{--c:#1a8a4a}
.dot.solved{background:#fff;color:var(--c);border:2px solid var(--c);box-shadow:none}.box.solved{border-style:dashed}
ol{margin:0;padding:0;list-style:none;display:grid;gap:10px;align-content:start}li{border-left:4px solid var(--c,#ccc);padding:4px 10px}
li.solved{color:#555}.n{font-weight:700}.tag{font-size:12px;border-radius:4px;padding:1px 6px;margin-left:6px;background:#eee}
.tag.new{background:#fde7c8}.tag.solved{background:#d6f2e1}dl{margin:4px 0 0;display:grid;grid-template-columns:auto 1fr;gap:0 8px}dt{color:#666}dd{margin:0}
.hide{display:none!important}"""
JS = """document.querySelectorAll('.chip').forEach(c=>c.onclick=()=>{document.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x===c));
const f=c.dataset.f;document.querySelectorAll('[data-s]').forEach(e=>e.classList.toggle('hide',f!=='all'&&e.dataset.s!==f));});"""


def key(i):
    return '%s|%s' % (i['rule'], i.get('node') or '%s@%s' % (i['screen'], i.get('box')))


def read_embedded(path):
    with open(path, encoding='utf-8') as f:
        m = re.search(r'<script type="application/json" id="review-data">(.*?)</script>', f.read(), re.S)
    return json.loads(m.group(1)) if m else None


def previous(folder, out):
    older = [p for p in glob.glob(os.path.join(folder, 'review-*.html')) if os.path.basename(p) < os.path.basename(out)]
    return max(older, key=os.path.basename) if older else None


def check(d):
    """Stop with a clear message on input the page can't show, instead of a crash or a silent gap."""
    def num(v):
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(d.get('date', ''))):
        sys.exit('date must be YYYY-MM-DD, got %r' % d.get('date'))
    ids = set()
    for s in d.get('screens', []):
        size = s.get('size')
        if not (isinstance(size, list) and len(size) == 2 and all(num(v) and v > 0 for v in size)):
            sys.exit('screen %s: size must be [width, height] in Figma units, got %r' % (s.get('id'), size))
        ids.add(s.get('id'))
        if 'sheet' in s:
            sheet = next((h for h in d.get('sheets', []) if h.get('id') == s['sheet']), None)
            hs = sheet and sheet.get('size')
            if not (isinstance(hs, list) and len(hs) == 2 and all(num(v) and v > 0 for v in hs)):
                sys.exit('screen %s: sheet %r is not in sheets or has no size' % (s.get('id'), s['sheet']))
            at = s.get('at')
            if not (isinstance(at, list) and len(at) == 2 and all(num(v) for v in at)):
                sys.exit('screen %s: at must be [x, y], its position in the sheet' % s.get('id'))
    for i in d.get('issues', []):
        if i.get('severity') not in SEV:
            sys.exit('issue %s: severity must be one of %s, got %r' % (i.get('rule'), ', '.join(SEV), i.get('severity')))
        if i.get('screen') not in ids:
            sys.exit('issue %s: screen %r is not in screens' % (i.get('rule'), i.get('screen')))
        if 'box' in i and not (isinstance(i['box'], list) and len(i['box']) == 4 and all(num(v) for v in i['box'])):
            sys.exit('issue %s: box must be [x, y, w, h], got %r' % (i.get('rule'), i['box']))


def margin(sheet):
    """Uniform margin (Figma units) the screenshot adds around the node, solved from its pixel size."""
    if not sheet.get('px'):
        return 0
    (W, H), (pw, ph) = sheet['size'], sheet['px']
    if pw == ph:
        return 0
    m = (W * ph - H * pw) / (2 * (pw - ph))
    return m if abs(m) >= 0.5 else 0


def main(argv):
    src = argv[0]
    folder = os.path.dirname(os.path.abspath(src))
    with open(src, encoding='utf-8') as f:
        d = json.load(f)
    check(d)
    t = L.get(d.get('language', 'en'), L['en'])
    out = os.path.join(folder, 'review-%s.html' % d['date'])
    screens = {s['id']: s for s in d['screens']}
    def load(rel, what):
        p = os.path.join(folder, rel)
        if not os.path.isfile(p):
            sys.exit('missing screenshot for %s: %s' % (what, p))
        with open(p, 'rb') as f:
            return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()
    used = {s['sheet'] for s in d['screens'] if 'sheet' in s}
    d['_sheets'] = {h['id']: dict(h, _img=load(h.get('image') or 'img/sheet-%s.png' % h['id'], 'sheet ' + h['id']), _n=n)
                    for n, h in enumerate(d.get('sheets', [])) if h['id'] in used}
    for s in d['screens']:
        if 'sheet' not in s:
            s['_img'] = load(s.get('image') or 'img/%s.png' % s['id'].replace(':', '-'), s['id'])
    issues = sorted(d['issues'], key=lambda i: (SEV.index(i['severity']), i['screen']))
    prev_path = previous(folder, out)
    prev = read_embedded(prev_path) if prev_path else None
    if not prev:
        prev_path = None
    # earlier issues = last report's issues plus what it carried from screens it did not recheck
    prev_keys = {key(i): i for i in (prev['issues'] + prev.get('carried', []))} if prev else {}
    for n, i in enumerate(issues, 1):
        i['n'], i['status'] = n, 'open' if key(i) in prev_keys else 'new'
    cur = {key(i) for i in issues}
    gone = [i for k, i in prev_keys.items() if k not in cur]
    solved = [dict(i, status='solved') for i in gone if i['screen'] in screens]
    carried = [i for i in gone if i['screen'] not in screens]
    data = {k: d[k] for k in ('app', 'date', 'language', 'scope') if k in d}
    data.update(screens=[{k: v for k, v in s.items() if k != '_img'} for s in d['screens']], issues=issues, solved=solved,
                carried=carried, not_rechecked=len(carried), previous=os.path.basename(prev_path) if prev_path else None)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(render(d, data, screens, t))
    return out


def render(d, data, screens, t):
    e = html.escape
    issues, solved = data['issues'], data['solved']
    cnt = lambda f: sum(1 for i in issues if f(i))
    chips = [('all', t['all'], len(issues) + len(solved)), ('new', t['new'], cnt(lambda i: i['status'] == 'new')),
             ('open', t['open'], cnt(lambda i: i['status'] == 'open')), ('solved', t['solved'], len(solved))]
    sev = ' · '.join('%s %d' % (s if s != 'UX' else t['ux'], cnt(lambda i, s=s: i.get('severity') == s)) for s in SEV)
    h = ['<!doctype html><html lang="%s"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
         '<title>%s · %s</title><style>%s</style><header><h1>%s · %s</h1><div class="meta">%s: %s · %s: %s · %s</div><div class="meta">%s</div><div class="chips">'
         % (e(d.get('language', 'en')), e(t['title']), e(d.get('app', '')), CSS, e(t['title']), e(d.get('app', '')), e(t['scope']), e(d.get('scope', '')),
            e(t['date']), e(d['date']), e(t['prev'] + ': ' + data['previous']) if data['previous'] else e(t['first']), e(sev))]
    h += ['<button class="chip%s" data-f="%s">%s %d</button>' % (' on' if f == 'all' else '', f, e(lab), c) for f, lab, c in chips]
    h.append('</div></header><main>')
    if d['_sheets']:  # each sheet image appears once; screens show their slice of it
        h.append('<style>%s</style>' % ''.join('.sh%d{background-image:url(%s)}' % (sh['_n'], sh['_img']) for sh in d['_sheets'].values()))

    def pos(i, s):
        x, y, w, hh = i['box']
        W, H = s['size']
        return x / W * 100, y / H * 100, w / W * 100, hh / H * 100

    for s in d['screens']:
        mine = [i for i in issues if i['screen'] == s['id']]
        fixed = [i for i in solved if i['screen'] == s['id']]
        h.append('<section class="screen"><h2>%s</h2><div class="shot">' % e(s.get('name', s['id'])))
        if 'sheet' in s:
            sh = d['_sheets'][s['sheet']]
            (SW, SH), (W, H), (ax, ay) = sh['size'], s['size'], s['at']
            pad = margin(sh)  # a section screenshot comes with a margin around the node; widen the sheet by it
            SW, SH, ax, ay = SW + 2 * pad, SH + 2 * pad, ax + pad, ay + pad
            px = ax / (SW - W) * 100 if SW > W else 0
            py = ay / (SH - H) * 100 if SH > H else 0
            h.append('<div class="crop sh%d" role="img" aria-label="%s" style="aspect-ratio:%s/%s;background-size:%.3f%% %.3f%%;background-position:%.3f%% %.3f%%"></div>'
                     % (sh['_n'], e(s.get('name', '')), W, H, SW / W * 100, SH / H * 100, px, py))
        else:
            h.append('<img src="%s" alt="%s">' % (s['_img'], e(s.get('name', ''))))
        for i in mine + fixed:
            if not i.get('box'):
                continue  # no place on the screen: the issue shows in the list only
            x, y, w, hh = pos(i, s)
            cls = 'solved' if i['status'] == 'solved' else e(i.get('severity', 'UX'))
            label = '✓' if i['status'] == 'solved' else i['n']
            if w and hh:
                h.append('<div class="box %s" data-s="%s" style="left:%.2f%%;top:%.2f%%;width:%.2f%%;height:%.2f%%"></div>' % (cls, i['status'], x, y, w, hh))
            h.append('<div class="dot %s" data-s="%s" style="left:%.2f%%;top:%.2f%%">%s</div>' % (cls, i['status'], x, y, label))
        h.append('</div><ol>')
        for i in mine + fixed:
            st = i['status']
            sevcls = 'solved' if st == 'solved' else e(i.get('severity', 'UX'))
            num = '✓' if st == 'solved' else '%d' % i['n']
            rows = ''.join('<dt>%s</dt><dd>%s</dd>' % (t[k], e(str(i[f]))) for k, f in (('ev', 'evidence'), ('imp', 'impact'), ('fix', 'fix'), ('conf', 'confidence')) if i.get(f))
            h.append('<li class="%s" data-s="%s"><span class="n">%s</span> %s <b>%s</b> %s<span class="tag %s">%s</span><dl>%s</dl></li>'
                     % (sevcls, st, num, e(i.get('severity', '')), e(i['rule']), e(i.get('title', '')), st, e(t[st]), rows))
        if not mine and not fixed:
            h.append('<li data-s="none" style="border:0">%s</li>' % e(t['none']))
        h.append('</ol></section>')
    if data['not_rechecked']:
        h.append('<p class="meta">%s: %d</p>' % (e(t['nr']), data['not_rechecked']))
    h.append('</main><script>%s</script><script type="application/json" id="review-data">%s</script></html>'
             % (JS, json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')))
    return ''.join(h)


if __name__ == '__main__':
    print(main(sys.argv[1:]))
