import tkinter as tk
from tkinter import messagebox

# === Nodo AVL ===
class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1

# === Árbol AVL ===
class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        else:
            return nodo  # duplicado no insertado

        nodo.altura = 1 + max(self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha))
        return self._balancear(nodo)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if not nodo:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            temp = self._min_value_node(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar(nodo.derecha, temp.valor)

        nodo.altura = 1 + max(self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha))
        return self._balancear(nodo)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        return self._buscar(nodo.derecha, valor)

    def _balancear(self, nodo):
        balance = self._get_balance(nodo)
        if balance > 1:
            if self._get_balance(nodo.izquierda) < 0:
                nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
            return self._rotar_derecha(nodo)
        if balance < -1:
            if self._get_balance(nodo.derecha) > 0:
                nodo.derecha = self._rotar_derecha(nodo.derecha)
            return self._rotar_izquierda(nodo)
        return nodo

    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self._get_altura(y.izquierda), self._get_altura(y.derecha))
        x.altura = 1 + max(self._get_altura(x.izquierda), self._get_altura(x.derecha))
        return x

    def _rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        x.altura = 1 + max(self._get_altura(x.izquierda), self._get_altura(x.derecha))
        y.altura = 1 + max(self._get_altura(y.izquierda), self._get_altura(y.derecha))
        return y

    def _get_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_altura(nodo.izquierda) - self._get_altura(nodo.derecha)

    def _min_value_node(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    def recorrido_en_orden(self):
        valores = []
        self._recorrido_en_orden(self.raiz, valores)
        return valores

    def _recorrido_en_orden(self, nodo, valores):
        if nodo:
            self._recorrido_en_orden(nodo.izquierda, valores)
            valores.append(nodo.valor)
            self._recorrido_en_orden(nodo.derecha, valores)

    def calcular_altura(self):
        return self._get_altura(self.raiz) - 1

# === Interfaz Tkinter para AVL ===
class AppAVL:
    def __init__(self, root):
        self.arbol = ArbolAVL()

        root.title("Árbol AVL - Interfaz")
        root.geometry("400x300")

        self.entrada = tk.Entry(root)
        self.entrada.pack(pady=5)

        tk.Button(root, text="Insertar", command=self.insertar).pack()
        tk.Button(root, text="Buscar", command=self.buscar).pack()
        tk.Button(root, text="Eliminar", command=self.eliminar).pack()
        tk.Button(root, text="Recorrido en Orden", command=self.mostrar_recorrido).pack()
        tk.Button(root, text="Calcular Altura", command=self.mostrar_altura).pack()

        self.resultado = tk.Label(root, text="", wraplength=380)
        self.resultado.pack(pady=10)

    def insertar(self):
        try:
            valor = int(self.entrada.get())
            self.arbol.insertar(valor)
            self.resultado.config(text=f"Insertado {valor}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")

    def buscar(self):
        try:
            valor = int(self.entrada.get())
            encontrado = self.arbol.buscar(valor)
            if encontrado:
                self.resultado.config(text=f"{valor} encontrado")
            else:
                self.resultado.config(text=f"{valor} NO encontrado")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")

    def eliminar(self):
        try:
            valor = int(self.entrada.get())
            self.arbol.eliminar(valor)
            self.resultado.config(text=f"Eliminado {valor} (si existía)")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")

    def mostrar_recorrido(self):
        recorrido = self.arbol.recorrido_en_orden()
        self.resultado.config(text=f"En orden: {' '.join(map(str, recorrido))}")

    def mostrar_altura(self):
        altura = self.arbol.calcular_altura()
        self.resultado.config(text=f"Altura del árbol: {altura}")

# === Ejecutar ===
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppAVL(ventana)
    ventana.mainloop()
