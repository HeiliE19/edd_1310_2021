class Array:
    def __init__( self, tam ):
        self.__info = [ 0 for x in range(tam)]

    def get_item (self, posicion):
        dato = 0
        try:
            dato = self.__info[posicion]
        except Exception as e:
            print('Error de posición')
            dato = 'Error'
        return dato

    def set_item( self , dato, posicion ):
        try:
            self.__info[posicion] = dato
        except Exception as e:
            print('Error de posicion')

    def get_lengt(self):
        return len(self.__info)

    def clear(self, dato):
        self.__info = [dato for x in range(len(self.__info)) ]

    def __iter__(self):
        return _IteradorArreglo(self.__info)

class _IteradorArreglo:
    def __init__(self, arr):
        self.__arr = arr
        self.__indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice < len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice += 1
            return dato
        else:
            raise StopIteration
