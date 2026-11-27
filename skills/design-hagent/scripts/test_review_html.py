"""Tests for review_html.py. Run: python3 -I skills/design-hagent/scripts/test_review_html.py"""
import json, os, sys, tempfile, unittest, base64

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import review_html  # noqa: E402

PNG = base64.b64decode(  # 1x1 transparent png
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=')


def review(date, issues, screens=('1:1', '1:2')):
    return {
        'app': 'Demo', 'date': date, 'language': 'en', 'scope': 'Flow 1',
        'screens': [{'id': s, 'name': 'Screen ' + s, 'size': [375, 812]} for s in screens],  # image defaults to img/<id>.png
        'issues': issues,
    }


def issue(rule, node, screen='1:1', sev='P2'):
    return {'rule': rule, 'title': rule + ' title', 'severity': sev, 'screen': screen, 'node': node,
            'box': [10, 20, 30, 40], 'evidence': 'e <b>', 'impact': 'i', 'fix': 'f'}


class ReviewHtmlTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.dir, 'img'))
        for s in ('1-1', '1-2', '1-3'):
            open(os.path.join(self.dir, 'img', s + '.png'), 'wb').write(PNG)

    def run_review(self, data, name):
        p = os.path.join(self.dir, name + '.json')
        json.dump(data, open(p, 'w'))
        out = review_html.main([p])
        return out, open(out, encoding='utf-8').read()

    def test_first_review_all_new_with_numbered_dots(self):
        out, html = self.run_review(review('2026-11-01', [issue('DR-001', '1:5', sev='P3'), issue('DR-002', '1:6', sev='P1')]), 'a')
        self.assertTrue(out.endswith('review-2026-11-01.html'))
        data = review_html.read_embedded(out)
        self.assertEqual([i['status'] for i in data['issues']], ['new', 'new'])
        self.assertEqual([(i['n'], i['rule']) for i in data['issues']], [(1, 'DR-002'), (2, 'DR-001')])  # P1 first
        self.assertIn('class="dot', html)
        self.assertIn('data:image/png;base64,', html)
        self.assertNotIn('e <b>', html)  # escaped
        self.assertNotIn('img/1-1.png', html)  # images embedded, not linked

    def test_second_review_marks_new_open_solved_and_not_rechecked(self):
        self.run_review(review('2026-11-01', [issue('DR-001', '1:5'), issue('DR-002', '1:6'),
                                                issue('DR-003', '1:9', screen='1:3')], screens=('1:1', '1:3')), 'a')
        out, html = self.run_review(review('2026-11-08', [issue('DR-001', '1:5'), issue('DR-004', '1:7')]), 'b')
        data = review_html.read_embedded(out)
        st = {i['rule']: i['status'] for i in data['issues']}
        self.assertEqual(st, {'DR-001': 'open', 'DR-004': 'new'})
        self.assertEqual([i['rule'] for i in data['solved']], ['DR-002'])
        self.assertEqual(data['not_rechecked'], 1)  # DR-003 was on a screen not in this scope
        self.assertEqual(data['previous'], 'review-2026-11-01.html')
        self.assertIn('Solved', html)

    def test_same_day_rerun_compares_with_earlier_report_not_itself(self):
        self.run_review(review('2026-11-01', [issue('DR-001', '1:5')]), 'a')
        out1, _ = self.run_review(review('2026-11-08', [issue('DR-001', '1:5')]), 'b')
        out2, _ = self.run_review(review('2026-11-08', []), 'c')
        self.assertEqual(out1, out2)
        data = review_html.read_embedded(out2)
        self.assertEqual(data['previous'], 'review-2026-11-01.html')
        self.assertEqual([i['rule'] for i in data['solved']], ['DR-001'])

    def test_vietnamese_labels(self):
        d = review('2026-11-01', [issue('DR-001', '1:5')]); d['language'] = 'vi'
        _, html = self.run_review(d, 'a')
        self.assertIn('Mới', html)

    def test_issues_on_skipped_screens_carry_forward(self):
        # A covers 1:1 and 1:3, B covers only 1:1, C covers 1:3 again
        self.run_review(review('2026-11-01', [issue('DR-001', '1:5'), issue('DR-003', '1:9', screen='1:3'),
                                                issue('DR-004', '1:8', screen='1:3')], screens=('1:1', '1:3')), 'a')
        self.run_review(review('2026-11-08', [issue('DR-001', '1:5')], screens=('1:1',)), 'b')
        out, _ = self.run_review(review('2026-11-15', [issue('DR-003', '1:9', screen='1:3')], screens=('1:3',)), 'c')
        data = review_html.read_embedded(out)
        self.assertEqual({i['rule']: i['status'] for i in data['issues']}, {'DR-003': 'open'})
        self.assertEqual([i['rule'] for i in data['solved']], ['DR-004'])
        self.assertEqual([i['rule'] for i in data['carried']], ['DR-001'])  # 1:1 not rechecked this time

    def test_bad_input_stops_with_a_message(self):
        bad = [
            dict(review('2026-11-01', [issue('DR-001', '1:5', sev='P0')])),
            dict(review('../x', [])),
            dict(review('2026-11-1', [])),
            dict(review('2026-11-01', [issue('DR-001', '1:5', screen='7:7')])),
            dict(review('2026-11-01', []), screens=[{'id': '1:1', 'size': [0, 812]}]),
            dict(review('2026-11-01', [dict(issue('DR-001', '1:5'), box=[1, 2])])),
        ]
        for n, d in enumerate(bad):
            with self.subTest(n=n), self.assertRaises(SystemExit):
                self.run_review(d, 'bad%d' % n)

    def test_issue_without_box_gets_no_dot_and_text_is_escaped_in_data(self):
        i = issue('DR-001', '1:5'); del i['box']; i['evidence'] = '</script><b>'
        out, html = self.run_review(review('2026-11-01', [i]), 'a')
        self.assertNotIn('class="dot', html)
        self.assertNotIn('</script><b>', html)
        self.assertEqual(review_html.read_embedded(out)['issues'][0]['evidence'], '</script><b>')

    def test_missing_image_fails_clearly(self):
        d = review('2026-11-01', [], screens=('9:9',))
        with self.assertRaises(SystemExit):
            self.run_review(d, 'a')


if __name__ == '__main__':
    unittest.main()
