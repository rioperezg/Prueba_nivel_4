# PILAS
class nodoPila(object):
    info, sig = None, None
class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamaño = 0
    def apilar(pila, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.tamaño += 1
    def desapilar(pila):
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamaño -= 1
        return x
    def pila_vacia(pila):
        return pila.cima is None
    def Tamaño(pila):
        return pila.tamaño

# MONTICULO
class Heap(object):
    def __init__(self, tamaño):
        self.tamaño = 0
        self.vector = [None] * tamaño
    def intercambio(vector, indice1, indice2):
        aux = vector[indice1]
        vector[indice1] = vector[indice2]
        vector[indice2] = aux
    def heap_vacio(heap):
        return heap.tamaño == 0
    def flotar(heap, indice):
        while(indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]):
            padre = (indice - 1) // 2
            Heap.intercambio(heap.vector, indice, padre)
            indice = padre
    def hundir(heap, indice):
        hijo_izq = (indice * 2) + 1
        control = True
        while(control and hijo_izq < heap.tamaño):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < heap.tamaño):
                if(heap.vector[hijo_der] > heap.vector[hijo_izq]):
                    aux = hijo_der
            if(heap.vector[indice] < heap.vector[aux]):
                Heap.intercambio(heap.vector, indice, aux)
                indice = aux
                hijo_izq = (indice * 2) + 1
            else:
                control = False
    def buscar_H(heap, buscado):
        pos = -1
        for i in range(heap.tamaño):
            if(heap.vector[i][1] == buscado):
                pos = i
        return pos

    def agregar(heap, dato):
        heap.vector[heap.tamaño] = dato
        Heap.flotar(heap, heap.tamaño)
        heap.tamaño += 1
    def Quitar(heap):
        Heap.intercambio(heap.vector, 0, heap.tamaño - 1)
        dato = heap.vector[heap.tamaño - 1]
        heap.tamaño -= 1
        Heap.hundir(heap, 0)
        return dato
    def arrib_H(heap, dato, prioridad):
        Heap.agregar(heap, [prioridad, dato])
    def atencion_H(heap):
        return Heap.Quitar(heap)[1]

    def cambiar_prioridad(heap, indice, prioridad):
        prioridad_anterior = heap[indice][0]
        heap[indice][0] = prioridad
        if(prioridad > prioridad_anterior):
            Heap.flotar(heap, indice)
        elif(prioridad < prioridad_anterior):
            Heap.hundir(heap, indice)

# COLAS
class nodoCola(object):
    info, sig = None, None
class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamaño = 0
    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamaño += 1
    def atencion(cola, dato):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
            cola.tamaño -= 1
            return dato
    def cola_vacia(cola):
        return cola.frente is None

# GRAFOS
class Grafo(object):
    def __init__(self, dirigido = True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamaño = 0
class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0
    def buscar_vertice(grafo, buscado):
        aux = grafo.inicio
        while(aux is not None and aux.info != buscado):
            aux = aux.sig
        return aux
    def barrido_profundo(grafo, vertice):
        while(vertice is not None):
            if(not vertice.visitado):
                vertice.visitado = True
                print(vertice.info)
                adyacentes = vertice.adyacentes.inicio
                while(adyacentes is not None):
                    adyacente = Arista.buscar_vertice(grafo, adyacentes.destino)
                    if(not adyacente.visitado):
                        Arista.barrido_profundo(grafo, adyacente)
                    adyacentes = adyacentes.sig
            vertice = vertice.sig
    def barrido_amplitud(grafo, vertice):
        cola = Cola()
        while(vertice is not None):
            if(not vertice.visitado):
                vertice.visitado = True
                Cola.arribo(cola, vertice)
                while(not Cola.cola_vacia(cola)):
                    nodo = Cola.atencion(cola)
                    print(nodo.info)
                    adyacentes = nodo.adyacentes.inicio
                    while(adyacentes is not None):
                        adyacente = Arista.buscar_vertice(grafo, adyacentes.destino)
                        if(not adyacente.visitado):
                            adyacente.visitado = True
                            Cola.arribo(cola, adyacente)
                        adyacentes = adyacentes.sig
            vertice = vertice.sig

    def existe_paso(grafo, origen, destino):
        resultado = False
        if(not origen.visitado):
            origen.visitado = True
            vadyacentes = origen.adyacentes.inicio
            while(vadyacentes is not None and not resultado):
                adyacente = Grafo.buscar_vertice(grafo, vadyacentes.destino)
                if(adyacente.info == destino.info):
                    resultado = True
                elif(not adyacente.visitado):
                    resultado = Grafo.existe_paso(grafo, adyacente, destino)
                vadyacentes = vadyacentes.sig
        return resultado
    def marcar_no_visitado(grafo):
        aux = grafo.inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.sig


def dijkstra(grafo, origen, destino):
    no_visitados = Heap(Pila.Tamaño(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            Heap.arrib_H(no_visitados, [aux, None], 0)
        else:
            Heap.arrib_H(no_visitados, [aux, None], inf)
        aux = aux.sig
    while(not Heap.heap_vacio(no_visitados)):
        dato = Heap.atencion_H(no_visitados)
        Pila.apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = Heap.buscar_H(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0]>dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                Heap.cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino
