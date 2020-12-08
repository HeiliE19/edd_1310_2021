from backtracking import LaberintoADT
import time
pasillos_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
entrada = (5,2)
salida = (2,5)
lab = LaberintoADT(6, 6, pasillos_inicial, entrada, salida)
lab.buscar_entrada()

lab.to_string()
#imprimir la pila
lab.imprimir_camino()

while not lab.es_salida(lab.get_pos_actual()[0], lab.get_pos_actual()[1]):
    print('probar')
    lab.resolver_laberinto()
    lab.imprimir_camino()
    time.sleep(1.0)
