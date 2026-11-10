# Inhalte aller Anleitungen von digi.marcscheidegger.ch (wird von build.py gelesen).
# Eine Anleitung = ein Eintrag in GUIDES. Aufbau jeder Anleitung:
#   1 Basics, 2 Installation/Anmeldung, 3 Erste Schritte (mit Tutorial), 4 Kleine Umsetzung, dann Stolpersteine.
# Alle Texte sind Entwürfe: nicht von Hand getestet, Quellen siehe jeweils "quellen".


def tut(url, title, note):
    return (f'            <div class="tutorial">\n                <span class="badge badge--soft">Tutorial</span>\n'
            f'                <p><a href="{url}" target="_blank" rel="noopener">{title}</a><br>\n'
            f'                <small>{note}</small></p>\n            </div>')


def yt(query, note="Wähle ein aktuelles Video und schau es vor dem Praxistag kurz an."):
    from urllib.parse import quote_plus
    return tut("https://www.youtube.com/results?search_query=" + quote_plus(query),
               "YouTube-Suche: «" + query + "»", note)


def check(slug, items):
    rows = "\n".join(f'                <li><label><input type="checkbox" data-k="{slug}{i}"> {t}</label></li>'
                     for i, t in enumerate(items, 1))
    return f'            <h3>Fertig, wenn&hellip;</h3>\n            <ul class="check">\n{rows}\n            </ul>'


def note(title, text):
    return f'            <div class="note"><b>{title}</b>{text}</div>'


def warn(title, text):
    return f'            <div class="warn"><b>{title}</b>{text}</div>'


def ul(items):
    return "            <ul>\n" + "\n".join(f"                <li>{i}</li>" for i in items) + "\n            </ul>"


def ol(items):
    return "            <ol>\n" + "\n".join(f"                <li>{i}</li>" for i in items) + "\n            </ol>"


def p(text):
    return f"            <p>{text}</p>"


def h3(text):
    return f"            <h3>{text}</h3>"


def code(text):
    import html as _h
    return ('            <div class="code">\n                <button type="button" class="copy">Kopieren</button>\n'
            '                <pre><code>' + _h.escape(text.rstrip("\n")) + '</code></pre>\n            </div>')


GUIDES = []
import os as _os
CODE_OPENDAW = open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "beispiele", "opendaw-midnight-hook.txt"), encoding="utf-8").read()

# ------------------------------------------------------------------ Noteflight
GUIDES.append(dict(
    slug="noteflight", final=True, title="Noteflight", title_long="Noteflight: erste Noten im Browser",
    eyebrow="Notation · Beispiel 3, 4, 5, 6",
    lead="Eine Melodie schreiben, abspielen, teilen und exportieren, ohne etwas zu installieren.",
    card="Erste Noten im Browser, abspielen, teilen, exportieren.", diff_kurz="leicht", bsp=["B3", "B4", "B5", "B6"],
    zeit="ca. 60&ndash;90 Minuten", diff="leicht", geraet="Computer oder Tablet, nur Browser", kosten="Gratis-Konto zum Testen",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "5 Min.", "\n".join([
            p("Noteflight ist ein Notenschreibprogramm, das im Browser läuft. Du kannst Noten schreiben, sie sofort abspielen, mit anderen teilen und als PDF, MP3 oder MusicXML herunterladen. Dazu gibt es <b>Noteflight Learn</b>: die Variante für den Unterricht, in der Lernende in einem geschlossenen Rahmen Aufgaben bekommen und Noten teilen."),
            h3("Das brauchst du"),
            ul(["Computer oder Tablet mit einem aktuellen Browser (Chrome, Safari, Edge oder Firefox)", "Internetverbindung",
                "Eine E-Mail-Adresse für das Konto", "Kopfhörer, wenn du dein Stück abspielst und andere nicht stören willst"]),
            note("Noteflight Learn am Praxistag", "Für den Praxistag bekommst du von Marc einen Zugang zu seinem Noteflight Learn. Damit kannst du im geschlossenen Rahmen testen, teilen und alle Funktionen ausprobieren. Du brauchst dafür noch kein eigenes Abo."),
        ])),
        ("start", "Anmelden", "10 Min.", "\n".join([
            ol(['Öffne <a href="https://www.noteflight.com/" target="_blank" rel="noopener">noteflight.com</a>.',
                "Erstelle ein Gratis-Konto mit deiner E-Mail-Adresse und bestätige die E-Mail, die Noteflight dir schickt.",
                "Melde dich an. Du siehst nun deine Startseite, noch ohne Noten."]),
            note("Sprache", "Die Hilfeseiten von Noteflight gibt es auch auf Deutsch. Die Oberfläche selbst ist teilweise englisch. Das ist kein Problem, die wichtigsten Wörter lernst du auf dieser Seite."),
            warn("Kein Passwort weitergeben", "Verwende ein Passwort, das du sonst nirgends brauchst, und schreibe es nirgends ins E-Book oder in einen Chat."),
        ])),
        ("erste", "Erste Schritte zum Testen", "20 Min.", "\n".join([
            tut("https://support.noteflight.com/hc/en-us/articles/360021511631-Creating-Your-First-Score-video", "«Creating Your First Score» aus dem Hilfe-Center von Noteflight (Video, Englisch)",
                "Zeigt, wie man eine Partitur anlegt und eine einfache Melodie eingibt. Schau dir zuerst das Video an und probiere dann die Schritte unten aus. Nutze bei Bedarf die automatischen Untertitel."),
            ol(["Klicke oben auf <b>Create</b> (neue Partitur anlegen).", "Wähle ein Instrument, zum Beispiel Klavier oder Flöte, und bestätige mit <b>OK</b>.",
                "Klicke in den ersten Takt. Der Cursor zeigt dir, wo die nächste Note landet.", "Wähle in der Werkzeugleiste den Notenwert (zum Beispiel Viertelnote).",
                "Gib die Tonhöhe ein: mit den Pfeiltasten hoch und runter, oder durch Eintippen eines Buchstabens von A bis G.",
                "Drücke den <b>Play-Knopf</b> oder die Leertaste, um das Stück anzuhören."]),
            note("Tastenkürzel", 'Noteflight hat eine Übersicht aller Tastenkürzel, auch auf Deutsch. Du findest sie im Hilfe-Center unter <a href="https://noteflight.com/guide" target="_blank" rel="noopener">noteflight.com/guide</a>.'),
        ])),
        ("umsetzung", "Kleine Umsetzung: deine erste Melodie", "30&ndash;45 Min.", "\n".join([
            p("<b>Auftrag:</b> Schreibe eine achttaktige Melodie, die du kennst (zum Beispiel ein Kinderlied oder eine Tonleiter mit Rhythmus), und mache sie für andere zugänglich."),
            ol(["<b>Schreiben:</b> Gib die 8 Takte ein. Speichere die Partitur mit einem Titel, den du später wiederfindest.",
                "<b>Anpassen:</b> Ändere Tempo und Instrument, höre jede Version kurz an und entscheide dich für eine.",
                "<b>Teilen:</b> Öffne die Freigabe (Share) und erstelle einen Link, den nur Personen mit dem Link sehen. Schick ihn einer Kollegin oder einem Kollegen und lass sie oder ihn abspielen.",
                "<b>Exportieren:</b> Klicke auf den Export-Knopf (Symbol mit Pfeil nach unten) und lade dein Stück als <b>PDF</b> herunter. Probiere danach <b>MP3</b> aus."]),
            check("nf", ["deine Melodie 8 Takte hat und sich abspielen lässt,", "du Tempo und Instrument geändert hast,", "jemand anderes deinen Link öffnen und abspielen konnte,", "du ein PDF und eine MP3-Datei auf deinem Gerät hast."]),
            h3("Wenn du weitermachen willst"),
            ul(["<b>Mehrstimmig:</b> Füge ein zweites Instrument oder eine Gesangsstimme hinzu und schreibe einen dreistimmigen Satz. Teile ihn mit der Gruppe.",
                "<b>Importieren:</b> Noteflight liest MusicXML- und MIDI-Dateien ein, zum Beispiel aus MuseScore oder Dorico. Dateien mit der Endung <code>.mxl</code> (komprimiertes MusicXML) werden nicht direkt gelesen, exportiere sie vorher als <code>.musicxml</code> oder <code>.xml</code>.",
                "<b>Noteflight Learn:</b> Importiere eine fertige Partitur in Learn und mache daraus eine Aufgabe für die Klasse."]),
        ])),
    ],
    stolper=["<b>Gratis-Konto begrenzt:</b> Das Gratis-Konto hat Einschränkungen (zum Beispiel bei der Zahl der Partituren). Schau vor dem Start in den aktuellen Bedingungen nach, wie weit es reicht.",
             "<b>Import sieht anders aus:</b> Noteflight nutzt eine ältere Version von MusicXML. Nach dem Import kann die Formatierung abweichen, prüfe Taktstriche, Vorzeichen und Texte.",
             "<b>Urheberrecht:</b> Geschützte Stücke nur im geschlossenen Rahmen teilen (zum Beispiel Noteflight Learn oder Moodle mit Anmeldung), nicht öffentlich im Internet.",
             "<b>Learn kostet:</b> Noteflight Learn ist ein Abo-Angebot. Für den Praxistag nutzt ihr Marcs Zugang."],
    quellen=[("Noteflight: Guide", "https://noteflight.com/guide"),
             ("Noteflight Hilfe-Center: Importing and Exporting Music", "https://support.noteflight.com/hc/en-us/articles/360021512951-Importing-and-Exporting-Music"),
             ("Noteflight Hilfe-Center: Exporting Scores for Noteflight Learn Assignments", "https://support.noteflight.com/hc/en-us/articles/360040361432-Exporting-Scores-for-Noteflight-Learn-Assignments")],
))

# ------------------------------------------------------------------ MuseScore
GUIDES.append(dict(
    slug="musescore", final=True, title="MuseScore", title_long="MuseScore: Noten schreiben, finden und tauschen",
    eyebrow="Notation · Beispiel 3, 4, 5, 6, 7",
    lead="Das kostenlose Notenprogramm installieren, eine Melodie schreiben und als PDF, MP3 und MusicXML weitergeben.",
    card="Plattform, Software und Import/Export.", diff_kurz="mittel", bsp=["B3", "B4", "B5", "B6", "B7"],
    zeit="ca. 60&ndash;90 Minuten", diff="mittel", geraet="Computer (Mac, Windows, Linux)", kosten="Programm gratis, kein Konto nötig",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "10 Min.", "\n".join([
            p("<b>MuseScore Studio</b> ist ein freies Notenschreibprogramm, das du auf dem Computer installierst. Du schreibst Noten, hörst sie sofort ab und gibst sie als PDF, MP3, MIDI oder MusicXML weiter. Es ist die kostenlose Alternative zu Programmen wie Dorico oder Sibelius."),
            p("Dazu gehört die Plattform <b>musescore.com</b>: eine Website, auf der Menschen ihre Noten veröffentlichen und andere sie finden und abspielen können. Das Programm und die Plattform sind getrennt. Für das Programm brauchst du kein Konto, für Downloads von der Plattform schon."),
            h3("Das brauchst du"),
            ul(["Computer mit Mac, Windows oder Linux (die Installation geht über das Hilfsprogramm MuseHub, siehe unten)", "Internetverbindung für den Download", "Kopfhörer",
                "Ein Gratis-Konto auf musescore.com, um Noten von dort herunterzuladen oder selbst zu veröffentlichen"]),
            note("Welche Version?", "Der aktuelle Name ist <b>MuseScore Studio</b> (früher MuseScore 4). Ältere Videos und Seiten sprechen von MuseScore 3 oder 4, die Oberfläche ist ähnlich, aber nicht gleich. Gilt nur, was du auf dem Bildschirm siehst."),
        ])),
        ("start", "Installieren", "15 Min.", "\n".join([
            ol(['Öffne <a href="https://musescore.org/en/download" target="_blank" rel="noopener">musescore.org/download</a> und klicke auf <b>Free Download</b>.',
                "Du lädst damit <b>MuseHub</b> herunter, ein kleines Programm, das MuseScore Studio installiert und aktuell hält.",
                "<b>Mac:</b> Öffne die Datei <code>Muse_Hub.dmg</code> in den Downloads, ziehe MuseHub in den Ordner «Programme» und starte es. Erlaube bei Rückfrage die Berechtigungen.",
                "<b>Windows:</b> Starte die heruntergeladene Datei und folge dem Installationsfenster.",
                "Klicke in MuseHub auf <b>Apps</b> und bei MuseScore Studio auf <b>Free</b>. Wenn der Download fertig ist, klicke auf <b>Open</b>."]),
            note("Installation im Detail", 'Die Anleitung von MuseScore dazu: <a href="https://handbook.musescore.org/introduction/download-and-installation" target="_blank" rel="noopener">Download and installation</a> (Handbuch, Englisch).'),
            warn("Nicht von anderen Seiten laden", "Lade MuseScore nur von musescore.org. Auf Drittseiten gibt es Versionen mit unerwünschten Zusatzprogrammen."),
        ])),
        ("erste", "Erste Schritte zum Testen", "25 Min.", "\n".join([
            tut("https://www.youtube.com/watch?v=0X8G59wJcXc", "«MuseScore in Minutes: The Basics of Score Writing» (Video, Englisch)",
                "Kurze Einführung in die Basis: Partitur anlegen, Noten eingeben, abspielen. Das Video gehört zur Reihe «MuseScore in Minutes» auf dem YouTube-Kanal von MuseScore. Nutze bei Bedarf die automatischen Untertitel mit Übersetzung."),
            tut("https://handbook.musescore.org/introduction/create-your-first-score", "MuseScore Handbuch: Create your first score (Englisch)",
                "Schritt für Schritt vom neuen Dokument bis zur ersten Note. Es gibt auch Handbuchseiten auf Deutsch, die Auswahl oben rechts auf der Seite."),
            ol(["Klicke auf <b>New score</b> und wähle eine Vorlage, zum Beispiel «Klavier» oder «Melodie».", "Im nächsten Fenster stellst du Tonart, Taktart und Tempo ein oder überspringst es mit <b>Done</b>.",
                "Klicke in den ersten Takt und drücke <kbd>N</kbd>. Ein blaues Feld zeigt, wo die nächste Note landet (Eingabemodus).", "Wähle den Notenwert in der Leiste oben oder mit den Zifferntasten <kbd>1</kbd> bis <kbd>7</kbd>.",
                "Tippe die Tonhöhe als Buchstabe von <kbd>A</kbd> bis <kbd>G</kbd>. Mit <kbd>Esc</kbd> verlässt du den Eingabemodus.", "Drücke die <b>Leertaste</b> zum Abspielen."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: Noten tauschen und eigene Melodie", "45&ndash;60 Min.", "\n".join([
            p("<b>Auftrag:</b> Hole dir ein Stück von der Plattform, öffne es in MuseScore, gib es in der älteren MusicXML-Form wieder heraus und schreibe danach eine eigene Melodie."),
            h3("Teil 1: Noten von der Plattform holen und tauschen"),
            ol(['Öffne <a href="https://musescore.com/" target="_blank" rel="noopener">musescore.com</a> und melde dich mit einem Gratis-Konto an (E-Mail bestätigen).',
                "Suche ein Stück, das gemeinfrei ist (Public Domain), zum Beispiel ein Volkslied, oder ein Stück, das als <b>Original</b> gekennzeichnet ist. Nach Angaben von MuseScore dürfen Gratis-Konten genau diese Stücke herunterladen.",
                "Klicke auf <b>Download</b> und wähle das Format <b>MusicXML</b>.",
                "Öffne die Datei in MuseScore Studio (Doppelklick oder <b>Datei &rarr; Öffnen</b>) und drücke die Leertaste zum Abspielen.",
                "Wähle <b>Datei &rarr; Exportieren</b>, das Format <b>MusicXML</b> und dabei die <b>unkomprimierte (ältere) Form</b> mit der Endung <code>.musicxml</code> oder <code>.xml</code>.",
                "Öffne diese Datei in Noteflight oder einem anderen Notenprogramm (Anleitung zu Noteflight auf dieser Seite) und prüfe, ob alles angekommen ist."]),
            warn("Nicht auf «Trial» klicken", "Bei Downloads schlägt die Plattform manchmal ein Pro-Abo oder eine Testphase vor. Das brauchst du für gemeinfreie Stücke nicht. Schliesse das Fenster oder wähle ein anderes Stück."),
            h3("Teil 2: Eigene Melodie schreiben"),
            ol(["<b>Schreiben:</b> Lege mit <b>New score</b> eine neue Partitur an und gib eine achttaktige Melodie ein, die du kennst. Speichere sie auf dem Computer (<b>Datei &rarr; Speichern</b>).",
                "<b>Anpassen:</b> Ändere Tempo und Instrument und entscheide dich für eine Version.",
                "<b>Exportieren:</b> Exportiere die Melodie als <b>PDF</b> und als <b>MP3</b> und kontrolliere beide Dateien."]),
            check("ms", ["du ein Stück als MusicXML von musescore.com geladen und in MuseScore geöffnet hast,", "du es als unkomprimierte MusicXML-Datei wieder exportiert hast,", "diese Datei in Noteflight oder einem anderen Programm aufgeht,",
                         "deine eigene Melodie 8 Takte hat und sich abspielen lässt,", "du ein PDF und eine MP3-Datei deiner Melodie auf dem Gerät hast."]),
            h3("Wenn du weitermachen willst"),
            ul(["<b>Weitere Formate:</b> MuseScore öffnet auch MIDI und Dateien anderer Programme, zum Beispiel Guitar Pro. So kommst du an Noten aus anderen Quellen und kannst sie bearbeiten.",
                "<b>Teilen auf musescore.com:</b> Mit deinem Konto kannst du eigene Noten dort online speichern und per Link teilen. Die Bedingungen für Gratis-Konten ändern sich, schau vor dem Veröffentlichen in den aktuellen Angaben der Plattform nach.",
                "<b>Mehrere Stimmen:</b> Füge im Fenster «Instrumente» ein zweites Instrument oder Gesang hinzu und schreibe einen Satz für die Gruppe."]),
        ])),
    ],
    stolper=["<b>Konto nur für die Plattform:</b> Für das Programm brauchst du kein Konto. Mit einem Konto auf musescore.com lassen sich Noten herunterladen, online speichern und teilen. Welche Gratis-Grenzen dort gelten, ändert sich. Prüfe es im Konto.",
             "<b>Noten von musescore.com herunterladen:</b> Mit einem Gratis-Konto gehen nach Angaben von MuseScore nur gemeinfreie Stücke und als «Original» gekennzeichnete Eigenkompositionen. Für geschützte Stücke braucht es ein Pro-Abo. Das Anschauen und Abspielen im Browser geht in der Regel ohne.",
             "<b>MusicXML in Noteflight:</b> Noteflight liest die komprimierte Form (<code>.mxl</code>) nicht direkt. MuseScore kann die ältere, unkomprimierte Form exportieren (<code>.musicxml</code> oder <code>.xml</code>). Nimm diese.",
             "<b>Format sieht anders aus:</b> Nach dem Import aus anderen Programmen kann das Layout abweichen. Prüfe Taktstriche, Vorzeichen und Texte.",
             "<b>Urheberrecht:</b> Fremde Stücke nur im geschlossenen Rahmen weitergeben (zum Beispiel Moodle mit Anmeldung) und nicht öffentlich auf musescore.com veröffentlichen."],
    quellen=[("MuseScore Studio: Download", "https://musescore.org/en/download"),
             ("MuseScore: Plattform", "https://musescore.com/"),
             ("MuseScore Handbuch: Download and installation", "https://handbook.musescore.org/introduction/download-and-installation"),
             ("MuseScore Handbuch: Create your first score", "https://handbook.musescore.org/introduction/create-your-first-score"),
             ("MuseScore Handbuch: File export", "https://handbook.musescore.org/file-management/file-export"),
             ("MuseScore in Minutes: The Basics of Score Writing (YouTube)", "https://www.youtube.com/watch?v=0X8G59wJcXc")],
))

# ------------------------------------------------------------------ Video mit dem Handy
GUIDES.append(dict(
    slug="handyvideo", title="Video mit dem Handy", title_long="Video mit dem Handy: Mehrbildvideo gleich beim Filmen",
    eyebrow="Video · Beispiel 3",
    lead="Mehrere Stimmen nacheinander aufnehmen und als Mehrbildvideo zusammenbauen, direkt auf dem Handy und ohne Schnittprogramm.",
    card="Mehrbildvideo mit Acapella oder CapCut, Notenrolle per Bildschirmaufnahme.", diff_kurz="leicht bis mittel", bsp=["B3"],
    zeit="ca. 45&ndash;60 Minuten", diff="leicht bis mittel", geraet="Handy oder Tablet (iPhone, iPad oder Android)", kosten="Acapella gratis bis 30 Sekunden, CapCut gratis ohne Zeitlimit",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "10 Min.", "\n".join([
            p("Ein <b>Mehrbildvideo</b> zeigt mehrere Aufnahmen gleichzeitig in einem Raster, zum Beispiel vier Stimmen, die zusammen ein Lied singen. Mit <b>DaVinci Resolve</b> (eigene Anleitung) ist das genau, aber aufwendig. Die App <b>Acapella</b> (von PicPlay) macht es einfacher: Du nimmst eine Stimme nach der anderen auf, hörst dabei die bisherigen im Kopfhörer, und am Ende liegt das fertige Video im Raster vor."),
            p("Die <b>Pilotspur</b> ist die Spur, nach der sich alle anderen richten: eine erste Aufnahme (zum Beispiel die Melodie oder ein Klavier) oder eine fertige Tonspur, etwa ein MP3-Export aus Noteflight. Eine <b>Notenrolle</b> ist ein Video, in dem die Noten zum Stück durchlaufen. Du machst sie mit einer Bildschirmaufnahme (siehe unten)."),
            h3("Das brauchst du"),
            ul(["Handy oder Tablet mit Kamera und Mikrofon", "<b>Kabelkopfhörer mit Mikrofon</b>. Bluetooth-Kopfhörer sind für Acapella nicht ideal, weil der Ton leicht verzögert ankommt", "Ein ruhiger Raum und ein Stück, das du kennst",
                "Genug Speicherplatz auf dem Gerät"]),
            warn("Gratis-Version und Premium", "Beim ersten Start zeigt die App ein Fenster «Hole dir Premium» (Stand November 2026, Schweiz: eine Woche gratis testen, danach CHF 11.00 im Monat oder CHF 52.00 im Jahr). Du brauchst das nicht. Schliesse das Fenster mit dem <b>X</b> oben links oder tippe auf «Acapella jetzt entdecken». Premium bringt unter anderem 1080p-Video, das Hinzufügen von Videos aus der Fotobibliothek und mehr Raster. Ohne Premium nimmst du höchstens 30 Sekunden pro Video auf. Mehr als neun Bilder gehen auch mit Premium nur über einen Umweg."),
        ])),
        ("start", "Installieren", "10 Min.", "\n".join([
            ol(["Suche im App Store (iPhone, iPad) oder Play Store (Android) nach <b>Acapella</b> und achte darauf, dass die App von <b>PicPlay</b> (früher Mixcord) stammt.", "Installiere sie und öffne sie. Erlaube den Zugriff auf Kamera und Mikrofon.",
                "Lege bei Bedarf ein Konto an (E-Mail oder bestehendes Konto). Aufnehmen geht je nach Version auch ohne Veröffentlichung.",
                "Schliesse das Premium-Fenster mit dem <b>X</b>. Starte keine Testphase, wenn du kein Abo willst: Sie geht sonst nach einer Woche in ein kostenpflichtiges Abo über."]),
            note("iPad ohne Abo?", 'Für das iPad gibt es zusätzlich die gratis App <a href="https://apps.apple.com/us/app/duette/id1515610873" target="_blank" rel="noopener">Duette</a> für Mehrbild-Musikvideos. Sie ist hier nicht Hauptweg, weil ich sie nicht getestet habe.'),
        ])),
        ("erste", "Erste Schritte zum Testen", "15 Min.", "\n".join([
            tut("https://intercom.help/mixcord/en/articles/4713363-acapella-getting-started", "Acapella: Getting Started (Hilfe-Center des Herstellers, Englisch)",
                "Die offizielle Kurzanleitung mit allen Schritten vom neuen Projekt bis zum Speichern. Ein Video von Acapella selbst habe ich nicht gefunden."),
            ol(["Wähle <b>Record New</b> (neues Projekt).", "Wähle ein Raster, zum Beispiel vier Felder.", "Wähle die Länge. Gratis gehen <b>15 oder 30 Sekunden</b> (oder eine eigene Zeit bis höchstens 30 Sekunden). 1, 3 und 10 Minuten gehören zu Premium. Die App beendet die Aufnahme von selbst, wenn die Zeit um ist. Nimm deshalb jede Stimme für die ganze Dauer auf.", "Tippe auf das erste Feld und dann auf die rote Aufnahmetaste. Sing oder spiel die gewählte Zeit lang.",
                "Schau dir den Take an. Mit dem grünen Häkchen behältst du ihn, mit dem roten Kreuz nimmst du neu auf.", "Tippe auf das nächste Feld und nimm die zweite Stimme auf. Du hörst die erste im Kopfhörer."]),
            note("Metronom", "Die App hat ein Metronom, das du im Kopfhörer hörst. Es wird nicht ins Video aufgenommen."),
        ])),
        ("umsetzung", "Kleine Umsetzung: vierstimmiges Mehrbildvideo", "20&ndash;30 Min.", "\n".join([
            p("<b>Auftrag:</b> Nimm einen kurzen Ausschnitt (30 Sekunden, zum Beispiel den Anfang eines Kanons oder eines vierstimmigen Liedes) in vier Bildern auf und speichere das Video. Mehr erlaubt die Gratis-Version nicht."),
            ol(["<b>Pilotspur:</b> Nimm im ersten Feld die Melodie auf. Sie ist das Vorbild für die anderen.",
                "<b>Stimmen:</b> Nimm in den anderen drei Feldern je eine Stimme auf. Du kannst dazu singen, summen oder mit einem Instrument spielen.",
                "<b>Speichern:</b> Wähle <b>Save &amp; Share</b>. Wähle <b>Private</b> und speichere das Video auf dem Gerät. Wähle nie «Public», solange du nicht willst, dass es öffentlich ist.",
                "<b>Kontrollieren:</b> Schau das Video an. Stimmt der Ton, stimmen die Einsätze?"]),
            h3("Mit Notenrolle (für Fortgeschrittene)"),
            ol(["Öffne die Noten in Noteflight oder MuseScore (siehe die Anleitungen dazu) auf dem Handy, Tablet oder Computer.",
                "Starte eine <b>Bildschirmaufnahme</b>: Auf dem iPhone öffnest du das Kontrollzentrum und tippst auf die Aufnahme-Taste (wenn sie fehlt, fügst du sie unter Einstellungen &rarr; Kontrollzentrum hinzu). Es gibt einen Countdown von drei Sekunden.",
                "Spiele das Stück ab und beende die Aufnahme. Das Video liegt in der Fotomediathek unter «Bildschirmaufnahmen».",
                "Lege Notenrolle und Mehrbildvideo in <b>iMovie</b> nebeneinander (Split Screen) oder in einem Schnittprogramm."]),
            tut("https://support.apple.com/en-us/102653", "Apple: Record the screen on your iPhone, iPad, or iPod touch (Englisch)", "Die Anleitung von Apple zur Bildschirmaufnahme. Android-Geräte haben eine ähnliche Funktion in den Schnelleinstellungen."),
            check("hv", ["dein Video vier Bilder zeigt und der Ton stimmt,", "du die Pilotspur zuerst aufgenommen hast,", "das Video privat auf deinem Gerät gespeichert ist,", "du weisst, wie du Bildschirmaufnahme und iMovie für eine Notenrolle einsetzen würdest."]),
            h3("Alternative ohne Zeitlimit: CapCut"),
            p("Wenn die 30 Sekunden von Acapella nicht reichen, filmst du die Stimmen normal und legst sie danach in <b>CapCut</b> nebeneinander. CapCut gibt es als App für Handy und Tablet und als Programm für Mac und Windows. Es kostet in der Grundversion nichts."),
            ol(["Filme jede Stimme einzeln mit der Kamera-App, mit Kopfhörern und der Pilotspur (zum Beispiel einem MP3-Export aus Noteflight) im Ohr.",
                "Öffne CapCut, lege ein neues Projekt an und importiere den ersten Clip.",
                "Füge die weiteren Clips als <b>Overlay</b> (zusätzliche Videospur) darüber ein. Auf dem Computer legst du sie in der Timeline übereinander. Die Clips müssen zeitlich übereinander liegen, sonst laufen sie nacheinander.",
                "Verkleinere jeden Clip mit zwei Fingern (oder an den Ecken) und schiebe ihn an seinen Platz im Raster.",
                "Richte die Clips am Ton aus. Du hörst, ob die Einsätze zusammenpassen, und schiebst einen Clip bei Bedarf kurz nach vorn oder hinten.",
                "Exportiere das Video in der höchsten Gratis-Qualität (1080p)."]),
            warn("Wasserzeichen und Pro", "Nach den Angaben, die ich gefunden habe, exportiert CapCut ein Video ohne Wasserzeichen, solange du keine Vorlagen oder Effekte mit Pro-Zeichen benutzt. Manche Quellen widersprechen sich, und die Preise ändern sich. Schau beim Export auf das Pro-Zeichen und starte keine Testphase, wenn du kein Abo willst. Die Menünamen der App können je nach Version abweichen."),
            h3("Weitere Alternativen"),
            ul(["<b>GridPlayer (Mac, Windows, Linux, gratis):</b> Ein Abspielprogramm, das mehrere Videos gleichzeitig nebeneinander im Raster zeigt. Es ist <b>kein</b> Aufnahme- und kein Schnittprogramm und exportiert nichts (laut Beschreibung des Projekts). Nützlich, um die einzelnen Stimmen beim Üben oder in der Besprechung nebeneinander anzuschauen. Für den Mac gibt es die Version nur für Apple-Chips (M-Reihe). Sie ist nicht signiert, macOS fragt deshalb nach einer Ausnahme. Lade es nur von der Seite des Projekts auf <a href=\"https://github.com/vzhd1701/gridplayer\" target=\"_blank\" rel=\"noopener\">GitHub</a>, nicht von Download-Portalen. Ich habe es nicht getestet.",
                "<b>iMovie (iPhone, iPad, Mac, gratis):</b> Legt zwei Clips nebeneinander oder übereinander (Split Screen). Mehr als zwei Bilder gehen nicht. Details bei Apple: <a href=\"https://support.apple.com/guide/imovie-iphone/kna831efee4d/ios\" target=\"_blank\" rel=\"noopener\">iMovie Split Screen</a>.",
                "<b>InShot:</b> Funktioniert ähnlich wie CapCut, mit Gratis-Einschränkungen (zum Beispiel Wasserzeichen).",
                "<b>DaVinci Resolve:</b> Wenn du mehr Kontrolle über Ton und Schnitt willst, siehe die eigene Anleitung auf dieser Seite."]),
        ])),
    ],
    stolper=["<b>Bluetooth-Kopfhörer:</b> Der Ton kommt leicht verzögert an, die Stimmen sind dann nicht synchron. Nimm Kabelkopfhörer mit Mikrofon.",
             "<b>Premium-Abo:</b> Die Testphase von einer Woche wird danach kostenpflichtig (CHF 11.00 im Monat oder CHF 52.00 im Jahr, Stand November 2026). Beende sie rechtzeitig in den Abos deines Apple- oder Google-Kontos, wenn du sie ausprobiert hast.",
             "<b>Gratis-Grenzen:</b> In Acapella sind gratis nur 15 oder 30 Sekunden möglich. Längere Videos (1, 3, 10 Minuten), das Hinzufügen von Videos aus der Fotobibliothek und 1080p gehören zu Premium. Für ein ganzes Lied nimm CapCut.",
             "<b>Privat bleiben:</b> Wähle beim Speichern «Private». Nimm keine Kinder oder fremden Personen auf, ohne dass sie einverstanden sind.",
             "<b>Notenrolle:</b> Einige Apps erlauben keine Bildschirmaufnahme ihrer Inhalte. Bildschirmaufnahme und Spiegelung laufen nicht gleichzeitig.",
             "<b>Urheberrecht:</b> Fremde Stücke nur im geschlossenen Rahmen zeigen und nicht öffentlich veröffentlichen."],
    quellen=[("Acapella: Getting Started (Mixcord/PicPlay Hilfe)", "https://intercom.help/mixcord/en/articles/4713363-acapella-getting-started"),
             ("Acapella: mehr als neun Bilder (Mixcord/PicPlay Hilfe)", "https://intercom.help/mixcord/en/articles/3856094-acapella-how-can-i-create-a-video-with-more-than-9-grids"),
             ("Apple: Bildschirmaufnahme auf iPhone, iPad", "https://support.apple.com/en-us/102653"),
             ("Apple: iMovie auf dem iPhone, Split Screen", "https://support.apple.com/guide/imovie-iphone/kna831efee4d/ios"),
             ("CapCut: Two videos side by side (Desktop)", "https://www.capcut.com/resource/how-to-put-two-videos-side-by-side"),
             ("GridPlayer auf GitHub", "https://github.com/vzhd1701/gridplayer")],
))

# ------------------------------------------------------------------ Moises
GUIDES.append(dict(
    slug="moises", final=True, title="Moises", title_long="Moises: Stimmen trennen und Playalong machen",
    eyebrow="Playalongs · Beispiel 7, 8",
    lead="Ein Stück in Gesang, Schlagzeug, Bass und mehr zerlegen und dir daraus ein Playalong bauen.",
    card="Stimmen trennen im Browser, Gratis-Konto.", diff_kurz="mittel", bsp=["B7", "B8"],
    zeit="ca. 45&ndash;60 Minuten", diff="mittel", geraet="Browser auf Computer oder Tablet, oder App", kosten="Gratis-Konto mit Monatslimit",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "5 Min.", "\n".join([
            p("Moises trennt mit künstlicher Intelligenz eine Aufnahme in einzelne Spuren (Stems): zum Beispiel Gesang, Schlagzeug, Bass und Übriges. Du kannst Spuren stummschalten, einzeln hören sowie Tempo und Tonhöhe ändern. So entsteht aus einem Lied ein Playalong ohne die Stimme, die du selber übst."),
            h3("Das brauchst du"),
            ul(["Browser (Moises läuft in der Web-App, du musst nichts installieren) oder die App für Handy und Tablet", "Ein Konto (E-Mail oder Anmeldung über einen bestehenden Account)",
                "Eine Audiodatei, die du verwenden darfst, zum Beispiel eine eigene Aufnahme oder eine gekaufte mp3", "Kopfhörer"]),
            warn("Monatslimit im Gratis-Konto", "Das Gratis-Konto erlaubt nur wenige Songs pro Monat (nach Angaben von Moises etwa 5 Trennungen). Plane deshalb genau, welche Songs du trennst, und schau die aktuellen Bedingungen im Konto an."),
        ])),
        ("start", "Anmelden", "10 Min.", "\n".join([
            ol(['Öffne <a href="https://moises.ai/" target="_blank" rel="noopener">moises.ai</a> und wähle «Kostenlos starten» oder die Anmeldung.', "Erstelle das Konto und bestätige die E-Mail.",
                "Auf dem Handy lädst du alternativ die App «Moises» aus dem App Store oder Play Store."]),
            warn("Kein Passwort weitergeben", "Gib dein Passwort nie in einen Chat oder ins E-Book. Moises braucht keine Zahlungsdaten fürs Gratis-Konto."),
        ])),
        ("erste", "Erste Schritte zum Testen", "15 Min.", "\n".join([
            tut("https://www.youtube.com/watch?v=ylBV5q5X4VY", "«How to Use Stem Separation to Practice Smarter» (Moises Essentials, Video, Englisch)",
                "Vom offiziellen Moises-Kanal auf YouTube. Zeigt, wie man ein Stück in Stems trennt und damit übt. Es gibt kein deutsches Video von Moises. Nutze bei Bedarf die automatischen Untertitel mit Übersetzung."),
            tut("https://www.youtube.com/watch?v=NBmJklnDnZE", "«How To Separate Stems With Moises AI [2026 Guide]» (AJ Tech Tutorials, Video, Englisch)",
                "Zweites Tutorial, zeigt den Ablauf Schritt für Schritt am Computer im Browser. Von einem Drittanbieter, nicht von Moises selbst."),
            ol(["Wähle <b>Hochladen</b> (Upload) und lade deine Audiodatei hoch. Je nach Version geht auch ein Link oder eine Datei aus der Cloud.",
                "Wähle, welche Spuren du trennen willst, zum Beispiel Gesang und Begleitung, und starte die Trennung.",
                "Warte, bis die Verarbeitung fertig ist. Bei einem normalen Lied dauert das meist nur kurz.",
                "Im Mixer siehst du jede Spur mit Lautstärke, <b>Mute</b> (stumm) und <b>Solo</b>. Probiere aus, was passiert, wenn du die Gesangsspur stumm schaltest."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: dein Playalong", "20&ndash;30 Min.", "\n".join([
            p("<b>Auftrag:</b> Mache aus einem Stück, das du singen oder spielen möchtest, ein Playalong in deinem Tempo und deiner Tonlage."),
            ol(["Trenne das Stück in Gesang und Begleitung.", "Schalte die Gesangsspur stumm.", "Setze das Tempo etwas herunter (zum Beispiel auf 80 Prozent), ohne dass sich die Tonhöhe ändert.",
                "Falls das Stück zu hoch oder zu tief liegt, ändere die Tonhöhe in Halbtönen.", "Speichere oder exportiere das Ergebnis, soweit dein Konto das zulässt, und probiere es mit Kopfhörern aus."]),
            check("mo", ["das Stück ist getrennt und du hörst die Spuren einzeln,", "die Gesangsspur ist stumm und die Begleitung läuft,", "du hast Tempo oder Tonhöhe verändert,", "du weisst, wie viele Trennungen im Gratis-Konto noch frei sind."]),
            h3("Wenn du weitermachen willst"),
            ul(["Vergleiche Moises mit der Stem-Funktion in Logic oder Ableton (Anleitung folgt).", "Verwende das Ergebnis in Anytune zum Üben mit Loop."]),
        ])),
    ],
    stolper=["<b>Urheberrecht:</b> Trenne und verwende fremde Aufnahmen nur für den Unterricht im geschlossenen Rahmen und gib die Ergebnisse nicht öffentlich weiter.",
             "<b>Monatslimit:</b> Gratis-Konten sind begrenzt. Teste zuerst mit einem Song und speichere das Ergebnis, bevor du weitere hochlädst.",
             "<b>Klangqualität:</b> Die Trennung ist nie perfekt, bei dichten Arrangements hört man Reste der anderen Spuren.",
             "<b>Funktionen ändern sich:</b> Welche Funktionen gratis sind, ändert Moises laufend. Prüfe im Konto, was im Moment geht."],
    quellen=[("Moises: Webseite", "https://moises.ai/"), ("Moises: Hilfe-Center", "https://help.moises.ai/"), ("Moises im App Store", "https://apps.apple.com/US/app/id1515796612")],
))

# ------------------------------------------------------------------ Anytune
GUIDES.append(dict(
    slug="anytune", title="Anytune", title_long="Anytune: Tempo und Tonhöhe anpassen",
    eyebrow="Playalongs · Beispiel 7, 8",
    lead="Eine bestehende Aufnahme langsamer machen, höher oder tiefer stellen und eine schwierige Stelle in der Schleife üben.",
    card="Tempo und Tonhöhe einer Aufnahme anpassen.", diff_kurz="mittel", bsp=["B7", "B8"],
    zeit="ca. 30&ndash;45 Minuten", diff="mittel", geraet="iPhone, iPad oder Mac (App)", kosten="App, Preis im Store prüfen",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "5 Min.", "\n".join([
            p("Anytune ist eine App zum Üben mit Aufnahmen. Sie ändert das <b>Tempo</b>, ohne dass sich die Tonhöhe verändert, und umgekehrt. Dazu kommen Schleifen (Loops) über eine Stelle und ein Trainer, der das Tempo Schritt für Schritt steigert."),
            h3("Das brauchst du"),
            ul(["iPhone, iPad oder Mac. Eine Windows-Version konnte ich nicht bestätigen. Prüfe das im Store, bevor du planst.", "Eine Audiodatei auf dem Gerät (mp3, m4a), die du verwenden darfst",
                "Ein Konto im App Store und ein paar Franken, falls die App kostet (Preis und Funktionsumfang im Store prüfen)"]),
        ])),
        ("start", "Installieren", "10 Min.", "\n".join([
            ol(["Suche im App Store (iPhone, iPad) oder Mac App Store nach <b>Anytune</b> und installiere die App.", "Starte die App. Beim ersten Start fragt sie, ob sie auf deine Musik zugreifen darf. Erlaube den Zugriff, wenn du Dateien aus der Musik-App nutzen willst.",
                "Hole eine Aufnahme in die App: aus der Musik-App, aus der Dateien-App oder per «Öffnen in» aus einer anderen App."]),
            note("Hinweis", "Zeige Marcs Playalongs aus Moises oder Noteflight (mp3-Export) hier hinein, dann übst du mit deinen eigenen Dateien."),
        ])),
        ("erste", "Erste Schritte zum Testen", "10 Min.", "\n".join([
            tut("https://de.anytune.us/user-guide/basics", "Anytune: Benutzerhandbuch, Grundlagen (Deutsch)", "Das offizielle Handbuch gibt es auch auf Deutsch. Lies die Grundlagen, bevor du die Schritte unten ausprobierst."),
            ol(["Öffne ein Stück und starte die Wiedergabe.", "Ziehe den <b>Tempo</b>-Regler nach links, bis das Stück deutlich langsamer läuft. Die Tonhöhe bleibt gleich.", "Ändere die <b>Tonhöhe</b> (Pitch) in Halbtönen. Das Tempo bleibt gleich.",
                "Setze mit den Markierungen <b>A</b> und <b>B</b> eine Schleife über eine schwierige Stelle."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: eine Stelle üben", "15&ndash;20 Min.", "\n".join([
            p("<b>Auftrag:</b> Wähle eine kurze Stelle, die dir schwerfällt, und übe sie in der Schleife vom langsamen zum normalen Tempo."),
            ol(["Setze die Schleife A-B über die Stelle.", "Starte mit etwa 70 Prozent Tempo und spiele oder singe mit.", "Erhöhe das Tempo in kleinen Schritten, wenn die Stelle sitzt. Der «Step-It-Up»-Trainer (je nach Version) macht das automatisch.",
                "Falls die Tonlage nicht passt, verschiebe die Tonhöhe in Halbtönen."]),
            check("an", ["du hast eine A-B-Schleife gesetzt,", "du hast Tempo und Tonhöhe getrennt verstellt,", "du hast die Stelle im langsamen Tempo gespielt oder gesungen."]),
        ])),
    ],
    stolper=["<b>Funktionsumfang:</b> Einige Funktionen (zum Beispiel der Trainer oder Notizen) gibt es nur in der Pro-Version. Prüfe im Store, was deine Version kann.",
             "<b>Dateien:</b> Streaming-Titel lassen sich nicht laden. Du brauchst Audiodateien auf dem Gerät.",
             "<b>Alternative im Browser:</b> YouTube und Vimeo haben eine eigene Geschwindigkeits-Einstellung im Player, aber ohne Tonhöhe.",
             "<b>Urheberrecht:</b> Aufnahmen nur für das eigene Üben und den Unterricht im geschlossenen Rahmen verwenden."],
    quellen=[("Anytune: Benutzerhandbuch, Grundlagen", "https://de.anytune.us/user-guide/basics"), ("Anytune: Hilfe-Center", "https://anytune.zendesk.com/hc/en-us/articles/360025666651")],
))

# ------------------------------------------------------------------ Guitar Pro
GUIDES.append(dict(
    slug="guitar-pro", title="Guitar Pro, Ultimate Guitar, Soundslice", title_long="Guitar Pro, Ultimate Guitar und Soundslice",
    eyebrow="Notation · Beispiel 7, 8",
    lead="Tabulaturen und Noten finden, abspielen, verlangsamen und in einzelne Stimmen zerlegen.",
    card="Installation, mySongBook, Ultimate Guitar, Soundslice.", diff_kurz="mittel", bsp=["B7", "B8"],
    zeit="ca. 60 Minuten", diff="mittel", geraet="Computer (Mac, Windows) oder Browser", kosten="Testversion 7 Tage, danach Player-Modus gratis",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "10 Min.", "\n".join([
            p("<b>Guitar Pro</b> ist ein Programm für Tabulaturen und Noten. Es spielt ein Stück ab, zeigt Griffbild und Noten, und du kannst Tempo und Spuren ändern. <b>mySongBook</b> ist die Sammlung mit vielen fertigen Stücken in Guitar Pro. Sie ist auch für Nicht-Gitarristinnen und Nicht-Gitarristen nützlich, weil sie Noten und Bandspuren liefert."),
            p("<b>Ultimate Guitar</b> (ultimate-guitar.com) ist eine Website und App mit sehr vielen Tabs und Akkordblättern. <b>Soundslice</b> kann Guitar-Pro-Dateien im Browser anzeigen und abspielen, ohne dass du etwas installierst."),
            h3("Das brauchst du"),
            ul(["Computer mit Mac oder Windows für Guitar Pro, für die anderen beiden reicht der Browser", "Eine E-Mail-Adresse für die Konten", "Kopfhörer"]),
        ])),
        ("start", "Installieren und anmelden", "20 Min.", "\n".join([
            ol(['Lade Guitar Pro von <a href="https://www.guitar-pro.com/" target="_blank" rel="noopener">guitar-pro.com</a> herunter und installiere es wie jedes Programm. Die Testversion läuft 7 Tage, danach bleibt der Player-Modus: Du kannst Stücke abspielen, aber nicht mehr speichern oder bearbeiten.',
                'Die Anleitung des Herstellers beschreibt die Installation Schritt für Schritt: <a href="https://www.guitar-pro.com/docs/gp8/basics/installation" target="_blank" rel="noopener">Getting Started, Installation</a>.',
                'Öffne <a href="https://www.ultimate-guitar.com/" target="_blank" rel="noopener">ultimate-guitar.com</a> und erstelle ein Gratis-Konto (oder lade die App).']),
            warn("mySongBook kostet", "Die Stücke aus mySongBook brauchen ein Abo, abgesehen von einzelnen Gratis-Stücken (zum Beispiel dem «Free Tab of the Day»). Klär das mit Marc, bevor du etwas abschliesst."),
        ])),
        ("erste", "Erste Schritte zum Testen", "15 Min.", "\n".join([
            tut("https://www.guitar-pro.com/docs/gp8/mysongbook", "Guitar Pro: mySongBook in Guitar Pro 8 (offizielle Anleitung, Englisch)", "Erklärt, was mySongBook ist und wie man ein Stück öffnet."),
            ol(["Öffne in Guitar Pro eine Datei (zum Beispiel ein Gratis-Stück) und drücke <b>Play</b>.", "Ändere das <b>Tempo</b> und schalte einzelne Spuren (Gitarre, Bass, Schlagzeug) stumm.", "Setze eine Schleife über eine Stelle, die du üben willst.",
                "Öffne dasselbe Stück auf Ultimate Guitar: Dort siehst du Akkorde und Tab. Mit der App ist das Playalong gleich angepasst abspielbar.", 'Öffne auf <a href="https://www.soundslice.com/guitar-pro-viewer/" target="_blank" rel="noopener">soundslice.com/guitar-pro-viewer</a> eine Guitar-Pro-Datei im Browser.']),
        ])),
        ("umsetzung", "Kleine Umsetzung: ein Stück zum Üben", "20&ndash;30 Min.", "\n".join([
            p("<b>Auftrag:</b> Suche ein Stück, das du üben möchtest, und bereite es zum Üben vor."),
            ol(["Suche das Stück auf Ultimate Guitar oder in mySongBook und öffne es.", "Verlangsame es auf ein Tempo, in dem du mitspielen oder singen kannst.", "Schalte die Spur deines Instruments stumm, damit du zur Band übst.", "Notiere dir die schwierigsten zwei Takte und übe sie in der Schleife."]),
            check("gp", ["ein Stück läuft in Guitar Pro oder im Browser,", "du hast das Tempo verändert,", "du hast eine Spur stummgeschaltet und mit der Band geübt."]),
        ])),
    ],
    stolper=["<b>Player-Modus:</b> Nach der Testzeit lassen sich Stücke nur noch abspielen. Zum Bearbeiten brauchst du eine Lizenz.", "<b>Kosten:</b> mySongBook ist ein Abo. Ultimate Guitar hat ein Gratis-Angebot mit Einschränkungen.",
             "<b>Qualität der Tabs:</b> Tabs von Nutzenden können Fehler enthalten. Vergleiche mit einer Aufnahme.", "<b>Urheberrecht:</b> Tabs und Noten nur für das eigene Üben und den Unterricht im geschlossenen Rahmen weitergeben."],
    quellen=[("Guitar Pro: Installation (Docs)", "https://www.guitar-pro.com/docs/gp8/basics/installation"), ("Guitar Pro: mySongBook (Docs)", "https://www.guitar-pro.com/docs/gp8/mysongbook"),
             ("Guitar Pro: Support", "https://support.guitar-pro.com/"), ("Soundslice: Guitar Pro Viewer", "https://www.soundslice.com/guitar-pro-viewer/")],
))

# ------------------------------------------------------------------ iReal Pro
GUIDES.append(dict(
    slug="ireal-pro", title="iReal Pro", title_long="iReal Pro: Playalong aus Akkorden",
    eyebrow="Playalongs · Beispiel 7, 8",
    lead="Akkorde eingeben und eine Band spielen lassen, in deinem Tempo und deiner Tonart.",
    card="Begleitautomat mit Akkordeingabe.", diff_kurz="leicht bis mittel", bsp=["B7", "B8"],
    zeit="ca. 45 Minuten", diff="leicht bis mittel", geraet="Handy, Tablet oder Computer (App)", kosten="App, Preis im Store prüfen",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "5 Min.", "\n".join([
            p("iReal Pro ist ein Begleitautomat: Du gibst die Akkorde eines Stücks ein, wählst einen Stil, und eine virtuelle Band (Klavier, Bass, Schlagzeug) begleitet dich. Es gibt eine grosse Sammlung von Stücken, die andere Nutzende geteilt haben."),
            h3("Das brauchst du"),
            ul(["iPhone, iPad, Android-Gerät, Mac oder Windows-Computer", "Die App aus dem Store (kostenpflichtig, Preis im Store prüfen)", "Ein Stück mit Akkorden, zum Beispiel aus einem Liederbuch"]),
        ])),
        ("start", "Installieren", "10 Min.", "\n".join([
            ol(['Lade iReal Pro aus dem App Store, Play Store oder von <a href="https://www.irealpro.com/" target="_blank" rel="noopener">irealpro.com</a> (Mac, Windows) herunter.', "Starte die App. Sie enthält schon einige Beispielstücke zum Hören."]),
        ])),
        ("erste", "Erste Schritte zum Testen", "15 Min.", "\n".join([
            tut("https://www.irealpro.com/video-tutorials", "iReal Pro: Videotutorials des Herstellers (Englisch)", "Darunter «Input a song in less than 3 mins», das zeigt, wie man ein Stück eingibt."),
            ol(["Öffne ein Beispielstück und drücke <b>Play</b>.", "Ändere das <b>Tempo</b>, den <b>Stil</b> (zum Beispiel Swing oder Bossa Nova) und die Tonart.", "Schalte einzelne Instrumente der Band im Mixer stumm, zum Beispiel das Klavier, wenn du selber Akkorde spielen willst."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: ein eigenes Playalong", "20&ndash;30 Min.", "\n".join([
            p("<b>Auftrag:</b> Erfasse ein Stück mit den Akkorden, die du kennst, und lass dich von der Band begleiten."),
            ol(["Lege ein neues Stück an (Plus-Knopf, bei Mac das Plus oben rechts oder <b>Cmd+N</b>, bei Windows der Stift oder <b>Strg+N</b>).", "Wähle eine Vorlage, vergib einen Titel und stelle die Tonart ein.", "Gib die Akkorde Takt für Takt ein. Die erlaubten Akkordsymbole stehen in der Anleitung des Herstellers.",
                "Wähle einen Stil und spiele das Stück ab. Passe Tempo und Tonart an deine Stimme an.", "Dupliziere das Stück, bevor du viel experimentierst, damit du die Ausgangsfassung behältst."]),
            check("ir", ["dein Stück ist mit Akkorden erfasst,", "die Band spielt es in deinem Tempo,", "du hast die Tonart mindestens einmal geändert."]),
        ])),
    ],
    stolper=["<b>Kein Notenimport:</b> iReal Pro kann kein PDF, MIDI oder MusicXML in ein Stück verwandeln. Die Akkorde musst du selber eingeben oder aus der Sammlung der Community holen.", "<b>Kosten:</b> Die App ist kostenpflichtig. Preise unterscheiden sich je nach Gerät.",
             "<b>Urheberrecht:</b> Die Sammlung wird von Nutzenden gepflegt, dort gelten fremde Urheberrechte. Nutze die Stücke für das eigene Üben."],
    quellen=[("iReal Pro: Song erstellen", "https://www.irealpro.com/learn/create-a-song"), ("iReal Pro: Videotutorials", "https://www.irealpro.com/video-tutorials"), ("iReal Pro: Dokumentation", "https://www.irealpro.com/documentation/")],
))

# ------------------------------------------------------------------ DaVinci Resolve
GUIDES.append(dict(
    slug="davinci-resolve", final=True, title="DaVinci Resolve", title_long="DaVinci Resolve: Multispurvideo schneiden",
    eyebrow="Video · Beispiel 3, 5",
    lead="Mehrere Aufnahmen auf einer Tonspur synchron schneiden und nebeneinander zeigen, zum Beispiel für ein Multispurvideo mit Notenrolle.",
    card="Installieren, ausprobieren, Multispurvideo schneiden.", diff_kurz="mittel bis schwierig", bsp=["B3", "B5"],
    zeit="ca. 2&ndash;3 Stunden", diff="mittel bis schwierig", geraet="Computer (Mac, Windows), iPad-Version vorhanden", kosten="Gratisversion reicht",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "10 Min.", "\n".join([
            p("DaVinci Resolve ist ein Videoschnittprogramm von Blackmagic Design. Die Gratisversion reicht für unser Multispurvideo. Du schneidest mehrere Aufnahmen (zum Beispiel jede Stimme einzeln) auf dieselbe Tonspur und zeigst sie nebeneinander."),
            h3("Das brauchst du"),
            ul(["Einen Computer mit genügend Speicher und Leistung (Mac oder Windows, am Praxistag notfalls im Computerraum der HSLU) oder ein iPad mit der iPad-Version", "Etwa 1&ndash;2 Stunden Zeit für Download und Installation, am besten <b>vor</b> dem Praxistag",
                "Deine Aufnahmen als Videodateien und eine Tonspur zum Synchronisieren, zum Beispiel einen mp3-Export aus Noteflight als Pilotspur", "Kopfhörer"]),
            note("Vor dem Praxistag", "Installiere DaVinci Resolve zu Hause. Der Download ist gross und dauert auch bei schnellem Internet lange."),
        ])),
        ("start", "Installieren", "30&ndash;60 Min.", "\n".join([
            ol(['Öffne <a href="https://www.blackmagicdesign.com/products/davinciresolve" target="_blank" rel="noopener">blackmagicdesign.com/products/davinciresolve</a> und lade die <b>kostenlose Version</b> für dein System herunter. Je nach Seite brauchst du ein Anmeldeformular mit E-Mail-Adresse.',
                "Installiere das Programm wie jedes andere (Mac: Datei öffnen und ins Programme-Verzeichnis ziehen, Windows: Installer ausführen).", "Starte Resolve. Beim ersten Start fragt es nach Einstellungen und Speicherort. Die Voreinstellungen sind in Ordnung.",
                "Lege über <b>Neues Projekt</b> ein Projekt an und gib ihm einen Namen."]),
        ])),
        ("erste", "Erste Schritte zum Testen", "30 Min.", "\n".join([
            tut("https://www.tutkit.com/de/text-tutorials/1829-davinci-resolve-audio-synchronisieren-leicht-gemacht", "tutkit: DaVinci Resolve Audio synchronisieren (Textanleitung, Deutsch)", "Zeigt zwei Wege: von Hand an der Wellenform und automatisch mit «Autosync Audio». Menüs können je nach Version abweichen."),
            yt("DaVinci Resolve Einsteiger Tutorial deutsch Schnitt", "Wähle ein aktuelles Video zur Version, die du installiert hast."),
            ol(["Importiere deine Videodateien und die Tonspur auf der Seite <b>Medien</b> (Media).", "Wechsle auf die Seite <b>Schnitt</b> (Cut oder Edit) und ziehe die Tonspur und einen Clip in die Timeline.",
                "Spiele ab und prüfe, ob Bild und Ton zusammenpassen."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: Multispurvideo mit drei Spuren", "60&ndash;90 Min.", "\n".join([
            p("<b>Auftrag:</b> Setze drei Aufnahmen auf einer Tonspur synchron zusammen und zeige sie nebeneinander."),
            ol(["Lege die Tonspur (Pilotspur) in die Timeline und je eine Videoaufnahme auf eine eigene Videospur darüber.", "Synchronisiere jede Aufnahme mit der Tonspur (Autosync Audio «basierend auf Wellenformen», oder von Hand an der Wellenform).",
                "Stelle die Bilder nebeneinander: Wähle einen Clip, öffne im <b>Inspektor</b> (Inspector) die Transformationen und ändere <b>Zoom</b> und <b>Position</b>, bis die drei Bilder nebeneinander passen.",
                "Schalte die Tonspuren der einzelnen Clips stumm, wenn die Pilotspur den Ton liefert, oder mische die Tonspuren ab.", "Exportiere das Ergebnis auf der Seite <b>Ausgabe</b> (Deliver) als MP4."]),
            check("dv", ["drei Aufnahmen laufen synchron zusammen,", "die Bilder sind nebeneinander angeordnet,", "du hast eine MP4-Datei exportiert und angehört."]),
            h3("Wenn du weitermachen willst"),
            ul(["Füge die Notenrolle (Bildschirmaufnahme aus Noteflight) als weitere Spur hinzu.", "Bette das fertige Video in Moodle ein (Anleitung zum Moodle-Kurs)."]),
        ])),
    ],
    stolper=["<b>Leistung:</b> Auf älteren Geräten ruckelt die Vorschau. Das Ergebnis ist trotzdem in Ordnung. Schneide in kurzen Stücken.", "<b>Dateien:</b> Resolve verknüpft Videodateien. Verschiebe sie nicht nach dem Import.",
             "<b>Kopfhörer:</b> Ohne Kopfhörer nehmen die Aufnahmen die Pilotspur mit auf und alles klingt doppelt.", "<b>Version:</b> Menüs und Namen unterscheiden sich je nach Version. Halte dich an die Wörter in deinem Programm."],
    quellen=[("Blackmagic Design: DaVinci Resolve", "https://www.blackmagicdesign.com/products/davinciresolve"), ("tutkit: Audio synchronisieren", "https://www.tutkit.com/de/text-tutorials/1829-davinci-resolve-audio-synchronisieren-leicht-gemacht"),
             ("tutkit: Multicam-Schnitt", "https://www.tutkit.com/de/text-tutorials/1799-meistere-den-multicam-schnitt-in-davinci-resolve")],
))

# ------------------------------------------------------------------ openDAW
GUIDES.append(dict(
    slug="opendaw", final=True, title="openDAW", title_long="openDAW: Musik produzieren im Browser",
    eyebrow="Producing · Beispiel 4",
    lead="Einen kurzen Beat im Browser bauen, ohne Anmeldung und ohne Installation.",
    card="DAW im Browser, ohne Registrierung.", diff_kurz="leicht bis schwierig", bsp=["B4"],
    zeit="ca. 45&ndash;60 Minuten", diff="leicht bis schwierig", geraet="Computer mit Browser", kosten="gratis, ohne Registrierung",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "5 Min.", "\n".join([
            p("openDAW ist eine DAW (Programm zum Musikproduzieren) im Browser. Es braucht keine Registrierung und keine Installation. Es hat eine Tutorial-Funktion für die Tastatur und einen Visualteil. Wer Code mag, kann Musik sogar mit Prompts erzeugen."),
            h3("Das brauchst du"),
            ul(["Computer mit aktuellem Browser (wenn etwas nicht läuft, probiere Chrome)", "Kopfhörer", "Etwas Geduld: openDAW ist ein junges Programm und verändert sich schnell"]),
        ])),
        ("start", "Öffnen", "5 Min.", "\n".join([
            ol(['Öffne <a href="https://opendaw.studio/" target="_blank" rel="noopener">opendaw.studio</a>.', "Erlaube dem Browser bei Nachfrage die Audio-Wiedergabe. Eine Registrierung ist nicht nötig.", "Lege ein neues Projekt an."]),
            warn("Projekte nur im Browser", "Ob und wie ein Projekt gespeichert wird, hängt vom Browser und von der Version ab. Speichere dein Projekt als Datei oder exportiere den Ton, sobald du etwas Brauchbares hast."),
        ])),
        ("erste", "Erste Schritte zum Testen", "20 Min.", "\n".join([
            p("Ein offizielles Einsteigervideo habe ich nicht gefunden. Nutze die eingebaute Tutorial-Funktion von openDAW und probiere die Schritte unten aus."),
            yt("openDAW tutorial", "Die Videos zu openDAW sind noch selten. Wähle ein neues und prüfe es zuerst."),
            ol(["Füge eine Spur mit einem Schlagzeug oder Instrument hinzu.", "Zeichne im Raster ein paar Noten oder Schläge und drücke <b>Play</b>.", "Ändere das Tempo und höre dir den Unterschied an.", "Füge eine zweite Spur (zum Beispiel einen Bass) hinzu."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: ein 8-Takt-Beat", "30&ndash;45 Min.", "\n".join([
            p("<b>Auftrag:</b> Baue einen Beat von acht Takten mit Schlagzeug, Bass und einem Klang deiner Wahl."),
            ol(["Lege ein Tempo fest (zum Beispiel 90 BPM für einen ruhigen Hip-Hop-Groove).", "Baue den Schlagzeug-Rhythmus aus Kick, Snare und Hi-Hat.", "Füge eine einfache Basslinie hinzu, die dem Rhythmus folgt.", "Füge einen dritten Klang hinzu und spiele alles zusammen ab.", "Speichere das Projekt oder exportiere den Ton."]),
            check("od", ["der Beat läuft acht Takte lang,", "du hast mindestens drei Spuren,", "du hast dein Ergebnis gespeichert oder exportiert."]),
            h3("Wenn du weitermachen willst"),
            ul(["Probiere den Code-Editor aus (nächster Abschnitt): Mit einem Auftrag an Claude lässt sich ein Beat als Code beschreiben.", "Vergleiche mit dem Koala Sampler auf dem Handy (Anleitung zum Koala Sampler)."]),
        ])),
        ("code", "Code-Editor: Musik als Code", "20&ndash;30 Min.", "\n".join([
            p("openDAW hat einen eingebauten <b>Script Editor</b>. Dort beschreibst du ein ganzes Projekt als Text (TypeScript): Tempo, Instrumente, Noten und Effekte. Ein Klick auf <b>Run</b>, und das Projekt öffnet sich im Studio. Das ist nachvollziehbar, lässt sich beliebig wiederholen und ist leicht abzuwandeln."),
            p("Das Skript unten hat Claude Code geschrieben, nachdem es die Scripting Docs auf opendaw.studio gelesen hat. Es baut einen <b>8-Takt-Hip-Hop-Beat</b> in a-Moll mit 88 BPM: Schlagzeug, 808-Bass, Pad (Akkordfolge Am9, Fmaj9, Dm9, E7(b9)) und eine Hookline als Frage und Antwort."),
            h3("So führst du das Skript aus"),
            ol(['Öffne <a href="https://opendaw.studio/" target="_blank" rel="noopener">opendaw.studio</a> und lege ein neues Projekt an.', "Öffne im Menü <b>openDAW</b> den <b>Script Editor</b>.",
                "Lösche den Beispieltext im Editor, füge den Code von unten ein (Button <b>Kopieren</b>) und klicke auf <b>Run</b>.", "Das neue Projekt «Midnight Hook» öffnet sich im Studio. Drücke <b>Play</b>."]),
            code(CODE_OPENDAW),
            p('Den Code gibt es auch als Datei: <a href="../beispiele/opendaw-midnight-hook.txt" download>opendaw-midnight-hook.txt</a> (reiner Text, Endung beim Einfügen egal).'),
            h3("Selber abwandeln"),
            ul(["<b>Tempo:</b> Ändere <code>project.bpm = 88</code> zum Beispiel auf <code>100</code>.", "<b>Länge:</b> <code>const BARS = 8</code> bestimmt die Takte. Die Muster sind auf 8 Takte ausgelegt, ändere es nur mit Bedacht.",
                "<b>Akkorde:</b> Die Liste <code>chords</code> enthält die Akkorde als Tonnummern (MIDI). Tausche einen Akkord aus und höre, was passiert.", "<b>Melodie:</b> Die Listen <code>call</code>, <code>answer</code> und <code>resolve</code> enthalten die Hookline als [Position, Länge, Tonhöhe].",
                "<b>Klang:</b> Zahlen bei <code>cutoff</code>, <code>attack</code> oder <code>volume</code> ändern den Klang der Instrumente."]),
            h3("Mit KI selber ein Skript erzeugen"),
            p("Gib einer KI (zum Beispiel Claude) den Auftrag, ein Skript nach den Scripting Docs von openDAW zu schreiben. Ein Beispiel für den Auftrag:"),
            code("Lies die Scripting Docs auf opendaw.studio. Schreibe ein openDAW-Skript (TypeScript), das einen 8-Takt-Beat in [Stil] mit [Tempo] BPM erzeugt: Schlagzeug, Bass und eine einfache Melodie. Es soll mit openDAW.newProject() beginnen und mit project.openInStudio() enden."),
            note("Wichtig", "Die KI muss die aktuellen Scripting Docs kennen. Ohne sie erfindet sie Befehle, die es nicht gibt. Läuft das Skript nicht, kopiere die Fehlermeldung des Editors zurück in den Chat und lass es korrigieren."),
            warn("Fremden Code nur mit Vorsicht ausführen", "Ein Skript läuft in deinem Browser. Führe nur Code aus, den du von einer vertrauenswürdigen Quelle hast und zumindest grob verstehst. Dieser Code stammt aus dem Praxistag und tut nichts anderes, als ein Projekt zu bauen."),
        ])),
    ],
    stolper=["<b>Neues Programm:</b> Funktionen und Menüs ändern sich. Wenn etwas anders aussieht, folge dem, was du siehst.", "<b>Browser:</b> Nicht jede Funktion läuft in jedem Browser. Wechsle im Zweifel auf Chrome.", "<b>Speichern:</b> Ohne Anmeldung liegt dein Projekt nur auf deinem Gerät. Sichere es."],
    quellen=[("openDAW", "https://opendaw.studio/"), ("openDAW auf GitHub", "https://github.com/andremichelle/openDAW")],
))

# ------------------------------------------------------------------ Koala Sampler
GUIDES.append(dict(
    slug="koala-sampler", title="Koala Sampler", title_long="Koala Sampler: Beats mit dem Handy",
    eyebrow="Producing · Beispiel 4",
    lead="Eigene Klänge aufnehmen, auf Pads legen und zu einem kleinen Beat zusammensetzen.",
    card="Sampling, geeignet für die Schulmusik.", diff_kurz="mittel", bsp=["B4"],
    zeit="ca. 45&ndash;60 Minuten", diff="mittel", geraet="iPhone, iPad oder Android (App)", kosten="App, Preis im Store prüfen",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "5 Min.", "\n".join([
            p("Koala Sampler ist eine App, mit der du Klänge aufnimmst, auf Pads verteilst und zu Beats zusammenbaust. Sie eignet sich für die Schulmusik mit Jugendlichen, weil man ohne Vorkenntnisse schnell ein Ergebnis hat."),
            h3("Das brauchst du"),
            ul(["Ein iPhone, iPad oder Android-Gerät", "Die App «Koala Sampler» aus dem Store (kostenpflichtig, Preis im Store prüfen)", "Kopfhörer oder einen Lautsprecher"]),
        ])),
        ("start", "Installieren", "10 Min.", "\n".join([
            ol(["Suche im App Store oder Play Store nach <b>Koala Sampler</b> und installiere die App.", "Starte die App und erlaube den Zugriff auf das Mikrofon, damit du Klänge aufnehmen kannst."]),
        ])),
        ("erste", "Erste Schritte zum Testen", "20 Min.", "\n".join([
            tut("https://violetrecording.com/how-to-use-koala-sampler/", "Violet Recording: How to use Koala Sampler (Englisch)", "Erklärt Aufnehmen, Zerschneiden, Spielen und Sequenzieren in einer Übersicht."),
            yt("Koala Sampler Basic Tutorial", "Der Entwickler (elf audio) hat englische Einsteigervideos. Auf Deutsch habe ich keines gefunden."),
            ol(["Tippe auf ein leeres Pad und nimm einen Klang auf, zum Beispiel Klatschen oder deine Stimme.", "Schneide den Klang so zu, dass nur der gewünschte Teil bleibt.", "Spiele den Klang auf den Pads und probiere verschiedene Tonhöhen aus."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: ein Beat aus eigenen Klängen", "30&ndash;45 Min.", "\n".join([
            p("<b>Auftrag:</b> Baue mit vier selbst aufgenommenen Klängen einen Beat von zwei Takten."),
            ol(["Nimm vier Klänge auf: einen tiefen (Kick), einen hellen (Snare), einen kurzen (Hi-Hat) und einen melodischen.", "Lege jeden Klang auf ein eigenes Pad.", "Nimm im Sequenzer ein Muster von zwei Takten auf, indem du die Pads im Takt antippst.", "Füge einen Effekt hinzu (zum Beispiel Hall) und spiele den Beat ab.", "Exportiere den Beat als Audiodatei."]),
            check("ko", ["du hast vier eigene Klänge aufgenommen,", "dein Beat läuft zwei Takte lang,", "du hast eine Audiodatei exportiert."]),
        ])),
    ],
    stolper=["<b>Mikrofon:</b> Erlaube dem Gerät den Mikrofonzugriff, sonst nimmt die App nichts auf.", "<b>Lärm:</b> Nimm in einer ruhigen Umgebung auf, sonst hört man den Raum auf jedem Klang.", "<b>Kosten:</b> Die App ist kostenpflichtig. Für den Praxistag genügt, wenn eine Person sie zeigt.", "<b>Urheberrecht:</b> Samples aus fremden Liedern nicht öffentlich weitergeben."],
    quellen=[("Koala Sampler im App Store", "https://apps.apple.com/ch/app/id1449584007"), ("Violet Recording: How to use Koala Sampler", "https://violetrecording.com/how-to-use-koala-sampler/")],
))

# ------------------------------------------------------------------ Moodle
GUIDES.append(dict(
    slug="moodle-kurs", final=True, title="Moodle-Kurs", title_long="Moodle: Kursinhalte erstellen und Video einbetten",
    eyebrow="Hosten · Beispiel 5",
    lead="In deinem persönlichen Moodle-Kurs eine Seite oder ein E-Book anlegen und ein Video einbetten.",
    card="Kurs ausprobieren, Inhalte erstellen, Video einbetten.", diff_kurz="mittel", bsp=["B5"],
    zeit="ca. 60&ndash;90 Minuten", diff="mittel", geraet="Computer mit Browser", kosten="Zugang kommt von Marc",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "5 Min.", "\n".join([
            p("Moodle ist eine Lernplattform. In deinem persönlichen Kurs legst du Abschnitte an und füllst sie mit Texten, Dateien, Videos und kleinen Aufgaben. Ein <b>Buch</b> (E-Book) ist eine Aktivität mit mehreren Kapiteln, eine <b>Seite</b> ist ein einzelner Text mit Medien."),
            h3("Das brauchst du"),
            ul(["Einen Moodle-Zugang mit Kursrechten (bekommst du von Marc für den Praxistag)", "Ein Video, das schon online liegt (zum Beispiel auf Vimeo oder YouTube)", "Einen Browser"]),
        ])),
        ("start", "Anmelden", "10 Min.", "\n".join([
            ol(["Öffne die Moodle-Adresse, die dir Marc mitteilt, und melde dich mit deinen Zugangsdaten an.", "Öffne deinen persönlichen Kurs.", "Schalte oben rechts <b>Bearbeiten</b> ein. Erst dann siehst du die Knöpfe zum Anlegen und Ändern."]),
            warn("Zugangsdaten", "Gib dein Passwort nie weiter. Ändere das Startpasswort beim ersten Mal, wenn Moodle dazu auffordert."),
        ])),
        ("erste", "Erste Schritte zum Testen", "25 Min.", "\n".join([
            tut("https://docs.moodle.org/de/Video", "Moodle-Dokumentation: Video (Deutsch)", "Beschreibt, wie man Videos von externen Servern einbettet. Der Editor in deiner Version kann anders aussehen."),
            ol(["Klicke in einem Abschnitt auf <b>Aktivität oder Material anlegen</b> und wähle <b>Seite</b> (oder <b>Buch</b>).", "Gib einen Namen ein und schreibe einen kurzen Text in das Textfeld.", "Speichere und öffne die Seite wie ein Teilnehmender."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: eine Seite mit Video", "30&ndash;45 Min.", "\n".join([
            p("<b>Auftrag:</b> Lege eine Seite an, die ein Video einbettet und kurz erklärt, was die Lernenden damit tun sollen."),
            ol(["Lege eine neue Seite an und schreibe zwei Sätze Aufgabe.", "Kopiere den <b>Einbettungscode</b> deines Videos (bei Vimeo und YouTube unter «Teilen», «Einbetten»).",
                "Schalte im Textfeld in die <b>HTML-Ansicht</b> (Symbol mit spitzen Klammern, oft über «Weitere Schaltflächen») und füge den Code ein. Das bettet das Video so ein, dass es auch auf dem Handy passt.",
                "Speichere und prüfe: Läuft das Video, wenn du die Seite als Gast oder mit einem Testzugang öffnest?", "Teste den Kurs gegenseitig mit einer Kollegin oder einem Kollegen."]),
            check("mk", ["deine Seite ist angelegt und gespeichert,", "das Video läuft in der Seite,", "eine andere Person konnte die Seite öffnen und abspielen."]),
            h3("Wenn du weitermachen willst"),
            ul(["Lege ein <b>Buch</b> mit mehreren Kapiteln an: ein Kapitel pro Instrument oder Thema.", "Verlinke eine Anleitung von <b>digi.marcscheidegger.ch</b> in deinem Kurs."]),
        ])),
    ],
    stolper=["<b>Bearbeiten einschalten:</b> Ohne diesen Schalter siehst du keine Knöpfe zum Anlegen.", "<b>Video nicht sichtbar:</b> Prüfe, ob das Video auf Vimeo oder YouTube öffentlich oder per Link freigegeben ist.",
             "<b>Editor sieht anders aus:</b> Je nach Moodle-Version heisst der Editor und das Menü anders. Suche nach dem Symbol für HTML oder Medien.", "<b>Urheberrecht:</b> Lege geschützte Noten und Aufnahmen nur im Kurs mit Anmeldung ab."],
    quellen=[("Moodle-Dokumentation: Video", "https://docs.moodle.org/de/Video"), ("Moodle-Dokumentation (Deutsch)", "https://docs.moodle.org/de/")],
))

# ------------------------------------------------------------------ Website mit KI
GUIDES.append(dict(
    slug="website-mit-ki", title="Website mit KI", title_long="Website mit KI: erzeugen und lokal testen",
    eyebrow="Hosten · Beispiel 2",
    lead="Eine einfache Website von einer KI schreiben lassen, auf dem eigenen Computer öffnen und anpassen.",
    card="HTML, CSS und JS erzeugen lassen und lokal testen, Jimdo.", diff_kurz="mittel", bsp=["B2"],
    zeit="ca. 60&ndash;90 Minuten", diff="mittel", geraet="Computer mit Browser und einem Texteditor", kosten="gratis (KI-Zugang vorausgesetzt)",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "10 Min.", "\n".join([
            p("Eine Website besteht aus Dateien: <b>HTML</b> (Inhalt), <b>CSS</b> (Aussehen) und manchmal <b>JavaScript</b> (Verhalten). Eine KI wie Claude kann sie nach deiner Beschreibung schreiben. Du speicherst sie auf dem Computer, öffnest sie im Browser und passt sie an. Erst danach überlegst du, wo sie gehostet wird."),
            h3("Das brauchst du"),
            ul(["Einen Zugang zu einer KI (zum Beispiel Claude)", "Einen Texteditor (Mac: «TextEdit» im Nur-Text-Modus, Windows: Editor, besser ein Code-Editor)", "Einen Browser", "Einen kurzen Plan: Wofür ist die Seite, und für wen?"]),
            note("Muss es sofort Git und Server sein?", "Nein. Fang lokal an: Datei speichern, im Browser öffnen, anpassen. Hosting kommt später. Alternative ohne Code: eine Jimdo-Seite, die eine KI nach deiner Vorlage erstellen lässt."),
        ])),
        ("start", "Plan und Prompt", "20 Min.", "\n".join([
            ol(["Schreibe in fünf Sätzen auf: Wer bist du, was bietest du an, für wen, und was sollen Besuchende tun (zum Beispiel anrufen, schreiben, anmelden)?", "Sammle, was auf die Seite soll: Name, Foto, Kurztext, drei Angebote, Kontakt.",
                "Gib diese Angaben der KI mit einem klaren Auftrag, zum Beispiel: «Schreibe mir eine einfache Website mit einer Seite, Abschnitte Über mich, Angebote und Kontakt, schlicht, gut lesbar auf dem Handy. Liefere eine einzige Datei index.html mit eingebautem CSS.»"]),
            warn("Datenschutz", "Gib der KI keine privaten Angaben anderer Personen (Namen, Adressen, Fotos), die nicht öffentlich werden sollen."),
        ])),
        ("erste", "Erste Schritte zum Testen", "20 Min.", "\n".join([
            yt("HTML Website lokal öffnen index.html Anfänger", "Falls du das Speichern und Öffnen noch nie gemacht hast."),
            ol(["Kopiere den Code der KI in deinen Texteditor und speichere ihn als <code>index.html</code> in einem neuen Ordner.", "Doppelklicke auf die Datei. Sie öffnet sich im Browser.", "Lies die Seite durch und notiere drei Dinge, die du ändern möchtest."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: deine Seite verbessern", "30&ndash;45 Min.", "\n".join([
            p("<b>Auftrag:</b> Verbessere deine Seite in drei Runden und prüfe sie auf dem Handy."),
            ol(["Sag der KI, was du ändern möchtest, in kurzen Sätzen («Farbe ruhiger», «Kontaktblock mit E-Mail»). Ersetze den Code in deiner Datei.", "Lade die Seite im Browser neu (<kbd>Cmd+R</kbd> oder <kbd>F5</kbd>).", "Öffne die Datei auf dem Handy (zum Beispiel per AirDrop oder Mail) oder verkleinere das Browserfenster, um die schmale Ansicht zu testen."]),
            check("ws", ["deine Seite öffnet sich lokal im Browser,", "du hast sie dreimal mit der KI verbessert,", "sie sieht auch in der schmalen Ansicht gut aus."]),
            h3("Wenn du weitermachen willst"),
            ul(["<b>Jimdo:</b> Lass die KI eine Jimdo-Seite nach deiner Vorlage erstellen. Das geht ohne Code, du brauchst nur ein Konto.", "<b>Hosten:</b> Lade die Datei bei deinem Hosting hoch oder lege sie im Moodle-Kurs ab (Anleitung zum Moodle-Kurs)."]),
        ])),
    ],
    stolper=["<b>Eine Datei:</b> Wenn die KI mehrere Dateien liefert, speichere sie im gleichen Ordner und halte die Namen genau ein.", "<b>Bilder:</b> Verwende nur Bilder, die du verwenden darfst, und halte sie klein.", "<b>Impressum und Datenschutz:</b> Eine öffentliche Seite braucht beides. Eine KI schreibt dir eine Vorlage, prüfe sie aber selbst.", "<b>Alte Fassung sichern:</b> Speichere vor grossen Änderungen eine Kopie der Datei."],
    quellen=[("MDN: Erste Schritte mit HTML (Deutsch)", "https://developer.mozilla.org/de/docs/Learn/Getting_started_with_the_web"), ("Jimdo", "https://www.jimdo.com/")],
))

# ------------------------------------------------------------------ Konzeptarbeit
GUIDES.append(dict(
    slug="konzeptarbeit", title="Konzeptarbeit", title_long="Konzeptarbeit: vom Ist-Zustand zum Konzept",
    eyebrow="Konzipieren · Beispiel 1, 8",
    lead="Mit einer KI den Ist-Zustand analysieren, Handlungsfelder finden und ein einfaches Konzept formulieren.",
    card="Ist-Zustand, Handlungsfelder, Konzept.", diff_kurz="mittel bis schwierig", bsp=["B1", "B8"],
    zeit="ca. 60&ndash;90 Minuten", diff="mittel bis schwierig", geraet="Computer oder Tablet mit KI-Zugang", kosten="gratis (KI-Zugang vorausgesetzt)",
    steps=[
        ("basics", "Basics: Was ist das, was brauche ich?", "5 Min.", "\n".join([
            p("Konzeptarbeit ist der Teil, den keine KI für dich übernimmt: Du entscheidest, was du erreichen willst. Die KI hilft beim Sortieren, Nachfragen und Formulieren. Das Konzept hat drei Teile: den <b>Ist-Zustand</b>, die <b>Handlungsfelder</b> und das <b>Konzept</b> mit ersten Schritten."),
            h3("Das brauchst du"),
            ul(["Ein Thema, das dich beschäftigt (zum Beispiel dein Unterricht, ein Projekt oder dein eigenes Üben)", "Einen Zugang zu einer KI", "Papier oder eine Notizapp"]),
        ])),
        ("start", "Ist-Zustand beschreiben", "20 Min.", "\n".join([
            ol(["Schreibe selber in Stichworten auf: Wo stehe ich? Was läuft gut, was nicht? Was habe ich schon?", "Gib die Stichworte der KI und bitte sie, <b>Rückfragen</b> zu stellen, bevor sie etwas vorschlägt."]),
            note("Ein Prompt zum Start", "«Ich beschreibe dir meinen Ist-Zustand. Stelle mir erst fünf Rückfragen, bevor du etwas vorschlägst. Danach fasse den Ist-Zustand in zehn Zeilen zusammen.»"),
            warn("Datenschutz", "Gib keine Namen oder vertraulichen Angaben zu Schülerinnen, Schülern oder Kolleginnen ein."),
        ])),
        ("erste", "Handlungsfelder und Ziele", "20 Min.", "\n".join([
            ol(["Bitte die KI, aus dem Ist-Zustand drei bis fünf <b>Handlungsfelder</b> vorzuschlagen.", "Streiche, was nicht zu dir passt, und wähle ein bis zwei Felder aus.", "Formuliere pro Feld ein <b>Ziel</b>, das du in einem Monat überprüfen kannst."]),
        ])),
        ("umsetzung", "Kleine Umsetzung: dein Konzept auf einer Seite", "30&ndash;45 Min.", "\n".join([
            p("<b>Auftrag:</b> Fasse dein Konzept auf einer Seite zusammen."),
            ol(["Ist-Zustand in fünf Sätzen.", "Zwei Handlungsfelder mit je einem Ziel.", "Drei erste Schritte mit Termin.", "Eine Frage, die du am Nachmittag in deinem Auftritt beantwortest."]),
            check("kz", ["dein Ist-Zustand steht auf einer Seite,", "du hast zwei Ziele mit Termin,", "du hast die Vorschläge der KI geprüft und selbst entschieden."]),
        ])),
    ],
    stolper=["<b>Zu schnell auf Lösungen:</b> Lass die KI zuerst fragen, dann vorschlagen.", "<b>Alles glauben:</b> KI-Vorschläge klingen überzeugend, aber du kennst deine Situation besser.", "<b>Zu viele Ziele:</b> Zwei Ziele genügen für den Anfang."],
    quellen=[],
))

# ------------------------------------------------------------------ Index-Struktur
SOON = {
    "dorico": dict(title="Dorico SE", card="Installation, Ausprobieren, Soundbanks, Export und Import.", diff="mittel"),
    "daw": dict(title="GarageBand, Logic, Ableton", card="Playalongs bauen und Stimmen trennen in der DAW.", diff="mittel bis schwierig", bsp=["B7"]),
    "suno": dict(title="Suno und KI-Songtext", card="Komponieren und Songtexte mit KI.", diff="leicht bis mittel", bsp=["B4", "B7"]),
    "kdrive": dict(title="kDrive und Cloud", card="Noten und Dateien teilen.", diff="mittel", bsp=["B6"]),
}

GROUPS = [
    ("Notation", "Noten schreiben, finden, tauschen", ["noteflight", "guitar-pro", "musescore", "dorico"]),
    ("Playalongs", "Tempo, Tonhöhe, Stimmen trennen", ["moises", "anytune", "ireal-pro", "daw"]),
    ("Video", "Multispur, Notenrolle", ["davinci-resolve", "handyvideo"]),
    ("Producing und Songwriting", "", ["opendaw", "koala-sampler", "suno"]),
    ("Hosten und Konzept", "Moodle, Website, Cloud", ["moodle-kurs", "website-mit-ki", "kdrive", "konzeptarbeit"]),
]
