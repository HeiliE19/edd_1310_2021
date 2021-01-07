from colas import Queue
class BoundedPriorityQueue:
    def __init__(self , niveles ):
        self.__data = [Queue() for x in range(niveles)]
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def len( self ):
        return self.__size

    def enqueue(self , prioridad , elem):
        if  prioridad < len(self.__data) and prioridad >= 0:
            self.__data[prioridad].enqueue(elem)
            self.__size += 1

    def dequeue(self):
        if not self.is_empty():
            for nivel in self.__data:
                if not nivel.is_empty():
                    self.__size-=1
                    return nivel.dequeue()
        else:
            print('No existe nadie en la cola')

    def to_string(self):
        print("\n\nCola de evacuación:")
        if not self.is_empty():
            for nivel in range(len(self.__data)):
                print(f"Nivel {nivel} --> {self.__data[nivel].to_string()}")
        else:
            print("El barco ya ha sido evacuado por completo")
