class Usuario:

    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password

    def __str__(self):
        pass

class NodoLista:

    def __init__(self, usuario):
        self.siguiente = None
        self.anterior = None
        self.usuario = usuario

class ListaDoble:

    raiz = NodoLista(None)

    def __init__(self):
        self.raiz = None

    def esta_vacia(self):
        if self.raiz.usuario is None:
            return True
        else:
            return False

    def agrega_Lista(self, nombre, password):
        # Añadiendo nuevo usuario a la Lista
        nuevo_us = Usuario(nombre, password)
        nuevo_nodo = NodoLista(nuevo_us)
        # Si la lista esta vacía lo inserta en la raíz
        if self.esta_vacia() is True:
            try:
                self.raiz = nuevo_nodo
            except Exception as ex:
                print("Error al Empezar a llenar la Lista: raiz: "+ ex)
        else:
            # de lo contrario recorre la lista para insertarlo al final
            aux = self.raiz
            while aux.siguiente is not self.raiz:
                try:
                    aux = aux.siguiente
                except Exception as inst:
                    print("Error al recorrer la lista: "+inst)
            try:
                aux.siguiente = nuevo_nodo
                nuevo_nodo.anterior = aux
            except Exception as inst:
                print("error al recorrer al insertar en Lista "+inst)
    
    def imprimir_lista(self):
        aux = self.raiz
        print("---------Inicio de Lista---------")
        while aux.siguiente is not None:
            print("Usuario: "+ aux.usuario.nombre)
            aux = aux.siguiente
        print("---------Fin de Lista-----------")