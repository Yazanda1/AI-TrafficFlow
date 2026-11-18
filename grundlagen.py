import csv
import numpy as np
# Anzahl der Fahrzeuge in fünf Messungen
fahrzeuge = [5, 8, 3, 10, 4]

# Funktion zur Berechnung der Gesamtanzahl
def gesamt_berechnen(werte):
    gesamt = 0

    for anzahl in werte:
        gesamt = gesamt + anzahl

    return gesamt


ergebnis = gesamt_berechnen(fahrzeuge)

print("Fahrzeuge insgesamt:", ergebnis)
# Liste in ein NumPy-Array umwandeln
array = np.array(fahrzeuge)

# Durchschnitt berechnen
durchschnitt = np.mean(array)

print("Durchschnitt:", durchschnitt)
# CSV-Datei erstellen
with open("verkehrsdaten.csv", "w", newline="") as datei:

    writer = csv.writer(datei)

    # Spaltenüberschriften
    writer.writerow(["Minute", "Fahrzeuge"])

    # Fahrzeugzahlen speichern
    for minute, anzahl in enumerate(fahrzeuge, start=1):
        writer.writerow([minute, anzahl])

print("CSV-Datei wurde erstellt!")