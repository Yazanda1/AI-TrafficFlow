
import traci

# SUMO starten und mit Python verbinden
traci.start([
    "sumo-gui",
    "-c",
    "data/cross.sumocfg",
    "--start"
])

# Ost-West bekommt zunächst Grün (Phase 2)
traci.trafficlight.setPhase("0", 2)

# 120 Simulationsschritte ausführen
for schritt in range(120):

    # Nächsten Simulationsschritt ausführen
    traci.simulationStep()

    # Aktuelle Ampelphase lesen
    phase = traci.trafficlight.getPhase("0")

    # Anzahl der am Sensor erkannten Fahrzeuge
    fahrzeuge = traci.inductionloop.getLastStepVehicleNumber("0")

    # Nur reagieren, wenn Ost-West Grün hat
    if phase == 2:

        if fahrzeuge > 0:
            # Fahrzeug aus Norden: Wechsel zu Gelb
            traci.trafficlight.setPhase("0", 3)
            print("Fahrzeug erkannt: Ampelwechsel!")

        else:
            # Kein Fahrzeug: Ost-West Grün halten
            traci.trafficlight.setPhase("0", 2)

    print("Zeit:", traci.simulation.getTime(),
          "Phase:", phase,
          "Sensor:", fahrzeuge)

# Verbindung beenden
traci.close()
