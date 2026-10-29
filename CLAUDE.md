# Second Brain von Sarah & Julez

Dieses Repository ist unser gemeinsames Gedächtnis für Claude. Sarah und Julez arbeiten beide damit, jede in ihren eigenen Claude-Code-Sitzungen. Der gemeinsame Stand ist der Branch `main` auf GitHub.

## Sprache

Deutsch, per Du.

## Git: immer synchron bleiben (wichtigste Regel)

1. **Zu Beginn jeder Sitzung und vor jeder Änderung den neuesten Stand holen:**
   `git fetch origin main` und dann `git merge origin/main` (bzw. `git pull origin main`). Eine Sitzung sieht das Repository sonst nur so, wie es beim Start war.
2. **Alles, was Sarah oder Julez hineinschreiben, sofort committen und pushen** — ohne nachzufragen. Nach jedem abgeschlossenen Arbeitsschritt (z. B. ein Interview-Block, eine neue Notiz) committen und nach `main` pushen. Was nur im Arbeitszweig liegt, sieht die andere nicht.
3. Wenn die Sitzung auf einem eigenen Arbeitszweig läuft: dort committen und pushen **und** die Änderungen zusätzlich nach `main` bringen (`git push origin HEAD:main`, vorher `main` hineinmergen).
4. Bei Merge-Konflikten: beide Fassungen behalten und mit Namen markieren, nichts stillschweigend überschreiben; dann kurz nachfragen.
5. Commit-Nachrichten auf Deutsch, mit Namen, z. B. `Notiz Wunschkunde ergänzt (Sarah)`.
6. Nach dem Push prüfen, dass er angekommen ist (`git log origin/main -1`).

## Inhalt

- Anleitung (übersetzt aus dem Spanischen): `docs/second-brain-anleitung.md`
- Interview starten / fortsetzen: `/second-brain-interview`
- Sitzung beenden: `/uebergabe`
- Landkarte: `INDEX.md` · Status: `STATUS.md` · offene Fragen: `OFFENE-FRAGEN.md` · Entscheidungen: `ENTSCHEIDUNGEN.md` · Übergaben: `uebergaben/`

## Regeln

- Was nach außen geht (E-Mails, Nachrichten, Posts), nur mit ausdrücklicher Freigabe.
- Keine Zahl ohne Quelle — Schätzungen als solche kennzeichnen.
- Keine Passwörter, Tokens oder Kontaktdaten von Kunden im Repository.
- Erst prüfen, dann sagen — auch „ich habe keinen Zugriff“.
- Nichts löschen oder überschreiben, was die andere geschrieben hat; ergänzen mit Name und Datum.
- Entscheidungen mit Begründung in `ENTSCHEIDUNGEN.md` festhalten.
