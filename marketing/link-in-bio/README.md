# Link-in-Bio-Seite für Sarah

_Stand: 2026-11-28 · fertig gebaut und getestet, **noch nicht online**. Es fehlt nur der Upload auf den Webspace._

## Was wo liegt

- **Fertige Seite zum Hochladen:** `marketing/link-in-bio/final/` (13 Dateien, etwa 0,5 MB: `index.html`, `img/`, `fonts/`)
- **Vorschau zum Durchklicken:** https://claude.ai/artifact/1SvqgiX5giq7Zi7qj72qGz (privat, Player ohne Ton)
- **Quelle:** `index.html` (Vorschau) und `build.py` (baut daraus `final/`). Die Originalfotos von Sarah liegen in `img/`.

## So kommt die Seite online (René, etwa 5 Minuten)

1. Auf dem Webspace von brandyourvoice.de (WebGo) im Hauptordner der Website einen Ordner **`links`** anlegen.
2. Den **Inhalt** von `final/` dort hochladen: `index.html`, Ordner `img`, Ordner `fonts`.
3. `https://brandyourvoice.de/links/` im Browser öffnen und prüfen: Fotos da, Podcast spielt ab, Kacheln lassen sich wischen.
4. Diese Adresse bei Instagram als Link im Profil eintragen.

Die Seite muss auf **brandyourvoice.de** liegen. Nur dort kann sie die neueste Folge automatisch lesen (siehe unten). Falls es in WordPress schon eine Seite mit der Adresse `/links/` gibt, einen anderen Ordnernamen nehmen und in `build.py` die Adresse des Vorschaubilds anpassen.

## Aufbau

1. **Startbild:** Schwarz-Weiß-Porträt, darauf „Hi, I'm Sarah.“ und „Unternehmerin · Mentorin · Speakerin“
2. **Links:** LinkedIn („Lass uns connecten“), dann Website
3. **Podcast:** neueste Folge mit Player, dazu „Alle Folgen“, Spotify, Apple Podcasts
4. **Kacheln zum Wischen:** 0-€-Copywriting-Masterclass, Erfolgsgeschichten, Newsletter „Prosecco-Date“, alle mit abgedunkeltem Foto
5. **Rosé-Textfeld:** „DAFÜR GEHEN WIR HIER LOS“, „… für ein Leben, in dem du tun kannst, whatever the f*** YOU WANT!“, „Hier gibt’s kein Entweder-oder. Wir entscheiden uns für das UND. Okay, girl?“
6. **Fuß:** Impressum, Datenschutz

Farben: aktuelle Brandfarben (`firma/guidelines.md`).

## Technik

- **Neueste Folge:** Die Seite liest beim Öffnen `brandyourvoice.de/podcast/` und nimmt die Folge mit dem jüngsten Datum aus den Daten des Podcast-Plugins. Klappt das nicht, bleibt die zuletzt eingetragene Folge stehen (#132, Stand 28.11.2026). Wird das Podcast-Plugin oder die Seite `/podcast/` umgebaut, muss das hier angepasst werden.
- **Keine Abrufe bei Dritten beim Laden:** Schriften und Bilder liegen im eigenen Ordner, kein Google Fonts, kein Tracking, keine Cookies. Die Audiodatei kommt erst nach dem Klick auf Play von Podigee, wie auf der Podcast-Seite.
- **Suchmaschinen:** Die Seite ist auf „nicht indexieren“ gestellt.
- **Schriften:** Playfair Display und Open Sans. Goldney und Harlow Duo Serif sind nicht eingebaut, dafür werden die Schriftdateien gebraucht.

## Getestet am 28.11.2026 (lokal, Handybreite 400 px)

- Layout ohne seitliches Scrollen, alle Schriften geladen, Reihenfolge der Links, Wischen mit Pfeilen und Punkten
- Einlesen der neuesten Folge aus einer Kopie der echten Podcast-Seite, auch mit einer testweise eingefügten neueren Folge
- Player mit einer Test-Tondatei: Play, Pause, Zeit und Regler
- Rückfall auf #132, wenn die Podcast-Seite nicht erreichbar ist

**Nicht getestet:** das Abspielen der echten Folge von Podigee (in der Cloud-Sitzung gesperrt), die Seite auf dem echten Webspace und in der Instagram-App.

## Später ändern

Texte und Aufbau in `index.html` ändern, dann im Ordner `marketing/link-in-bio`:

```bash
python3 build.py <Ordner mit den woff2-Schriftdateien>
```

Die Schriftdateien stammen aus den npm-Paketen `@fontsource/playfair-display` und `@fontsource/open-sans`. Danach `final/` neu hochladen.
