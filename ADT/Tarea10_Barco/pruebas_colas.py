from colas_prioridad_acotada import BoundedPriorityQueue

print("\nPruebas de las colas con prioridad acotada")
print("Bienvenido al barco")
maestres = {"prioridad":4 , "descripcion":"Maestre" , "personas":["Juan P" , "Diego H"]}
ninos={"prioridad":2 , "descripcion":"Ninos" , "personas":["Santi H" , "Angel H"]}
mecanicos={"prioridad":4 , "descripcion":"Mecanicos" , "personas":["Diana T" , "Maria Z"]}
mujeres={"prioridad":3 , "descripcion":"Mujeres" , "personas":["Santi H" , "Angel h"]}
tera_edad={"prioridad":2 , "descripcion":"Tercera Edad" , "personas":["Pedro V" , "Carmen T"]}
ninas={"prioridad":1 , "descripcion":"Ninas" , "personas":["Itzel R" , "Romina D"]}
hombres={"prioridad":3 , "descripcion":"Hombres" , "personas":["Daniel M" , "Sebastian A"]}
vigia={"prioridad":4 , "descripcion":"Vigia" , "personas":["Ruben S"]}
capitan={"prioridad":5 , "descripcion":"Capitan" , "personas":["Samantha E"]}
timonel={"prioridad":4 , "descripcion":"Timonel" , "personas":["Rosa B" , "Raul A"]}

cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'] , maestres)
cpa.enqueue(ninos['prioridad'] , ninos)
cpa.enqueue(mecanicos['prioridad'] , mecanicos)
cpa.enqueue(tera_edad['prioridad'] , tera_edad)
cpa.enqueue(ninas['prioridad'] , ninas)
cpa.enqueue(hombres['prioridad'] , hombres)
cpa.enqueue(vigia['prioridad'] , vigia)
cpa.enqueue(capitan['prioridad'] , capitan)
cpa.enqueue(timonel['prioridad'] , timonel)
cpa.to_string()

sig = cpa.dequeue()
print(sig)
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
cpa.dequeue()
cpa.to_string()
