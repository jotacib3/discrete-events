def statics(port):
    if port.servedShips > 0:
        waitShips = port.wait / port.servedShips / 60
        timeInPort = port.timeInPort / port.servedShips / 60
        timeout = port.totalTimeout / port.servedShips / 60
        

        print("----------------------------------------------------------------------")
        print("Barcos atendidos: ", port.servedShips)
        print("Promedio total de demora de los barcos en el muelle en una corrida: ", waitShips )
        print("Promedio total del tiempo de los barcos en el puerto en una corrida: ", timeInPort )
        print("Promedio total del tiempo de espera de los barcos en las colass del puerto en una corrida: ", timeout )

        return (port.wait ,port.timeInPort  ,port.totalTimeout , port.servedShips)

    else:
        print("No se han atendido barcos")
        return 0,0,0,0