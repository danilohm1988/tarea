class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        return nodo

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        return self._buscar(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._min_value_node(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar(nodo.derecha, temp.valor)
        return nodo

    def _min_value_node(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def recorrido_en_orden(self):
        self._recorrido_en_orden(self.raiz)
        print()

    def _recorrido_en_orden(self, nodo):
        if nodo:
            self._recorrido_en_orden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._recorrido_en_orden(nodo.derecha)

    def calcular_altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._calcular_altura(nodo.izquierda), self._calcular_altura(nodo.derecha))
