 
import sys
from utils import *
from globals import *
from process import *
from statics import *
from entities import *

class PortSimulation():
    def __init__(self, simulationTime):
        self.piers = [Pier(),Pier(),Pier()]
        self.tugboat = Tugboat()
        self.simulationTime = simulationTime
        self.shipsQueue = []
        self.events = []
        self.currentTime = 0
        self.arrival = 0
        self.wait = 0
        self.totalTimeout = 0
        self.timeInPort = 0
        self.servedShips = 0
        self.shipId = 1
    
    def freePier(self):
        pos = [x for x in range(len(self.piers))  if self.piers[x].ship == None]
        if len(pos) > 0:
            return pos[0]
        return -1 
    

    def simulation(self):
        
        while self.currentTime < self.simulationTime :

            self.arrival += ship_arrival_generator() 
            nextArrival = self.arrival
            ship = Ship(id = self.shipId,arrivalTime = nextArrival)
            self.shipId += 1
            self.shipsQueue.append(ship)
            freePier = self.freePier()

            if freePier != -1:
                ship = self.shipsQueue.pop(0)
                heapq.heappush(self.events, ((ship.timeArrivalAtPort,ship.id), ("Llevar al Muelle", ship, freePier)))
            
                

            if len(self.events) > 0:
                evento = heapq.heappop(self.events)
                accion , ship , muelle = evento[1]

                if accion == "Llevar al Muelle":
                    self.currentTime = max(evento [0][0], self.currentTime)
                    take_boat_to_the_dock(self, ship,muelle)
                elif accion == "Fin de Carga":
                    self.currentTime = max(self.piers[muelle].endLoad,self.currentTime)
                    heapq.heappush(self.events, ((self.piers[muelle].endLoad, self.piers[muelle].ship.id ), ("Salir del Muelle", ship, muelle)))
                elif accion == "Salir del Muelle":
                    take_boat_off_the_dock(self, muelle)


def main():
    simulation_number = 0
    duration = 0
    numberOfBoats = 0
    timeoutPier = 0
    timeInPort = 0
    timeoutInPort = 0

    
    if len(sys.argv) < 3 :
        simulation_number = 45
        duration = 24

    else :
        simulation_number = int(sys.argv[1])
        duration = int(sys.argv[2])

    for i in range(simulation_number):
        print("#"*100)
        print(f"Simulación número : {i+1}")  
        p = PortSimulation(simulationTime = duration * 60)
        p.simulation()
        esperaBarcos ,timeInPort ,tiempoDeEspera , barcosAtendidos = statics(p)
        numberOfBoats += barcosAtendidos
        timeoutPier += esperaBarcos
        timeoutInPort += tiempoDeEspera
        timeInPort += timeInPort
    
    if numberOfBoats > 0:
        print("@"*100)
        print("Total de Barcos atendidos: ", numberOfBoats)
        print("Promedio total de demora de los barcos en el muelle en todas las corridas: ", timeoutPier / numberOfBoats /60 )
        print("Promedio total del tiempo de los barcos en el puerto en todas las corridas: ", timeInPort / numberOfBoats / 60 )
        print("Promedio total del tiempo de espera de los barcos en las colas del puerto en todas las corridas: ", timeoutInPort/ numberOfBoats / 60)
    else:
        print("No se atendieron barcos")

main()
