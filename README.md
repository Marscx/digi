# digi.marcscheidegger.ch

Anleitungen und Präsentationen zum HSLU-Praxistag «Konzipieren, umsetzen, hosten» (Modul Digitalisierung).
Reines HTML und CSS, keine Abhängigkeiten. Die Seiten werden mit `python3 build.py` aus `guides.py` erzeugt.

- `index.html`: Startseite mit Übersicht der Anleitungen und Präsentationen
- `anleitungen/`: eine Seite pro Werkzeug (Basics, Installation, erste Schritte, kleine Umsetzung)
- `praesentationen/`: die beiden Präsentationen als einzelne HTML-Dateien (`tag-2.html` ohne lokales Ersatzvideo, das Video läuft über Vimeo)
- `marke.css`: gemeinsamer Auftritt mit marcscheidegger.ch (identisch mit den Übe-Tools)
- `anleitungen.css`: Gestaltung der Seiten, hell und dunkel

Bei Änderungen an CSS die Versionsnummer `?v=N` in den HTML-Seiten erhöhen.
Die Seiten sind per `.htaccess` und Meta-Tag für Suchmaschinen gesperrt (`noindex`).

Neue Anleitung: Eintrag in `guides.py` ergänzen (und in `GROUPS` einordnen), dann `python3 build.py` ausführen. Die Seiten und die Startseite werden daraus erzeugt.

## Lizenz

Von [Marc Scheidegger](https://marcscheidegger.ch), entwickelt mit Claude (Anthropic),
lizenziert unter [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de).
