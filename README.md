
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
