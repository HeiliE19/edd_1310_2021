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
        self.__laberinto = Array2D(rows, cols, '1') #Todo con paredes
        for pasillo in pasillos:    #recorremos laberinto
            self.__laberinto.set_item(pasillo[0], pasillo[1], '0')  #agregamos los pasillos
        self.set_entrada(entrada[0], entrada[1])
        self.set_salida(salida[0], salida[1])   #Coordenadas
        self.__camino = Stack()
        self.__previa = None    #guardará la posición previa

    def to_string(self):        #imprime laberinto
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
        return self.__laberinto.get_item(row,col) == 'S'    #pregunta si es la salida

    def buscar_entrada(self):
        encontrado = False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(renglon, columna) == 'E':   #si el tope es la entrada
                    self.__camino.push((renglon,columna))
                    encontrado = True
        return encontrado

    def set_previa(self, pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def imprimir_camino(self):
        self.__camino.to_string()

    def get_pos_actual(self):
        return self.__camino.peek() #5,2

    def resolver_laberinto(self):
        actual = self.__camino.peek()
        #buscar a la izquierda          pos actual: 5,2
        #agregar validaciones para los límites del Laberinto
        if actual[1]-1 != -1 \
        and self.__laberinto.get_item(actual[0], actual[1]-1) == '0' \
        and self.get_previa() != (actual[0],actual[1]-1) \
        and self.__laberinto.get_item(actual[0],actual[1]-1) != 'X':
            self.set_previa(actual)
            self.__camino.push((actual[0], actual[1]-1))
        #Buscar arriba
        elif actual[0]-1 != -1 \
        and self.__laberinto.get_item(actual[0]-1, actual[1]) == '0' \
        and self.get_previa() != (actual[0]-1,actual[1]) \
        and self.__laberinto.get_item(actual[0]-1,actual[1]) != 'X':
            self.set_previa(actual)
            self.__camino.push((actual[0]-1, actual[1]))
        #Buscar a la derecha
        elif actual[1]+1 != -1 \
        and self.__laberinto.get_item(actual[0], actual[1]+1) == '0' \
        and self.get_previa() != (actual[0],actual[1]+1) \
        and self.__laberinto.get_item(actual[0],actual[1]+1) != 'X':
            self.set_previa(actual)
            self.__camino.push((actual[0], actual[1]+1))
        #Buscar abajo
        elif actual[0]+1 != -1 \
        and self.__laberinto.get_item(actual[0]+1, actual[1]) == '0' \
        and self.get_previa() != (actual[0]+1,actual[1]) \
        and self.__laberinto.get_item(actual[0]+1,actual[1]) != 'X':
            self.set_previa(actual)
            self.__camino.push((actual[0]+1, actual[1]))
        #La posición actual es un camino cerrado
        else:
            self.__laberinto.set_item(actual[0],actual[1], 'X')
            self.__previa = actual
            self.__camino.pop()
