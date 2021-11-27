from globals import *
import heapq

def take_boat_off_the_dock(port,pierIndex):

    if port.tugboat.location == 'Puerto':
        port.currentTime += tugboat_transfer_generator()

    ship = port.piers[pierIndex].ship
    ship.endLoad = port.piers[pierIndex].endLoad
    

    arrival = ship.timeArrivalAtPier
    exit = ship.endLoad
    ship.timeOnDock = exit - arrival

    times = port.currentTime
    port.currentTime += take_boat_out_port_generator()
    ship.timeInPort = port.currentTime - ship.timeArrivalAtPort
    
    ship.timeout = (ship.timeArrivalAtPier - ship.timeArrivalAtPort) + (times - port.piers[pierIndex].endLoad)


    port.tugboat.location = 'Puerto'

    port.servedShips += 1

    print(f'Espera del ship {ship.id} en el muelle: {ship.timeOnDock / 60} ' )
    print(f'Tiempo del ship {ship.id} en el puerto: {ship.timeInPort / 60}'  )
    print(f'Espera del ship {ship.id} en colas del puerto: {ship.timeout / 60}'  )

    port.wait += ship.timeOnDock
    port.timeInPort += ship.timeInPort
    port.totalTimeout += ship.timeout

    port.piers[pierIndex].ship = None

def take_boat_to_the_dock(port, ship, pierIndex):
    
    if port.tugboat.location == 'Muelle':
        port.currentTime += tugboat_transfer_generator()

    port.currentTime += take_boat_to_dock_generator()
    ship.timeArrivalAtPier = port.currentTime
    pier = port.piers[pierIndex]
    pier.ship = ship
    pier.endLoad = port.currentTime + ship.loadTime
    port.tugboat.location = 'Muelle'
    heapq.heappush(port.events,((pier.endLoad,ship.id) , ("Fin de Carga" , ship , pierIndex)))