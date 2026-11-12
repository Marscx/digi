#!/usr/bin/env python3
"""Baut die Startseite und alle Anleitungen von digi.marcscheidegger.ch.

Inhalte stehen in guides.py (eine Anleitung = ein Eintrag).
Aufruf:  python3 build.py
Danach die Dateien index.html und anleitungen/*.html committen.
Bei Änderungen an CSS die Konstante V erhöhen.
"""
import html
import os

from guides import GUIDES, GROUPS, SOON

V = 4                                   # Version der CSS-Dateien (?v=N)
HOME = "https://neu.marcscheidegger.ch"   # ÜBERGANG bis Livegang (nach 14.11.2026): "neu." entfernen
STAND = "November 2026"
HERE = os.path.dirname(os.path.abspath(__file__))


def head(title, desc, prefix):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="utf-8">
    <title>{html.escape(title)} · digi.marcscheidegger.ch</title>
    <meta name="description" content="{html.escape(desc)}">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex, nofollow">
    <meta name="theme-color" content="#0b1220">
    <link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="{prefix}marke.css?v=1">
    <link rel="stylesheet" href="{prefix}anleitungen.css?v={V}">
</head>
<body>
    <header class="ms-bar">
        <div class="ms-bar-inner">
            <a class="ms-brand" href="{HOME}/">Marc <span>Scheidegger</span></a>
            <nav aria-label="Hauptnavigation">
                <ul class="ms-nav">
                    <li><a href="{prefix}index.html"{' aria-current="page"' if prefix == '' else ''}>Start</a></li>
                    <li><a href="{prefix}index.html#anleitungen"{' aria-current="page"' if prefix else ''}>Anleitungen</a></li>
                    <li><a href="{prefix}index.html#praesentationen">Präsentationen</a></li>
                </ul>
            </nav>
        </div>
    </header>
"""


def foot():
    return f"""
    <footer class="ms-foot">
        <p>Von <a href="{HOME}/" target="_blank" rel="noopener">Marc Scheidegger</a>, entwickelt mit Claude (Anthropic) ·
        <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de" target="_blank" rel="noopener license">CC BY-NC-SA 4.0</a></p>
        <ul>
            <li><a href="{HOME}/impressum.html">Impressum</a></li>
            <li><a href="{HOME}/datenschutz.html">Datenschutz</a></li>
        </ul>
    </footer>
"""


CHECK_JS = """
    <script>
        // Häkchen der Checkliste im Browser merken (nur auf diesem Gerät)
        document.querySelectorAll('input[data-k]').forEach(function (c) {
            try { c.checked = localStorage.getItem('digi-' + c.dataset.k) === '1'; } catch (e) {}
            c.addEventListener('change', function () {
                try { localStorage.setItem('digi-' + c.dataset.k, c.checked ? '1' : '0'); } catch (e) {}
            });
        });

        // Kopieren-Knopf der Codefenster
        document.querySelectorAll('.code .copy').forEach(function (btn) {
            btn.addEventListener('click', function () {
                var text = btn.parentNode.querySelector('code').textContent;
                function ok() { btn.textContent = 'Kopiert'; btn.classList.add('done'); setTimeout(function () { btn.textContent = 'Kopieren'; btn.classList.remove('done'); }, 2000); }
                function fallback() {
                    var ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
                    document.body.appendChild(ta); ta.select();
                    try { document.execCommand('copy'); ok(); } catch (e) { btn.textContent = 'Markieren und Cmd/Strg+C'; }
                    document.body.removeChild(ta);
                }
                if (navigator.clipboard && window.isSecureContext) { navigator.clipboard.writeText(text).then(ok, fallback); } else { fallback(); }
            });
        });
    </script>
"""


def guide_page(g):
    out = [head(g["title_long"], g["lead"], "../")]
    out.append('    <main class="wrap">\n        <p class="crumbs"><a href="../index.html#anleitungen">&larr; Alle Anleitungen</a></p>\n')
    out.append('        <section class="hero">')
    out.append(f'            <p class="eyebrow">{g["eyebrow"]}</p>')
    out.append(f'            <h1>{g["title_long"]}</h1>')
    out.append(f'            <p class="lead">{g["lead"]}</p>')
    out.append('            <ul class="facts">')
    for label, key in (("Zeit", "zeit"), ("Schwierigkeit", "diff"), ("Gerät", "geraet"), ("Kosten", "kosten")):
        out.append(f'                <li><b>{label}</b><span>{g[key]}</span></li>')
    out.append('            </ul>')
    if not g.get("final"):
        out.append('            <p><span class="badge">Entwurf</span> Noch nicht von Hand getestet. Falls ein Menü anders heisst, gilt, was du auf dem Bildschirm siehst. Sag es Marc, dann wird die Anleitung korrigiert.</p>')
    if g.get("vorab"):
        out.append(f'            <div class="note"><b>Vorab einrichten</b>{g["vorab"].replace("<b>", "").replace("</b>", "")} So bleibt am Praxistag mehr Zeit zum Ausprobieren.</div>')
    out.append('            <ul class="toc">')
    for i, s in enumerate(g["steps"], 1):
        out.append(f'                <li><a href="#{s[0]}">{i} {s[1].split(":")[0]}</a></li>')
    out.append('                <li><a href="#stolper">Stolpersteine</a></li>')
    out.append('            </ul>')
    out.append('        </section>\n')
    for i, (sid, title, zeit, body) in enumerate(g["steps"], 1):
        out.append(f'        <section class="step" id="{sid}">')
        out.append(f'            <header><span class="step-num">{i}</span><h2>{title}</h2><span class="time">{zeit}</span></header>')
        out.append(body.strip("\n"))
        out.append('        </section>\n')
    out.append('        <section class="step" id="stolper">')
    out.append('            <header><span class="step-num">!</span><h2>Stolpersteine</h2></header>')
    out.append('            <ul>')
    for s in g["stolper"]:
        out.append(f'                <li>{s}</li>')
    out.append('            </ul>')
    out.append('        </section>\n')
    out.append('        <section class="sources">')
    if g["quellen"]:
        out.append('            <h3>Quellen</h3>\n            <ul>')
        for t, u in g["quellen"]:
            out.append(f'                <li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>')
        out.append('            </ul>')
    out.append(f'            <p>Stand: {STAND}.{"" if g.get("final") else " Noch nicht von Hand getestet."}</p>\n        </section>')
    out.append('    </main>')
    out.append(foot())
    out.append(CHECK_JS)
    out.append('</body>\n</html>\n')
    return "\n".join(out)


def card_done(g):
    tags = "".join(f'<span class="pill">{b}</span>' for b in g["bsp"])
    badge = '<span class="badge badge--ok">Fertig</span>' if g.get("final") else '<span class="badge">Entwurf</span>'
    return (f'                    <li class="card"><a class="card-link" href="anleitungen/{g["slug"]}.html">{g["title"]}</a>'
            f'<p>{g["card"]}</p><div class="meta">{badge}'
            f'<span class="pill">{g["diff_kurz"]}</span>{tags}</div></li>')


def card_soon(s):
    tags = "".join(f'<span class="pill">{b}</span>' for b in s.get("bsp", []))
    return (f'                    <li class="card card--soon"><b>{s["title"]}</b><p>{s["card"]}</p>'
            f'<div class="meta"><span class="badge badge--soft">Folgt</span><span class="pill">{s["diff"]}</span>{tags}</div></li>')


def index_page():
    out = [head("Digitale Werkzeuge für Musikvermittlung",
                "Anleitungen und Präsentationen zum HSLU-Praxistag: konzipieren, umsetzen, hosten.", "")]
    out.append("""
    <main class="wrap wrap--wide">
        <section class="hero">
            <p class="eyebrow">HSLU · Modul Digitalisierung · Praxistag</p>
            <h1>Konzipieren, umsetzen, hosten</h1>
            <p class="lead">Anleitungen zu den Werkzeugen aus den Beispielen, jede in vier Schritten: Basics, Installation, erste Schritte, kleine Umsetzung. Dazu die Präsentationen der beiden Tage.</p>
        </section>

        <section id="praesentationen">
            <h2>Präsentationen</h2>
            <div class="big-links">
                <a class="big-link" href="praesentationen/tag-2.html"><b>Tag 2: Konzipieren, umsetzen, hosten</b><span>Die Präsentation vom 14. November mit den acht Beispielen. Pfeiltasten zum Blättern, <kbd>N</kbd> zeigt das Drehbuch.</span></a>
                <a class="big-link" href="praesentationen/tag-1.html"><b>Tag 1</b><span>Die Präsentation vom ersten Tag.</span></a>
            </div>
        </section>

        <section id="anleitungen">
            <h2>Anleitungen</h2>
            <p class="lead">«Fertig» heisst, die Anleitung ist von Hand getestet. «Entwurf» heisst, sie ist geschrieben, aber noch nicht getestet. Falls ein Menü anders heisst, gilt, was du auf dem Bildschirm siehst.</p>
""")
    by_slug = {g["slug"]: g for g in GUIDES}
    for gtitle, gsub, items in GROUPS:
        out.append('            <div class="group">')
        out.append(f'                <h2>{gtitle} <small>{gsub}</small></h2>')
        out.append('                <ul class="cards">')
        for it in items:
            out.append(card_done(by_slug[it]) if it in by_slug else card_soon(SOON[it]))
        out.append('                </ul>')
        out.append('            </div>\n')
    out.append('        </section>\n    </main>')
    out.append(foot())
    out.append('</body>\n</html>\n')
    return "\n".join(out)


def main():
    os.makedirs(os.path.join(HERE, "anleitungen"), exist_ok=True)
    for g in GUIDES:
        with open(os.path.join(HERE, "anleitungen", g["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(guide_page(g))
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page())
    print(f"{len(GUIDES)} Anleitungen und Startseite gebaut.")


if __name__ == "__main__":
    main()
