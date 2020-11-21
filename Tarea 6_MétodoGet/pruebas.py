from listas import LinkedList
l = LinkedList()
print(f'¿L está vacía? { l.is_empty()}') #Pregunts si la lista está vacía
l.append(10)
l.append(5)
l.append(6)
l.append(20)
print(f'¿L está vacía? { l.is_empty()}')
l.transversal() #nos dice que el programa no etá vacío
l.remove(10)
l.transversal()
l.preppend(3)
l.transversal()
x = l.tail()
print(x.data)   #imprimir el dato que está en x, o sea dato "tail"(cola)
print(l.get(2))
