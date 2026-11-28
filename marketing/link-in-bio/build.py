"""Baut aus dem Entwurf (index.html) die fertige Seite in final/.

Aufruf im Ordner marketing/link-in-bio:  python3 build.py <Ordner mit den woff2-Schriftdateien>

Unterschiede zur Vorschau:
- vollständiges HTML-Dokument mit Titel, Beschreibung und Vorschaubild für geteilte Links
- Schriften liegen im Ordner fonts/ (kein Abruf bei Google)
- Bilder verkleinert im Ordner img/
- echter Podcast-Player, der die neueste Folge von /podcast/ auf derselben Domain liest
"""
import pathlib
import shutil
import sys

from PIL import Image

HIER = pathlib.Path(__file__).parent
ZIEL = HIER / "final"
SCHRIFTEN = pathlib.Path(sys.argv[1])

BILDER = {  # Quelle im Entwurf -> Name auf der fertigen Seite
    "img/sarah-sw.jpg": "img/start.jpg",
    "img/sarah-laptop.png": "img/masterclass.jpg",
    "img/gruppe.webp": "img/erfolgsgeschichten.jpg",
    "img/sarah-gehend.jpg": "img/prosecco-date.jpg",
}
FONTS = [  # (Familie, Datei, Gewicht, Stil)
    ("Playfair Display", "playfair-display-latin-400-normal.woff2", 400, "normal"),
    ("Playfair Display", "playfair-display-latin-400-italic.woff2", 400, "italic"),
    ("Playfair Display", "playfair-display-latin-500-normal.woff2", 500, "normal"),
    ("Open Sans", "open-sans-latin-400-normal.woff2", 400, "normal"),
    ("Open Sans", "open-sans-latin-600-normal.woff2", 600, "normal"),
]

# Letzter bekannter Stand, falls /podcast/ nicht gelesen werden kann
FOLGE = {
    "title": "#132 Dein Matcha ist keine Altersvorsorge",
    "src": "https://audio.podigee-cdn.net/2644729-m-f37c7adbfc87c702767dca8f571a06a5.mp3?source=feed",
    "duration": "15:42",
}

PLAYER_HTML = """      <div class="spieler">
        <button class="play" type="button" id="play" aria-label="Folge abspielen" aria-pressed="false">
          <svg viewBox="0 0 24 24" fill="currentColor" id="play-icon"><path d="M7 4.500v15l13-7.500z"/></svg>
        </button>
        <div class="spur">
          <input class="regler" type="range" id="regler" min="0" max="1000" value="0" step="1" aria-label="Position in der Folge">
          <p class="hinweis"><span id="zeit">0:00</span> / <span id="dauer">%(duration)s</span></p>
        </div>
      </div>
""" % FOLGE

PLAYER_CSS = """  .regler { -webkit-appearance: none; appearance: none; width: 100%; height: 22px; margin: 0; background: transparent; cursor: pointer; --p: 0%; }
  .regler::-webkit-slider-runnable-track { height: 5px; border-radius: 99px; background: linear-gradient(to right, var(--rose) var(--p), var(--auf-dunkel-leise) var(--p)); }
  .regler::-moz-range-track { height: 5px; border-radius: 99px; background: var(--auf-dunkel-leise); }
  .regler::-moz-range-progress { height: 5px; border-radius: 99px; background: var(--rose); }
  .regler::-webkit-slider-thumb { -webkit-appearance: none; width: 15px; height: 15px; border-radius: 50%; background: var(--rose); margin-top: -5px; }
  .regler::-moz-range-thumb { width: 15px; height: 15px; border: 0; border-radius: 50%; background: var(--rose); }
  .hinweis { font-variant-numeric: tabular-nums; }
"""

PLAYER_JS = """  // Podcast: echter Player. Die neueste Folge kommt von /podcast/ auf derselben Domain.
  const FOLGE = %(folge)s;
  const play = document.getElementById('play'), icon = document.getElementById('play-icon');
  const regler = document.getElementById('regler'), zeit = document.getElementById('zeit'), dauer = document.getElementById('dauer');
  const titel = document.getElementById('t-podcast');
  const audio = new Audio();
  audio.preload = 'none';
  let folge = FOLGE;

  const mmss = s => { s = Math.max(0, Math.floor(s)); const h = Math.floor(s / 3600), m = Math.floor(s %% 3600 / 60), r = String(s %% 60).padStart(2, '0'); return h ? h + ':' + String(m).padStart(2, '0') + ':' + r : m + ':' + r; };
  const klartext = t => { const e = document.createElement('textarea'); e.innerHTML = t; return e.value; };
  function zeige(f) { folge = f; titel.textContent = f.title; if (f.duration) dauer.textContent = f.duration; }
  function knopf(an) {
    play.setAttribute('aria-pressed', an);
    play.setAttribute('aria-label', an ? 'Folge pausieren' : 'Folge abspielen');
    icon.innerHTML = an ? '<path d="M7 4.500h3.500v15H7zM13.500 4.500H17v15h-3.500z"/>' : '<path d="M7 4.500v15l13-7.500z"/>';
  }
  play.addEventListener('click', () => {
    if (!audio.src) audio.src = folge.src;
    if (audio.paused) audio.play().catch(() => knopf(false)); else audio.pause();
  });
  audio.addEventListener('play', () => knopf(true));
  audio.addEventListener('pause', () => knopf(false));
  audio.addEventListener('ended', () => knopf(false));
  audio.addEventListener('loadedmetadata', () => { if (isFinite(audio.duration)) dauer.textContent = mmss(audio.duration); });
  audio.addEventListener('timeupdate', () => {
    zeit.textContent = mmss(audio.currentTime);
    if (isFinite(audio.duration) && audio.duration > 0) { regler.value = audio.currentTime / audio.duration * 1000; regler.style.setProperty('--p', regler.value / 10 + '%%'); }
  });
  regler.addEventListener('input', () => {
    regler.style.setProperty('--p', regler.value / 10 + '%%');
    if (isFinite(audio.duration) && audio.duration > 0) audio.currentTime = regler.value / 1000 * audio.duration;
  });

  (async () => {
    try {
      const antwort = await fetch('/podcast/', { credentials: 'omit' });
      if (!antwort.ok) return;
      const seite = await antwort.text();
      const von = seite.indexOf('var podcastPlayerData');
      if (von < 0) return;
      // Das Datenobjekt endet an der Klammer, die zur ersten öffnenden passt (Klammern in Texten zählen nicht).
      const start = seite.indexOf('{', von);
      let tiefe = 0, imText = false, ende = -1;
      for (let i = start; i < seite.length; i++) {
        const z = seite[i];
        if (imText) { if (z === '\\\\') i++; else if (z === '"') imText = false; continue; }
        if (z === '"') imText = true;
        else if (z === '{') tiefe++;
        else if (z === '}' && --tiefe === 0) { ende = i; break; }
      }
      if (ende < 0) return;
      const daten = JSON.parse(seite.slice(start, ende + 1));
      let neu = null;
      for (const gruppe of Object.values(daten)) {
        if (!gruppe || typeof gruppe !== 'object') continue;
        for (const f of Object.values(gruppe)) if (f && f.src && f.timestamp && (!neu || f.timestamp > neu.timestamp)) neu = f;
      }
      if (neu && audio.paused && !audio.src) zeige({ title: klartext(neu.title), src: neu.src, duration: neu.duration });
    } catch (fehler) { /* dann bleibt die zuletzt bekannte Folge stehen */ }
  })();
"""


def zwischen(text, start, ende):
    a = text.index(start)
    b = text.index(ende, a)
    return a, b


def main():
    import json

    s = (HIER / "index.html").read_text(encoding="utf-8")

    # Kopfzeilen der Vorschau entfernen
    for zeile in s.splitlines()[:3]:
        assert zeile.startswith(("<title>", "<meta", "<link")), zeile
    s = s.split("\n", 3)[3]

    # Schriften
    faces = "".join(
        "  @font-face { font-family: \"%s\"; src: url(fonts/%s) format(\"woff2\"); font-weight: %d; font-style: %s; font-display: swap; }\n"
        % f for f in FONTS
    )
    s = s.replace("<style>\n", "<style>\n" + faces, 1)

    # Bilder
    for alt, neu in BILDER.items():
        assert alt in s, alt
        s = s.replace(alt, neu)

    # Player: Markup, CSS, Skript
    a, b = zwischen(s, '      <div class="spieler">', '      <div class="wo">')
    s = s[:a] + PLAYER_HTML + s[b:]
    a, b = zwischen(s, "  .balken {", "  .hinweis {")
    s = s[:a] + PLAYER_CSS + s[b:]
    a, b = zwischen(s, "  // Podcast:", "</script>")
    s = s[:a] + PLAYER_JS % {"folge": json.dumps(FOLGE, ensure_ascii=False)} + s[b:]
    assert "Vorschau ohne Ton" not in s and "Entwurf" not in s

    kopf = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Sarah | brandyourvoice</title>
<meta name="description" content="Unternehmerin, Mentorin, Speakerin. Alle Links von Sarah: Podcast, Masterclass, Erfolgsgeschichten und Newsletter.">
<meta name="robots" content="noindex">
<meta property="og:title" content="Sarah | brandyourvoice">
<meta property="og:description" content="Unternehmerin · Mentorin · Speakerin">
<meta property="og:image" content="https://brandyourvoice.de/links/img/start.jpg">
<meta name="theme-color" content="#fffbfa">
<style>html { color-scheme: light; } body { margin: 0; } img { max-width: 100%; } [hidden] { display: none !important; }</style>
</head>
<body>
"""
    ZIEL.mkdir(exist_ok=True)
    (ZIEL / "index.html").write_text(kopf + s + "</body>\n</html>\n", encoding="utf-8")

    (ZIEL / "img").mkdir(exist_ok=True)
    for alt, neu in BILDER.items():
        bild = Image.open(HIER / alt).convert("RGB")
        bild.thumbnail((1000, 1500))
        bild.save(ZIEL / neu, "JPEG", quality=84, optimize=True, progressive=True)

    (ZIEL / "fonts").mkdir(exist_ok=True)
    for _, datei, _, _ in FONTS:
        shutil.copy(next(SCHRIFTEN.rglob(datei)), ZIEL / "fonts" / datei)

    print("fertig:", sorted(str(p.relative_to(ZIEL)) for p in ZIEL.rglob("*") if p.is_file()))


main()
