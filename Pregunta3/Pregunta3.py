"""
Dado un grafo no dirigido con personajes del MCU de la siguiente tabla:

 



 

 

Implementar los algoritmos necesarios para resolver las siguientes tareas:

 

cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos 
ambos personajes que se relacionan;
 

hallar el árbol de expansión máximo desde el vértice que contiene a Iron-Man, Thor y The Winter Soldier;
 

determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con 
dicho número
 

cargue todos los personajes de la tabla anterior
 

indicar qué personajes aparecieron en nueve episodios de la saga
"""
import colas, Grafos

grafo_superh = Grafos.Grafo(False)
# Primero cargamos el grafo con los personajes
dato = input("Ingrese el nombre del personaje: ")
while(dato != ""):
    Grafos.Arista.insertar_vertice(grafo_superh, dato)
    dato = input("Ingrese el nombre del personaje: ")
    # A continuacion realizamos un barrido para ver q vertices se unen

