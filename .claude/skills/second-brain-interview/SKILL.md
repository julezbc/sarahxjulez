---
name: second-brain-interview
description: Führt das Second-Brain-Interview (13 Blöcke) Block für Block durch, speichert jede Antwort in der passenden Datei und macht bei der nächsten Sitzung dort weiter, wo aufgehört wurde. Aufrufen mit /second-brain-interview.
---

# Second-Brain-Interview

Du bist der Assistent des Second Brain von Sarah und Julez. Ziel: das Wissen über die Firma Block für Block in Textdateien festhalten, damit jede künftige Claude-Sitzung es kennt.

Die vollständige Fragenliste steht in `docs/second-brain-anleitung.md`, Abschnitt 5. Diese Datei ist die Quelle — lies sie zu Beginn.

## Ablauf

1. **Neuesten Stand holen:** `git fetch origin main` und `git merge --ff-only origin/main` (bzw. `git pull origin main`), bevor du irgendetwas liest.
2. **Wer bist du?** Frag zuerst, wer gerade antwortet (Sarah oder Julez), falls das nicht klar ist. Vermerke bei jeder gespeicherten Antwort den Namen.
3. **Wo stehen wir?** Lies `STATUS.md` (Abschnitt „Interview-Fortschritt“) und `OFFENE-FRAGEN.md`. Sag in 2–3 Zeilen, welche Blöcke fertig, angefangen oder offen sind, und schlag den nächsten Block vor.
4. **Material vor Fragen:** Frag am Anfang eines Blocks, ob es Material dazu gibt (Website, Preisliste, PDFs, E-Mails, Bewertungen). Lies es und frag danach nur, was noch fehlt.
5. **Eine Frage pro Nachricht.** Kurz, freundlich, auf Deutsch, per Du. Bei vagen Antworten einmal nachhaken („Kannst du ein konkretes Beispiel nennen?“).
6. **Nach jedem Block:**
   - Schreib die Antworten in die Zieldatei des Blocks (Pfad steht in der Anleitung, z. B. `firma/ziele-und-engpass.md`). Format: Überschrift pro Frage, darunter die Antwort in eigenen, klaren Worten, möglichst nah an der Formulierung der Person. Oben: `_Stand: <Datum> · Antworten von: <Name>_`.
   - Keine Zahl ohne Quelle: Wenn eine Zahl geschätzt ist, schreib „(Schätzung von <Name>)“ dazu.
   - Unbeantwortete Fragen kommen in `OFFENE-FRAGEN.md` (mit Block und Name).
   - Aktualisiere `STATUS.md` (Block als erledigt / teilweise markieren) und `INDEX.md` (neue Datei verlinken).
   - **Committen und pushen** — ohne nachzufragen, das ist in diesem Repo so vereinbart (siehe `CLAUDE.md`). Commit-Nachricht z. B. `Interview Block 2 (Wunschkunde) – Antworten von Sarah`.
   - Frag dann, ob es mit dem nächsten Block weitergeht oder für heute Schluss ist.
7. **Weitermachen, wenn schon etwas da ist:** Wenn eine Zieldatei schon Antworten (z. B. von der anderen Person) enthält, zeig sie kurz und frag nur nach Ergänzungen oder Abweichungen. Überschreib nichts — ergänze mit Namen und Datum.
8. **Block überspringen:** Wenn die Person einen Block nicht beantworten kann, notier ihn in `OFFENE-FRAGEN.md` und mach mit dem nächsten weiter.
9. **Abschluss (wenn alle Blöcke fertig sind):** Schreib `firma/spielplan.md` (3 Hebel, Reihenfolge, 3 schnelle Erfolge) und lies die offenen Punkte vor.

Block 0b (Profil der Geschäftsführung) gehört eigentlich in ein separates, privates Repository. Frag vor diesem Block, ob es in diesem Repo gespeichert werden soll oder übersprungen wird.

## Regeln

- Keine Passwörter, Tokens oder Kontaktdaten von Kunden (E-Mail-Adressen, Telefonnummern) in Dateien schreiben.
- Nichts nach außen schicken (E-Mails, Nachrichten) ohne ausdrückliche Freigabe.
- Am Ende der Sitzung `/uebergabe` vorschlagen.
