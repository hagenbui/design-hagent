# Standard app flows

Part of the design-hagent skill. Read when you write or check a sitemap, start or catch up an app, or run the done check items for these flows. SKILL.md still applies.

Every app sitemap includes these flows unless the brief rules one out. Mark each "to confirm" when the brief doesn't say. Ask the designer for a reference build if one helps.
- Language: a first-run step after Splash and before Onboarding (Language Option list, device language preselected, Continue in the bottom bar, no Back), and a Settings Language row (current language as trailing text) that opens a list where the choice applies right away, with no Save.
- Settings Support group, in this order: Feedback, Rate App, Invite Friends, Privacy Policy, About the Developer, then the app version.
- Rate App: "Enjoying [app]?" (Love it / Not really), then a star dialog (Rate disabled until a star is picked). 1 to 3 stars or Not really go to Feedback. 4 to 5 stars open the system store review prompt (iOS App Store, Google Play in-app review), which is system UI and drawn only as a labeled mock. An automatic ask only at a happy moment, never on app open, and within store limits.
- Feedback: a sheet with a multi-line field (Send disabled while empty), typed state, Thank you dialog, and a send-failed case with no internet (Try again, Cancel, message kept).
- Invite Friends: the system share sheet, no custom screen.
- App update: Update available (soft, Later and Update, at most once per version) and Update required (blocking, Update now only, no Back or Close).
- No internet: a full-screen state with Try again and a retrying state, plus inline offline cases for actions that need the network.
