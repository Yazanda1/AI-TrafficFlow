
# AI-TrafficFlow

Bachelorprojekt: KI-gestützte Verkehrsanalyse und
adaptive Ampelsteuerung mit SUMO.

## Projektziel

Verkehrsvideos sollen analysiert werden, um
Fahrzeuge zu erkennen, zu verfolgen und
Verkehrskennzahlen zu berechnen.

Anschließend sollen in SUMO eine feste und
eine adaptive Ampelsteuerung verglichen werden.

## Aktueller Entwicklungsstand

WP0 - Grundlagen und Entwicklungsumgebung

Bisher umgesetzt:
- Virtuelle Python-Umgebung eingerichtet
- Python-Grundlagen mit Listen und Funktionen
- NumPy-Berechnungen
- CSV-Dateien erzeugen
- Verkehrsvideo mit OpenCV einlesen
- Erstes SUMO-Straßennetz erstellt
- Fahrzeugrouten in SUMO definiert
- SUMO über Python und TraCI gestartet
- Sensor ausgelesen und Ampelphase geändert

## Verwendete Technologien

- Python 3.12
- OpenCV
- NumPy
- SUMO
- TraCI
- Git

## Installation

Voraussetzungen:
- Python 3.12
- SUMO
- Git

Virtuelle Umgebung erstellen:

    py -3.12 -m venv .venv

Python-Bibliotheken installieren:

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt

## Programme starten

Python-Grundlagen:

    .\.venv\Scripts\python.exe grundlagen.py

Videoanalyse-Grundlage:

    .\.venv\Scripts\python.exe video_test.py

Erste SUMO-Simulation:

    sumo-gui -c sumo\hello\hello.sumocfg

TraCI-Grundtest:

    cd sumo\hello
    ..\..\.venv\Scripts\python.exe traci_test.py

Offizielles TraCI-Tutorial:

    cd sumo\traci_tutorial
    ..\..\.venv\Scripts\python.exe runner.py

Eigene Ampelsteuerung:

    cd sumo\traci_tutorial
    ..\..\.venv\Scripts\python.exe mein_controller.py

## Hinweise

- SUMO muss separat installiert werden.
- Verkehrsvideos werden nicht im Git-Repository gespeichert.
- Die späteren Arbeitspakete WP1 bis WP7
  werden schrittweise umgesetzt.
## Videoquelle fuer WP1

Datensatz:
City of Bellevue - Traffic Video Dataset

Quelle:
https://github.com/City-of-Bellevue/TrafficVideoDataset

Kreuzung:
150th Avenue / SE 38th Street, Bellevue, USA

Originalaufnahme:
Bellevue_150th_SE38th__2017-09-10_18-08-24.mp4

Fuer die ersten Untersuchungen wurde der Abschnitt
von Minute 30:00 bis 35:00 ausgewaehlt.

Lokaler Dateiname:
Bellevue_30_35.mp4

Eigenschaften:
- 1280 x 720 Pixel
- ca. 30 FPS
- ca. 5 Minuten
- feste Kameraperspektive
- sichtbare Ampelkreuzung und Warteschlangen

Das Video wird wegen seiner Groesse und der zu
pruefenden Nutzungsbedingungen nicht auf GitHub
hochgeladen.

Annotiertes Beispielbild:
documentation/evidence/Bellevue_Counting_Line.png

Die gelbe Linie ist eine vorgeschlagene Zaehlposition.
Die automatische Fahrzeugzaehlung ist noch nicht
Teil von WP0.