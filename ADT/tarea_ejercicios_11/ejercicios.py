from stack import Stack
"""Ejercicio 1: Crear una lista de enteros en Python y realizar la suma con recursividad, el
caso base es cuando la lista este vacia."""
def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0] #Regresa el valor que está en lista, en el elemento 0
    else:
        return lista.pop() + suma_lista_rec(lista)
"""Ejercicio 2: Hacer un contador regresivo con recursión."""
def contadorReg(num):
    if num > 0:
        print(num)
        contadorReg(num - 1)
    elif num == 0:
        print(num)
        print("El conteo ha terminado")
    else:
        print('Introduce un número positivo')

"""Ejercicio 3: Sacar de un ADT pila el valor en la posición media."""
"""Incompleto"""
def pos_media(pila):
    pila = Stack()
    m = (pila.length() / 2)
    if type(m/2) != float:
        return m/2
    else:
        return int((m/2)+0.5)
"""Incompleto"""

def main():
    datos = [4,2,3,5]  #14
    res = suma_lista_rec(datos)
    print(res)
main()

def main2():
    print('\nCuenta regresiva')
    cont = contadorReg(10)
    print(cont)
main2()


def main3():
    pila = Stack(8)
    pila.push(10)
    pila.push(8)
    pila.push(6)
    pila.push(4)
    pila.push(2)
    pila.pos_media()
