class DobleNodo:
    def __init__(self, value, siguiente = None, anterior = None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = DobleNodo(None, None, None)
        self.__tail = DobleNodo(None, None, None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0
        print(f'head: {self.__head}')
        print(f'tail: {self.__tail}')

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__head.data == None and self.__tail.data == None

    #agrega un nodo al final
    def append(self, value):
        self.__size+=1
        new_node = DobleNodo(value)
        if self.is_empty():
            self.__head = new_node
            self.__tail = self.__head
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            new = DobleNodo(value = value, anterior = curr_node)
            curr_node.next = new
            self.__tail = new

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -->", end = "")
            curr_node = curr_node.next
        print(" ")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f"{curr_node.data} -->", end = "")
            curr_node = curr_node.prev
        print(" ")


    def remove_from_head(self, value):  #value es el valor que queremos eliminar  #remove, elimina la primer coincidencia del dato solicitado
        if self.__head.data == value:   #si la cabeza, es decir, el primer dato, es igual al valor buscado...
            self.__head = self.__head.siguiente    #apuntamos head al siguiente dato
            self.__head.next = None
        else:
            curr_node = self.__head     #creamos la variable anterior (al dato que buscamos)
            while curr_node.data != value and curr_node.next != None:   #que no es el dato que buscamos ni el último
                curr_node = curr_node.next #SI se cumplen ambas condiciones va al siguiente valor para encontrar el dato buscado
            if curr_node.data == value:     #si curr_node es igual al valor que queremos
                curr_node.prev.next = curr_node
                curr_node.next.prev = curr_node.prev
            else:
                self.__size += 1
                print('El dato no existe en la lista')
        self.__size -=1



    def remove_from_tail(self, value):  #value es el valor que queremos eliminar  #remove, elimina la primer coincidencia del dato solicitado
        if self.__tail.data == value:   #si la cola, es decir, el último dato, es igual al valor buscado...
            self.__tail = self.__tail.prev    #apuntamos tail al  datoanterior
            self.__tail.next = None
        else:
            curr_node = self.__tail
            while curr_node.data != value and curr_node.prev != None:   #que no es el dato que buscamos ni el último
                curr_node = curr_node.prev  #SI se cumplen ambas condiciones va al valor anterior para encontrar el dato buscado
            if curr_node.data == value:     #si curr_node es igual al valor que queremos
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else:
                self.__size += 1
                print('El dato no existe en la lista')
        self.__size -=1


    def find_from_tail(self, value):
        curr_node = self.__head     #Ponemos apuntador a la cabeza
        find = None
        try:
            while curr_node.data != value:      #Mientras el apuntador sea diferente al valor  que queremos
                curr_node = curr_node.next      #Apuntamos al siguiente nodo
            if curr_node.data == value:     #Si el apuntador encontró el nodo buscado
                find = curr_node.data     #encontramos el dato
        except:                                            #Lanzamos excepción
            print("El valor no se encuentra en la lista")
        return find

    def find_from_head(self, value):
        curr_node = self.__head     #Ponemos apuntador a la cabeza
        find = None
        try:
            while curr_node.data != value:      #Mientras el apuntador sea diferente al valor  que queremos
                curr_node = curr_node.next      #Apuntamos al siguiente nodo
            if curr_node.data == value:     #Si el apuntador encontró el nodo buscado
                find = curr_node.data     #encontramos el dato
        except:
            print("El valor no se encuentra en la lista")
        return find
