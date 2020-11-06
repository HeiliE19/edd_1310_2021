from arrays import Array
from trabajador import Trabajador

class Pruebas:
    arch = open('junio.dat', 'rt')
    for lineas in arch.readlines():
        listas = lineas.strip('\n').split(',')
        listas = Array(15)
