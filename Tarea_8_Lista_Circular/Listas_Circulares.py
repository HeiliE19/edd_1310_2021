class Nodo:
    def __init__(self, value, next = None):
        self.data = value  # falta encapsulamiento
        self.next = next

class CircularList:
    def __init__(self):
        self.__ref = None

    def is_empty(self):
        return self.__ref == None

    def insert(self, value):
        new = Nodo(value)
        if self.is_empty():
            self.__ref = new
            self.__ref.next = self.__ref
        elif self.search(value) == False:
            if value < self.__ref.next.data:
                new = Nodo(value, self.__ref.next)
                self.__ref.next = new
            elif value > self.__ref.data:
                new = Nodo(value, self.__ref.next)
                self.__ref.next = new
                self.__ref = self.__ref.next
            else:
                curr_node = self.__ref
                while value > curr_node.next.data:
                    curr_node = curr_node.next
                new = Nodo(value, curr_node.next)
                curr_node.next = new
        else:
            print(f'El valor {value} ya existe en la lista')

    def search(self, value):
        curr_node = self.__ref
        while curr_node.next.data != value and curr_node.next.data != self.__ref.data:
            curr_node = curr_node.next
        if curr_node.next.data == value:
            return True
        else:
            return False

    def transversal( self ):
        curr_node = self.__ref
        while curr_node.next != self.__ref:
            print(f"{curr_node.data} --> ", end="")
            curr_node = curr_node.next
        print(f"{curr_node.data} --> ", end="")
        print("")


    def remove(self, value):  #value es el valor que queremos eliminar  #remove, elimina la primer coincidencia del dato solicitado
        curr_node = self.__ref #Hace una copia del dato al que apunta ref
        if self.__ref.data == value:   #si la referencia, es decir, el dato más alto, es igual al valor buscado...
            self.__ref = self.__ref.next        #apuntamos head al siguiente dato
        else:
            anterior = None     #creamos la variable anterior (al dato que buscamos)
            while curr_node.data != value:   #que no es el dato que buscamos ni el último
                anterior = curr_node
                curr_node = curr_node.next      #SI se cumplen ambas condiciones va al siguiente valor para encontrar el dato buscado
            if curr_node.data == value:         #si curr_node es igual al valor que queremos
                anterior.next = curr_node.next
            else:
                print('El dato no existe en la lista')
