# Routine: Zoom-Calls mit Sarah ins Second Brain

_Angelegt von Claude für Julez, 2026-11-12. Diesen Text als Prompt in einer Routine auf claude.ai verwenden (Repository `julezbc/sarahxjulez` auswählen, Connector **Zoom for Claude** freigeben, „neue Sitzung bei jedem Lauf“). Vorschlag: täglich 20:47 Uhr (Europe/Berlin)._

---

Aufgabe: Zoom-Meetings von Julez mit Sarah (Brand Your Voice, Konto info@brandyourvoice.de) ins Second Brain im Repository julezbc/sarahxjulez übernehmen. Sprache Deutsch, per Du. Lies zuerst CLAUDE.md im Repo und halte dich daran.

1. Repo aktualisieren: `git fetch origin main && git checkout -B main origin/main`.
2. Mit dem Zoom-Connector (`recordings_list`) die Cloud-Aufnahmen der letzten 3 Tage abrufen (Zeitzone Europe/Berlin). Falls der Zoom-Connector nicht verfügbar ist: nichts ändern und genau das melden.
3. Für jede Aufnahme mit nennenswerter Dauer `get_meeting_assets` (meetingId = uuid) aufrufen. Ein Meeting zählt NUR, wenn laut Teilnehmerliste bzw. „Attendees“-Zeile der Zusammenfassung Sarah / „brandyourvoice“ / „BYV“ / info@brandyourvoice.de dabei war. Alle anderen Meetings von Julez (eigene Kundinnen, andere Projekte) NICHT speichern und nicht erwähnen, die sind vertraulich.
4. Duplikate vermeiden: In `notizen/` prüfen, ob das Meeting schon gespeichert ist (im Dateikopf steht „Zoom-UUID: …“, sonst Datum und Thema vergleichen). Schon gespeicherte überspringen.
5. Für jedes neue passende Meeting:
   - Transkript holen: `get_recording_resource` mit types=transcript. Falls leer, vermerken „kein Wortlaut-Transkript in Zoom“.
   - Mit Transkript: `notizen/JJJJ-MM-TT-<thema>-transkript.md` (Sprechername und Text).
   - Immer: `notizen/JJJJ-MM-TT-<thema>-zusammenfassung.md` mit Kopf (Quelle Zoom-KI, Datum/Uhrzeit deutsche Zeit, Teilnehmende, Zoom-UUID, Hinweis „KI-Zusammenfassung, Zahlen und Namen ungeprüft“), Kurzfassung, Nächste Schritte nach Person. Widersprüche markieren, nichts erfinden. Vorlage: `notizen/2026-11-10-sales-analyse-zusammenfassung.md`.
   - Keine Telefonnummern, E-Mail-Adressen oder Kontaktdaten von Kundinnen/Leads, keine Zoom-Links mit Tokens.
   - In `STATUS.md` unter „Erledigt“ eine Zeile mit Verweis ergänzen. Nichts löschen, was andere geschrieben haben.
6. Commit auf Deutsch, z. B. `Zoom-Call 12.11. mit Sarah gespeichert (Claude für Julez)`, dann `git push origin HEAD:main` und mit `git log origin/main -1` prüfen.
7. Kein neues Meeting: nichts committen, kurz „keine neuen Calls mit Sarah“ melden. Am Ende in 2–3 Sätzen zusammenfassen, was gespeichert wurde.
