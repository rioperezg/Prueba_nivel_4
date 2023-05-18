"""
Kamala Khan alias Ms. Marvel es una adolescente Musulmana Pakistaní-estadounidense de Nueva Jersey. En el MCU tiene un linaje mutante 
latente activado unos misteriosos anillos que le dan una polimorfa con la capacidad de estirar su cuerpo de casi cualquier forma imaginable. 
Kamala era una gran fan de los superhéroes, especialmente de Carol Danvers, la antigua Ms. Marvel y por eso se ha convertido en una experta en 
redes sociales, pero nos ha pedido ayuda para implementar un grafo social y los algoritmos necesarios para atender los siguientes requerimientos:

 

cargar superhéroes de la siguiente tabla como vértices (puntos o nodos con los que están conformado los grafos. Llamaremos grado de un 
vértice, al número de aristas de las que es extremo) del grafo;
 

 

TWITTER

Iron Man

The increíble Hulk

Khan

Thor

Captain América

Ant-Man

Nick Fury

The Winter Soldier

Iron Man


cargar estos superhéroes con las siguientes etiquetas: Twitter, Instagram respectivamente, que representan si la persona del vértice origen 
sigue o es amigo de la persona del vértice destino;
 

hallar el árbol de expansión máximo para cada red social –considere el grafo como no dirigido para este punto–, es decir que las conexiones 
deben ser las de mayor peso –ósea el que tenga mayor interacción–; para lo cual, si desea utilizar Prim o Kruskal sin modificar el código, 
puede determinar la arista (relación entre dos vértices de un grafo) de mayor peso y cuando aplique este algoritmo, debe que considerar el 
peso de cada arista será la arista de mayor peso menos el peso de la arista;
 

determine si es posible conectar la persona Capitana Marvel con Nick Fury a través de la red social Twitter;
 

determine si es posible conectar la persona The Winter Soldier con Iron Man a través de cualquier red social;
 

indique a todas las personas que sigue a través de su red de Instagram Thor.
"""