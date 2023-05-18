"""
Nick Fury se encuentra en los cuarteles generales de S.H.I.E.L.D. y debe visitar a varios superhéroes para convencerlos de unirse para 
formar un grupo de vengadores, dado que es un asunto de suma importancia nos solicita implementar un algoritmo que permita determinar el 
recorrido de menor distancia –el menor posible, no importa que sea el óptimo– y terminar dicho recorrido de vuelta en los cuarteles (solo se 
puede pasar una vez por cada lugar).

 

Considere los siguientes superhéroes: S.H.I.E.L.D.

 

 

las distancias entre la localización de cada superhéroe están cargadas en la siguiente matriz:


"""


import colas, Grafos, Herramientas_necesarias

grafo_superh = Grafos.Grafo(False)
# Primero cargamos el grafo con los personajes
dato = input("Ingrese el nombre del personaje: ")
while(dato != ""):
    Grafos.Arista.insertar_vertice(grafo_superh, dato)
    dato = input("Ingrese el nombre del personaje: ")
    # A continuacion realizamos un barrido para ver q vertices se unen
while(vertice is not None):
    vertice = Grafos.Arista.barrido_vertices(grafo_superh)
    Episodios = input("Ingrese la cantidad de episodios en los que aparecieron juntos", vertice.info,"y", vertice.adyacentes.info, ":")
    Grafos.Arista.insertar_arista(grafo_superh, Episodios, vertice, vertice.adyacentes)
# A continuacion implementamos el algoritmo de Dijkstra para encontrar el camino mas corto
# Primero creamos una cola de prioridad con los vertices del grafo
while(vertice is not None):
    vertice = Grafos.Arista.barrido_vertices(grafo_superh)
    camino = Herramientas_necesarias.dijkstra(grafo_superh, vertice)
    print("El camino mas corto desde", vertice.info, "es:", camino)
    vertice = vertice.sig
    
