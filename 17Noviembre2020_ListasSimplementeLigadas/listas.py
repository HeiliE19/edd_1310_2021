class Nodo:
    def __init__(self, value, siguiente = None):
        self.data = value  # falta encapsulamiento
        self.siguiente = siguiente

class LinkedList:
    def __init__(self):
        self.__head = None #iniciamos la lista vacía, head apunta a nada

    def is_empty(self):
        return self.__head == None #Evaluación booleana si se cumple, el nodo está vacío, es decir, head está apuntando a none/vacío/null

    def append(self, value):
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

    def remove(self, value):  #value es el valor que queremos eliminar
        curr_node = self.__head #apuntamos a lo que apunta head
        while curr_node != value and curr_node.siguiente != None:   #validar que te mueves al dato que quieres eliminar y que el dato exista
            curr_node = curr_node.siguiente
        if curr_node.data == value:
            #EJERCICIO: hacer variable que almacene el nodo anterior a curr_node (6)
