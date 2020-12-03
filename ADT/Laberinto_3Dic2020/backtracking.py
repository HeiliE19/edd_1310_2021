from Array2D import Array2D
from stack import Stack
class LaberintoADT:
    """
    0 pasillo, 1 pared, S salida y E entrada
    pasillo es una tupla((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
    entrada en una tupla (5,2)
    salida (2,5)
    """
    def __init__(self, rows, cols, pasillos, entrada, salida):
        self.__laberinto = Array2D(rows, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0], pasillo[1], '0')
        self.set_entrada(entrada[0], entrada[1])
        self.set_salida(salida[0], salida[1])   #Coordenadas
        self.__camino = Stack()
        self.__previa = None

    def to_string(self):
        self.__laberinto.to_string()

    """
    Establece la entrada 'E' en la matriz, verificar límites
    """
    def set_entrada(self, row, col):
        #Terminar la validación de las coordenadas
        self.__laberinto.set_item(row,col,'E')

    """
    Establecer salida dentro de los límites periféricos de la matriz
    """
    def set_salida(self, row, col):
        #Terminar las validaciones
        self.__laberinto.set_item(row, col, 'S')

    def es_salida(self, row, col):
        return self.__laberinto.get_item(ren,col) == 'S'

    def buscar_entrada(self):
        encontrado = False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberito.get_num_cols()):
                if self.__laberito.get_item(renglon, columna) == 'E':   #si el tope es la entrada
                    self.__camino.push(tuple(renglon,columna))
                    encontrado = True
        return encontrado

    def set_previa(self, pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def resolver_laberinto(self):
        #Aplicar reglas
