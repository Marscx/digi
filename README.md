# digi.marcscheidegger.ch

Anleitungen und Präsentationen zum HSLU-Praxistag «Konzipieren, umsetzen, hosten» (Modul Digitalisierung).
Reines HTML und CSS, keine Abhängigkeiten, kein Build-Schritt.

- `index.html`: Startseite mit Übersicht der Anleitungen und Präsentationen
- `anleitungen/`: eine Seite pro Werkzeug (Basics, Installation, erste Schritte, kleine Umsetzung)
- `praesentationen/`: die beiden Präsentationen als einzelne HTML-Dateien (`tag-2.html` ohne lokales Ersatzvideo, das Video läuft über Vimeo)
- `marke.css`: gemeinsamer Auftritt mit marcscheidegger.ch (identisch mit den Übe-Tools)
- `anleitungen.css`: Gestaltung der Seiten, hell und dunkel

Bei Änderungen an CSS die Versionsnummer `?v=N` in den HTML-Seiten erhöhen.
Die Seiten sind per `.htaccess` und Meta-Tag für Suchmaschinen gesperrt (`noindex`).

Neue Anleitung: `anleitungen/noteflight.html` kopieren, Inhalt ersetzen, auf der Startseite die Karte von «Folgt» auf einen Link umstellen.

## Lizenz

Von [Marc Scheidegger](https://marcscheidegger.ch), entwickelt mit Claude (Anthropic),
lizenziert unter [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de).
