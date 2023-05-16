"""
Dado un grafo no dirigido con personajes del MCU de la siguiente tabla:

 

 

Iron Man

The increíble Hulk

Khan

Thor

Captain América

Ant-Man

Nick Fury

The Winter Soldier

Iron Man

 

6

0

1

8

7

3

2

The increíble Hulk

6

 

0

6

1

8

9

1

Khan

0

0

 

1

2

1

5

0

Thor

1

6

1

 

1

5

9

3

Captain América

8

1

2

1

 

2

4

5

Ant-Man

7

8

1

5

2

 

1

6

Nick Fury

3

9

5

9

4

1

 

1

The Winter Soldier

2

1

0

3

5

6

1

 

 

Implementar los algoritmos necesarios para resolver las siguientes tareas:

 

cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
 

hallar el árbol de expansión máximo desde el vértice que contiene a Iron-Man, Thor y The Winter Soldier;
 

determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número
 

cargue todos los personajes de la tabla anterior
 

indicar qué personajes aparecieron en nueve episodios de la saga
"""