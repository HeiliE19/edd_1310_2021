class Nodo:
    def __init__(self, value, siguiente = None):
        self.data = value  # falta encapsulamiento
        self.siguiente = siguiente

class LinkedList:
    def __init__(self):
        self.__head = None #iniciamos la lista vacía, head apunta a nada

    def is_empty(self):
        return self.__head == None #Evaluación booleana si se cumple, el nodo está vacío, es decir, head está apuntando a none/vacío/null

    def append(self, value):    #agrega un nodo al final
        nuevo = Nodo(value)
        if self.__head == None: # es equivalente a self._empty()
            self.__head = nuevo
        else:
            curr_node = self.__head #apunta a la cabeza(head)
            while curr_node.siguiente != None: #mientras curr_node en su posición siguiente sea diferente de None (vacío) #Mientras head apunte a un dato
                curr_node = curr_node.siguiente  #entonces curr_node es igual a curr_node.siguiente es decir el nodo siguiente de head
            curr_node.siguiente = nuevo

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f'{curr_node.data} --> ', end='')  #end='' para que no salte la linea
            curr_node = curr_node.siguiente   #curr_node apunta al nodo completo que sigue
        print('')

    def remove(self, value):  #value es el valor que queremos eliminar  #remove, elimina la primer coincidencia del dato solicitado
        curr_node = self.__head #Hace una copia del dato al que apunta head
        if self.__head.data == value:   #si la cabeza, es decir, el primer dato, es igual al valor buscado...
            self.__head = self.__head.siguiente    #apuntamos head al siguiente dato
        else:
            anterior = None     #creamos la variable anterior (al dato que buscamos)
            while curr_node.data != value and curr_node.siguiente != None:   #que no es el dato que buscamos ni el último
                anterior = curr_node
                curr_node = curr_node.siguiente #SI se cumplen ambas condiciones va al siguiente valor para encontrar el dato buscado
            if curr_node.data == value:     #si curr_node es igual al valor que queremos
                anterior.siguiente = curr_node.siguiente
            else:
                print('El dato no existe en la lista')

    def preppend(self, value):  #agrega un valor al principio de toda la lista
        nuevo = Nodo(value, self.__head)    #Hacemos que nuevo apunte a donde está apuntando head
        self.__head = nuevo

    def tail(self):#Regresa el ultimo nodo.
        curr_node = self.__head
        while curr_node.siguiente != None:  #Garantiza que te quedas en el ultimo nodo            curr_node = curr_node.siguiente
            curr_node = curr_node.siguiente
        return curr_node

    def get(self, posicion  = None): #Por defecto regresa el último, poniendo "posicion" seleccionas cual necesitas
        curr_node = self.__head
        contador = 0
        dato = None
        if posicion == None:    #si la posicion está vacía, quiere decir que quiero el último elemento
            dato = self.tail().data   #Obtiene ultimo dato
        else:
            while curr_node != None:    #mientras que el apuntador no sea vacío
                curr_node = curr_node.siguiente     #curr_node apunta al siguiente nodo
                contador += 1                       #aumenta el contador al recorrer la lista
                if (posicion == contador):          #si la posicion coincide con el contador
                    dato = curr_node.data           #el valor del dato es igual al dato al que apunta curr_node

        return dato

class NodoDoble:
    def __init__(self, value, anterior = None, siguiente = None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble(None)
        self.__tail = NodoDoble(None)
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def append(self, value):
        if self.is_empty():
            nuevo = NodoDoble(value)
            self.__head = nuevo
            self.__tail = nuevo
        else:
            nuevo = NodoDoble(value, self.__tail, None)
            self.__tail.next = nuevo
            self.__tail = nuevo
        self.__size += 1

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f'{curr_node.data} <-->', end='')
            curr_node = curr_node.next
        print('')

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f'{curr_node.data} <-->', end='')
            curr_node = curr_node.prev
        print('')

    def remove_from_head(self, value):
        curr_node = self.__head
        while curr_node.data != value and curr_node != None:
            curr_node = curr_node.next
        if curr_node.data == value:
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        curr_node.next = None
        curr_node.prev = None
        self.__size -= 1
