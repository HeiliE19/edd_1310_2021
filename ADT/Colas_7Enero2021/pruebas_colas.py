from colas import Queue, BoundedPriorityQueue
q1 = Queue()
q1.enqueue(3)
q1.enqueue(23)
q1.enqueue(33)
print(q1.to_string())

print('Prueba 2 de Queue')
c1 = {'id':1, "nombre":"Mario", "balance": 20.5}
c2 = {'id':2, "nombre":"Diana", "balance": 3456.3}
c3 = {'id':3, "nombre":"Bartolo", "balance": 1000000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())

siguiente = atencion.dequeue()
print(f"Bienvenido Sr/a.,{siguiente['nombre']}, ¿en qué podemos servirle el día de hoy?")
print('\n'+atencion.to_string())

print("Pruebas de las colas con prioridad acotada")
maestres = {"prioridad":4 , "descripcion":"Maestre" , "personas":["juan p" , "diego h"]}
ninos={"prioridad":2 , "descripcion":"Ninos" , "personas":["Santi H" , "Angel h"]}
mecanicos={"prioridad":4 , "descripcion":"Mecanicos" , "personas":["Diana T" , "Maria Z"]}

cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'] , maestres)
cpa.enqueue(ninos['prioridad'] , ninos)
cpa.enqueue(mecanicos['prioridad'] , mecanicos)
cpa.to_string()
sig=cpa.dequeue()
print(sig)
sig=cpa.dequeue()
print(sig)
