
import traci

# 1. SUMO über Python starten
traci.start([
    "sumo-gui",
    "-c",
    "hello.sumocfg",
    "--start"
])

# 2. Die Simulation 80 Schritte ausführen
for schritt in range(80):

    # SUMO führt den nächsten Simulationsschritt aus
    traci.simulationStep()

    # Aktuelle Simulationszeit lesen
    zeit = traci.simulation.getTime()

    # Alle aktuell fahrenden Fahrzeuge abfragen
    fahrzeuge = traci.vehicle.getIDList()

    print("Zeit:", zeit)
    print("Fahrzeuge:", fahrzeuge)
    print("---------------------")

# 3. Verbindung zu SUMO schließen
traci.close()
