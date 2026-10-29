# Second Brain von FPL Business — Installationsanleitung von Grund auf

> **Übersetzung** der spanischen Vorlage „Second Brain de FPL Business — guía de instalación desde cero“ (Version vom 18.10.2026). Original: [`docs/original/`](original/).
> In diesem Repo heißen Befehle und Dateien auf Deutsch. Die Zuordnung zur spanischen Vorlage steht am Ende unter [Namen im Original](#namen-im-original).

So richtest du das Second Brain von FPL Business in deiner Firma ein, mit deinem Konto und auf jedem beliebigen Computer: das Gedächtnis deiner Firma für Claude, mit Regeln, Sicherheitskontrollen und in der Praxis erprobten Befehlen. Ohne Daten irgendeiner anderen Firma, nur die Struktur.

**Kurz gesagt:** Du legst drei Konten an, kopierst die Vorlage mit einem Klick auf GitHub, verbindest zwei Dinge, wählst die Cloud-Umgebung und schreibst einen Satz. Claude macht den Rest und fragt dich, was es braucht. Zeitaufwand: 30–45 Minuten Installation + das Interview (2–3 Blöcke pro Sitzung, insgesamt etwa 4–6 Sitzungen).

**Vorlage (ein Klick):** https://github.com/finanzasparalatinos/secondbrain-template

---

## 1. Was es ist und wie es funktioniert

Das Second Brain hat drei Teile:

| Teil | Was es ist | Wo es liegt |
|---|---|---|
| Gedächtnis | das gesamte Wissen der Firma in Textdateien: Angebot, Wunschkunde, Tonfall, Vertrieb, Team, Prozesse, Entscheidungen | ein privates Repository auf GitHub |
| Regeln und Befehle | die „Verfassung“ (CLAUDE.md), automatische Sicherheitskontrollen und die Befehle `/second-brain-interview`, `/uebergabe`, `/agent-erstellen` | im selben Repository (`.claude/`) |
| Verbindungen | Zugriff auf Gmail, Drive, Kalender, CRM, jede Person mit ihrem eigenen Login | in deinem Claude-Konto (Konnektoren) |
| Cloud-Umgebung | der „Computer in der Cloud“, auf dem Claude mit dem Repository arbeitet | in deinem Claude-Konto (claude.ai/code) |

Jedes Mal, wenn jemand eine Claude-Code-Sitzung mit diesem Repository öffnet, liest Claude die Regeln, kennt die Firma und arbeitet mit demselben Stand wie das ganze Team.

**Was die Vorlage mitbringt:**

- `CLAUDE.md` — Verfassung mit Platzhaltern `{{…}}` (die Installation füllt sie aus)
- `INSTALLIEREN.md` — Skript, dem Claude folgt, um alles zu installieren
- `INDEX.md` — Landkarte des Gedächtnisses
- `OFFENE-FRAGEN.md` — offene Fragen
- `ENTSCHEIDUNGEN.md` — Entscheidungen mit Begründung
- `STATUS.md` — erledigt / offen
- `uebergaben/` — Übergaben zwischen Sitzungen
- `mcp-beispiel.json` — Beispiel für die Anbindung an das CRM GoHighLevel (optional)
- `.claude/` (im ZIP: `_claude/`) — `settings.json` (Sperre gefährlicher Befehle + Hinweis beim Sitzungsstart), `hooks/` (die zwei automatischen Kontrollen), `skills/` (Interview, Übergabe, Agent erstellen)
- `ANLEITUNG.md` — diese Anleitung · `vorlage-geschaeftsfuehrung/CLAUDE.md` — privater Bereich der Geschäftsführung (optional)

---

## 2. Was du brauchst

| Was | Wofür | Kosten | Pflicht |
|---|---|---|---|
| Claude-Konto mit Claude Code (Pro, Max, Team oder Enterprise; für ein Team: Team) | der Assistent | je nach Plan — siehe claude.com/pricing | ja |
| GitHub-Konto + eine Organisation der Firma | das Gedächtnis speichern | kostenlos | ja |
| Google Workspace (Gmail, Drive, Kalender) | vorhandene Dokumente und E-Mails lesen, Routinen | was ihr schon habt | empfohlen |
| CRM (z. B. GoHighLevel, HubSpot) | Kunden und Verkaufschancen | was ihr schon habt | optional |
| Browser (Chrome, Edge, Safari) | alles läuft im Web | — | ja |
| Claude-App (Desktop oder Handy) | vom Handy oder Computer aus arbeiten, per Mikrofon diktieren | kostenlos | optional |

Auf dem Computer muss nichts installiert werden: Claude Code arbeitet in der Cloud (claude.ai/code). Programmieren können muss man auch nicht.

---

## 3. Schritt für Schritt

### Schritt 1 — Claude-Konto

1. Geh auf https://claude.ai und lege das Konto mit der Firmen-E-Mail an.
2. Wähle einen Plan, der Claude Code enthält. Wenn ein Team arbeitet: den Team-Plan, dann hat jede Person ihr eigenes Login und ihre eigenen Verbindungen.
3. Prüfe, dass sich https://claude.ai/code öffnet.

### Schritt 2 und 3 — Schnelle Variante: ein Klick mit der Vorlage (empfohlen)

1. Lege ein Konto auf https://github.com an und eine Organisation der Firma (dein Profilbild → **Your organizations** → **New organization** → Plan **Free**).
2. Öffne die Vorlage: https://github.com/finanzasparalatinos/secondbrain-template
3. Grüner Button **Use this template** → **Create a new repository**.
4. Owner: deine Organisation · Name: z. B. `firma-gedaechtnis` · **Private** (wichtig!) → **Create repository**.

Fertig: Das Repository enthält schon alles (auch den Ordner `.claude`). Weiter mit **Schritt 4**. Wenn du den Button „Use this template“ nicht siehst, nimm die manuelle Variante mit dem ZIP weiter unten.

### Schritt 2 (manuelle Variante) — GitHub: Organisation und Repository

1. Lege ein Konto auf https://github.com an (falls noch keins existiert).
2. Oben rechts: dein Profilbild → **Your organizations** → **New organization** → Plan **Free**. Name: der der Firma.
3. In der Organisation: **New repository** · Name z. B. `firma-gedaechtnis` · **Private** (wichtig!) · **Add a README file** anhaken · **Create repository**.

### Schritt 3 (manuelle Variante) — Die Vorlage hochladen

1. Lade `second-brain-vorlage.zip` herunter (bekommst du von FPL Business) und entpacke es.
2. In deinem GitHub-Repository: **Add file** → **Upload files**.
3. Öffne den entpackten Ordner `second-brain/vorlage`, markiere **alles, was darin liegt** (nicht den Ordner selbst) und zieh es auf die Seite.
4. Unten: **Commit directly to the main branch** → **Commit changes**.
5. Prüfe, dass auf GitHub `CLAUDE.md`, `INSTALLIEREN.md` und der Ordner `_claude` erscheinen.

Warum `_claude` mit Unterstrich? Ordner, die mit einem Punkt beginnen, gehen beim Hochladen über das Web manchmal verloren. Die Installation benennt ihn von selbst in `.claude` um.

### Schritt 4 — GitHub mit Claude verbinden

1. Öffne https://claude.ai/connect-github und melde dich mit GitHub an.
2. Installiere die **Claude GitHub App** in deiner Organisation.
3. Unter **Repository access** wähle **Only select repositories** → dein Repository `firma-gedaechtnis`. (Nur das: Claude muss nicht mehr sehen.)
4. Wenn du nicht Eigentümerin der Organisation bist, bitte die Person, der sie gehört, die App zu installieren.

### Schritt 5 — Konnektoren (Gmail, Drive, Kalender, CRM)

1. Öffne https://claude.ai/customize/connectors.
2. Verbinde **Google Drive**, **Gmail** und **Google Calendar** — jeweils mit **deinem eigenen** Google-Login.
3. CRM: **HubSpot, Salesforce, Pipedrive oder ein anderes mit Konnektor:** auf derselben Seite verbinden. **GoHighLevel:** wird über Variablen in der Umgebung verbunden (Schritt 6).
4. Nützlich, optional: **Canva** (Designs), **Slack** oder **Notion**, falls ihr sie nutzt.
5. Jede Person im Team verbindet **ihre eigenen** Konten. Passwörter werden nie geteilt.

Die Konnektoren werden beim **Start** einer Sitzung gelesen. Wenn du etwas Neues verbindest, öffne eine neue Sitzung.

### Schritt 6 — Cloud-Umgebung (Pflicht, nur einmal)

Die Umgebung ist der „Computer in der Cloud“, auf dem Claude mit deinem Repository arbeitet. Ohne Umgebung kann keine Sitzung starten.

1. Öffne https://claude.ai/code.
2. **Das erste Mal in Claude Code:** Mit dem Plan **Pro oder Max** wird die Umgebung **Default** automatisch angelegt (weiter mit Punkt 3). Mit dem Plan **Team oder Enterprise** erscheint das Formular **Create your first cloud environment**: alles so lassen, wie es ist (Netzwerkzugriff **Trusted**, keine Variablen, kein Skript) und **Create & finish** drücken.
3. Auf dem Bildschirm für eine neue Sitzung gibt es unter dem Nachrichtenfeld eine Reihe von Auswahlfeldern. **Repository:** wähle dein Gedächtnis-Repository (z. B. `firma-gedaechtnis`); wenn es nicht erscheint, zurück zu Schritt 4. **Umgebung** (das erste Auswahlfeld der Reihe): prüfe, dass dort **Default** steht. Wenn es keine gibt: **New environment** → Name `Default` · Netzwerkzugriff **Trusted** → **Add environment**.
4. Fertig. Mehr braucht es nicht: Das Second Brain braucht weder Variablen noch ein Installationsskript.

Die Auswahl der Umgebung erscheint nur, **bevor** du die erste Nachricht schickst. Um die Umgebung einer schon geöffneten Sitzung zu ändern: Pfeil neben dem Titel der Sitzung → **Edit cloud environment**.

**Nur wenn du GoHighLevel nutzt:** Öffne die Umgebung zum Bearbeiten (in der Auswahl mit der Maus über **Default** fahren → Zahnrad-Symbol; oder in einer offenen Sitzung: Pfeil neben dem Titel → **Edit cloud environment**) und füge unter **Environment variables** hinzu: `GHL_PIT` = das Private Integration Token von GoHighLevel (Settings → Private Integrations → Token nur mit den nötigen Berechtigungen anlegen; möglichst nur Lesen) und `GHL_LOCATION_ID` = die ID deines Unterkontos (Settings → Business Profile). Speichern und eine neue Sitzung öffnen.

**Niemals** ein Token oder Passwort in den Chat einfügen. Nur in die Umgebung. Offizielle Details: https://code.claude.com/docs/en/cloud-environments

### Schritt 7 — Die Installation (Claude arbeitet)

1. Auf https://claude.ai/code: **neue Sitzung** mit deinem Repository und der Umgebung **Default** (Schritt 6).
2. Schreib genau: **Lies INSTALLIEREN.md und folge den Anweisungen.**
3. Claude prüft die Verbindungen, stellt dir **6 Fragen** (siehe Abschnitt 5) und füllt die Verfassung aus.
4. Wenn es fragt „Soll ich das im Hauptzweig speichern?“ → antworte **ja**.

### Schritt 8 — Das Interview (das Gedächtnis aufbauen)

1. **Neue Sitzung** (damit Befehle und Kontrollen geladen werden).
2. Schreib: **/second-brain-interview** — Claude stellt sich als Assistent des Second Brain von FPL Business vor.
3. Claude fragt dich Block für Block (13 Blöcke, siehe Abschnitt 5). Eine Frage pro Nachricht. Du kannst schreiben oder diktieren.
4. Tipp: **Material vor Fragen.** Lade eure Website, Preisliste, Angebots-PDFs, 2–3 typische E-Mails und Bewertungen hoch. Claude liest sie und fragt nur, was fehlt.
5. Nach jedem Block antworte **ja** auf „Soll ich den Fortschritt im Hauptzweig speichern?“.
6. An einem anderen Tag weitermachen: neue Sitzung → `/second-brain-interview` (Claude macht da weiter, wo ihr aufgehört habt).

### Schritt 9 — Der Alltag

- Am Ende einer Sitzung: **/uebergabe** (hält fest, was gemacht wurde, was fehlt und was als Nächstes kommt).
- Immer wenn Claude vorschlägt, im Hauptzweig zu speichern: ja, wenn das Ergebnis stimmt. Was nur im Arbeitszweig bleibt, sieht niemand sonst.
- Wenn Claude beim Start vor „Arbeit in alten Zweigen“ warnt: entscheide, ob sie in den Hauptzweig übernommen wird.

### Schritt 10 — Team

1. Lade jede Person zu deinem Claude-Plan (Team) und zur GitHub-Organisation ein (mit Zugriff auf das Gedächtnis-Repository).
2. Jede Person macht die Schritte 4, 5 und 6 mit **ihren eigenen** Konten.
3. Teile dem Team mit: „Öffne claude.ai/code mit dem Repository `firma-gedaechtnis` und der Umgebung Default. Am Ende: /uebergabe.“

### Schritt 11 — Bereich der Geschäftsführung (optional, empfohlen)

Für Zahlen, Gehälter, Personal und Strategie: ein **zweites privates Repository** nur für die Geschäftsführung.

1. GitHub → **New repository** → `firma-geschaeftsfuehrung`, **Private**.
2. Lade `vorlage-geschaeftsfuehrung/CLAUDE.md` hoch (liegt in deinem Gedächtnis-Repository) und ersetze die `{{…}}` (oder bitte Claude darum, in einer Sitzung mit diesem Repository).
3. In der Claude GitHub App füge dieses Repository **nur** in den Konten der Geschäftsführung hinzu; auf GitHub gib nur der Geschäftsführung Zugriff.
4. Für Block 0b des Interviews öffne die Sitzung mit **beiden** Repositories.

### Schritt 12 — Agenten und Routinen (wenn das Gedächtnis fertig ist)

- **Agent:** `/agent-erstellen` — Claude führt ein Interview, baut den Steckbrief, testet ihn an 3 echten Fällen und holt dein Ja ein, bevor er in Betrieb geht.
- **Routine** (etwas, das von selbst läuft, z. B. jeden Morgen eine Zusammenfassung): Bitte Claude darum in einer Sitzung mit dem Repository (siehe Prompts, Abschnitt 4).

---

## 4. Alle Prompts (kopieren und einfügen)

| Moment | Prompt |
|---|---|
| Installieren | Lies INSTALLIEREN.md und folge den Anweisungen. |
| Interview beginnen / fortsetzen | /second-brain-interview |
| Material auf einmal geben | Ich lade dir unser Material hoch (Website, Preise, Angebote, E-Mails). Lies alles, sag mir pro Interview-Block, was du verstanden hast, und frag mich nur, was fehlt. |
| Einen Block überspringen | Diesen Block weiß ich gerade nicht. Notier ihn in OFFENE-FRAGEN.md und lass uns mit dem nächsten weitermachen. |
| Sitzung beenden | /uebergabe |
| Im Hauptzweig speichern | Speichere alles aus dieser Sitzung im Hauptzweig und prüfe, dass es angekommen ist. |
| Verbindungen prüfen | Prüfe, welche Verbindungen diese Sitzung wirklich hat (GitHub, Gmail, Drive, Kalender, CRM), und zeig sie mir in einer Tabelle. Nicht annehmen: prüfen. |
| Alte Zweige übernehmen | Zeig mir, welche Arbeit in alten Zweigen liegt, die nicht in main ist, eine Zeile pro Zweig, und schlag vor, welche übernommen werden soll. |
| Erster Agent | /agent-erstellen |
| Tägliche Routine | Erstelle eine Routine, die an jedem Werktag um 7:00 (Zeitzone Europe/Berlin) STATUS.md, OFFENE-FRAGEN.md und die Übergaben von gestern liest und mir eine Zusammenfassung in 5 Zeilen schreibt: was offen ist, was fällig wird, was zu entscheiden ist. Nur lesen, nichts versenden. |
| Routine mit E-Mail (Stufe A) | Wie die tägliche Routine, aber schick mir die Zusammenfassung per Gmail an [DEINE E-MAIL]. Bevor du sie anlegst, sag mir, was sie tun wird, was schiefgehen könnte und wie ich es prüfe. |
| Nach einem Fehler eine Regel hinzufügen | Das ist schiefgegangen: [WAS PASSIERT IST]. Korrigiere es, erklär mir die Ursache und hinterlege eine Regel, damit es nicht wieder passiert, in der passenden Datei. |
| Eine Entscheidung festhalten | Wir haben [WAS] entschieden, weil [GRUND]. Notier das in ENTSCHEIDUNGEN.md. |

---

## 5. Alle Fragen (um die Antworten vorher vorzubereiten)

### Installation (6 Fragen, INSTALLIEREN.md)

1. Name der Firma.
2. Wer gibt frei, was nach außen geht? Wer vertritt diese Person?
3. Sprache der Dokumente und Anrede (du / Sie).
4. Branche und rechtliche Regeln (was man nicht versprechen darf, Aufsichtsbehörde, Pflichtangaben).
5. Bereich der Geschäftsführung? Wie heißt er?
6. Welches CRM nutzt ihr?

### Interview (/second-brain-interview)

**Block 0 — Ziel und Engpass** → `firma/ziele-und-engpass.md`

- Wo steht die Firma heute? (ungefährer Umsatz, Kunden, Team)
- Wohin will sie — welche Zahl, bis wann?
- Was bricht als Erstes, wenn morgen zehn Kunden mehr kommen?
- Was hängt persönlich an dir, das sonst niemand kann?
- Was habt ihr ausprobiert, das nicht funktioniert hat?
- Was sollte in den ersten 14 Tagen gelöst sein?
- Darf dein Team dieses Ziel sehen?

**Block 0b — Dein Profil** (Bereich der Geschäftsführung) → `profil-geschaeftsfuehrung.md`

- Kurz und direkt oder ausführlich erklärt?
- Was nervt dich an den Antworten einer KI?
- Wo soll ich dir widersprechen?
- Was schiebst du vor dir her?
- Was gibt dir Energie und was raubt sie dir?

**Block 1 — Firma** → `firma/profil.md` (Claude liest vorher eure Website, das Impressum und Bewertungen)

- Die Geschichte der Firma in fünf Sätzen.
- Was macht ihr besser als andere, und woher weißt du das?
- Worauf seid ihr stolz, was würdet ihr heute anders machen?

**Block 2 — Wunschkunde** → `wunschkunde/wunschkunde.md`

- Eine echte Person, mit der es sehr gut läuft: wer sie ist, welches Problem sie hat, warum sie kauft.
- Welchen Kunden würdest du nie wieder annehmen — und warum?
- Woran merkst du im ersten Gespräch, ob jemand passt?

**Block 3 — Angebot** → `angebot/angebot.md` (Material: Preise, PDFs)

- Was kauft der Kunde, was bekommt er, was kostet es?
- Häufigster Einstieg und größtes Paket?
- Was wird oft angefragt, das ihr NICHT macht?
- Zusatzverkäufe an bestehende Kunden?

**Block 4 — Sprache** → `sprache/tonfall.md` (Material: 2–3 E-Mails)

- Du oder Sie mit den Kunden?
- Wie unterschreibt ihr? (genau)
- Welche Wörter oder Sätze willst du nie sehen?

**Block 5 — Branchenregeln** → `firma/branchenregeln.md`

- Was dürft ihr laut Gesetz nicht sagen oder versprechen?
- Aufsichtsbehörde, Pflichtangaben, vorgeschriebene Formulierungen?
- Was gehört unter jede E-Mail / auf jede Rechnung?

**Block 6 — Marketing** → `marketing/kanaele-und-erfahrungen.md`

- Über welche Wege kommen Anfragen, wie viele pro Monat?
- Was habt ihr ausprobiert, was hat funktioniert, was ist gescheitert und warum?
- Wofür gebt ihr Geld aus und wisst ihr, was es bringt?
- Welcher Kanal ist ungenutzt, obwohl er passen würde?

**Block 7 — Vertrieb** → `vertrieb/prozess-und-einwaende.md`

- Schritt für Schritt von „eine Anfrage kommt rein“ bis „wir haben den Auftrag“.
- Was sagst du als Erstes im ersten Gespräch?
- Die drei häufigsten Einwände und deine Antwort darauf.
- Warum scheitern Abschlüsse?

**Block 8 — Leistung** → `leistung/prozess.md`

- Nach der Unterschrift: Was passiert, in welcher Reihenfolge, bis zur Lieferung?
- Wo hakt es?
- Wiederkehrende Termine mit Kunden?

**Block 9 — Team** → `team/team.md`

- Wer arbeitet hier und was macht die Person?
- Wer entscheidet was, ohne dich zu fragen?
- Wer gibt frei, was nach außen geht, und wer vertritt?

**Block 10 — Programme und Daten** → `programme/systeme.md`

- Welche Programme nutzt ihr täglich?
- Wo liegt die Wahrheit, wenn sich zwei Programme widersprechen?
- Was wird doppelt gepflegt oder von Hand kopiert?

**Block 11 — Routinen** → `routinen/uebersicht.md`

- Was wiederholt sich täglich, wöchentlich, monatlich?
- Was kostet am meisten Zeit?
- Was machst du selbst, obwohl es jemand anderes machen könnte?

**Block K — Kundenstimmen** → `kundenstimmen/`

- Alles hochladen: Bewertungen, Dankes-E-Mails, Erfolgsgeschichten.

**Abschluss:** Claude schreibt den Spielplan (`firma/spielplan.md`: 3 Hebel, Reihenfolge, 3 schnelle Erfolge) und liest die offenen Punkte vor.

### Einen Agenten erstellen (/agent-erstellen)

1. Welcher Agent, welches Problem löst er?
2. Für wen arbeitet er und wer ist verantwortlich?
3. Woran merkst du, dass er gut ist (messbares Signal)?
4. Ein echtes Beispiel aus der letzten Woche und das perfekte Ergebnis.

Danach nur noch die Lücken: Berechtigungen, Format des Ergebnisses, Sub-Agenten, Rhythmus, Grenzfälle, drei Testfälle.

---

## 6. Die mitgelieferten Regeln (und warum)

Alle sind aus echten Fehlern in der Praxis entstanden:

| Regel | Warum |
|---|---|
| Stufen A/B/C: Was nach außen geht, immer mit Freigabe | eine falsche E-Mail kostet einen Kunden |
| Im Hauptzweig speichern, immer mit Nachfrage | ein fertiges Interview war 8 Tage unsichtbar in einem Arbeitszweig |
| Zuerst den neuesten Stand holen (`git fetch origin main`) | eine Sitzung sieht das Repository so, wie es beim Start war |
| Erst prüfen, dann sagen („ich habe keinen Zugriff“ eingeschlossen) | ein ungeprüftes „geht nicht“ bremst Arbeit, die eigentlich möglich war |
| Keine Zahl ohne Quelle | glaubwürdige Erfindungen vermeiden |
| Keine Passwörter und keine Kundenkontakte im Repository | ein Export enthielt E-Mail-Adressen von Kunden |
| Automatische Sperre gefährlicher Befehle | kein Löschen und kein Überschreiben ohne Weg zurück |
| Automatischer Hinweis auf Arbeit in alten Zweigen | damit nichts vergessen wird |

---

## 7. Abschluss-Checkliste

- [ ] Claude mit Claude Code funktioniert (claude.ai/code).
- [ ] Privates Repository auf GitHub mit der Vorlage.
- [ ] Claude GitHub App installiert, nur für dieses Repository.
- [ ] Gmail, Drive, Kalender (und CRM) mit eigenem Login verbunden.
- [ ] Cloud-Umgebung Default angelegt (Zugriff Trusted).
- [ ] „Lies INSTALLIEREN.md …“ ausgeführt, im Hauptzweig gespeichert.
- [ ] Auf GitHub: CLAUDE.md ohne `{{`, Ordner `.claude` existiert.
- [ ] Neue Sitzung: `/second-brain-interview` erscheint und startet.
- [ ] Team eingeladen; jede Person hat ihre Konten verbunden.

## 8. Häufige Probleme

| Problem | Lösung |
|---|---|
| `/second-brain-interview` erscheint nicht | eine neue Sitzung öffnen (Befehle werden beim Start geladen); auf GitHub prüfen, dass `.claude/skills/` in main existiert |
| Der Button „Use this template“ erscheint nicht | die Vorlage ist für dein Konto nicht sichtbar: nimm die manuelle Variante mit dem ZIP oder bitte FPL Business um Zugriff |
| Der Ordner `.claude` oder `_claude` fehlt auf GitHub | den Ordner `_claude` erneut hochladen (Schritt 3) und Schritt 7 wiederholen |
| Ich kann die erste Nachricht nicht senden / es gibt keine Umgebung | Umgebung anlegen (Schritt 6): Auswahl unter dem Nachrichtenfeld → New environment → Trusted → Add environment |
| Claude kann nicht speichern („push“ abgelehnt) | auf claude.ai/connect-github prüfen, dass die App Zugriff auf das Repository hat |
| Claude sieht Gmail / Drive / CRM nicht | auf claude.ai/customize/connectors verbinden und eine neue Sitzung öffnen; bei GoHighLevel die Variablen der Umgebung prüfen |
| Eine Sitzung sieht nicht, was eine andere gemacht hat | das der anderen liegt in ihrem Arbeitszweig: „übernimm die Arbeit aus Zweig X nach main“ |
| Etwas Sensibles wurde ins Repository geschrieben | Claude bitten, es zu entfernen und eine Regel zu hinterlegen; war es ein Passwort, im Programm ändern |

---

*Second Brain von FPL Business · Version vom 18.10.2026. Enthält nur Struktur und Regeln, keine Daten von Kunden oder anderen Firmen.*

---

## Namen im Original

| Hier (deutsch) | Spanische Vorlage |
|---|---|
| `/second-brain-interview` | `/entrevista-segundo-cerebro` |
| `/uebergabe` | `/traspaso` |
| `/agent-erstellen` | `/crear-agente` |
| `INSTALLIEREN.md` | `INSTALAR.md` |
| `INDEX.md` | `INDICE.md` |
| `OFFENE-FRAGEN.md` | `PENDIENTES.md` |
| `ENTSCHEIDUNGEN.md` | `DECISIONES.md` |
| `STATUS.md` | `ESTADO.md` |
| `uebergaben/` | `traspasos/` |
| `ANLEITUNG.md` | `GUIA.md` |
| `firma/`, `wunschkunde/`, `angebot/`, `sprache/`, `marketing/`, `vertrieb/`, `leistung/`, `team/`, `programme/`, `routinen/`, `kundenstimmen/` | `empresa/`, `cliente-ideal/`, `oferta/`, `lenguaje/`, `marketing/`, `ventas/`, `servicio/`, `equipo/`, `programas/`, `rutinas/`, `opiniones-clientes/` |

**In diesem Repo vorhanden:** `/second-brain-interview`, `/uebergabe`, `INDEX.md`, `OFFENE-FRAGEN.md`, `ENTSCHEIDUNGEN.md`, `STATUS.md`, `uebergaben/`. Die übrigen Teile der Original-Vorlage (`INSTALLIEREN.md`, `/agent-erstellen`, Hooks, Geschäftsführungs-Vorlage) sind hier noch nicht angelegt.
