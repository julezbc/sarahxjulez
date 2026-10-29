---
name: uebergabe
description: Schreibt am Ende einer Sitzung eine Übergabe (was gemacht wurde, was fehlt, was als Nächstes kommt) nach uebergaben/ und pusht sie, damit die andere Person nahtlos weitermachen kann. Aufrufen mit /uebergabe.
---

# Übergabe

1. Neuesten Stand holen: `git pull origin main`.
2. Lege `uebergaben/<JJJJ-MM-TT>-<name>.md` an (Name = wer die Sitzung geführt hat; bei mehreren am selben Tag `-2`, `-3` anhängen). Inhalt:
   - **Gemacht:** Stichpunkte, mit Links auf geänderte Dateien
   - **Offen:** was angefangen, aber nicht fertig ist
   - **Als Nächstes:** konkrete nächste Schritte, wer was macht
   - **Fragen an die andere Person:** falls es welche gibt
3. Aktualisiere `STATUS.md` (erledigt / offen).
4. Committen und pushen (siehe `CLAUDE.md`), dann prüfen, dass der Push angekommen ist.
5. Zum Schluss die Übergabe in 3–5 Zeilen im Chat zusammenfassen.
