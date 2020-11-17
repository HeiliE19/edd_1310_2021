from listas import LinkedList
l = LinkedList()
print(f'¿L está vacía? { l.is_empty()}') #Pregunts si la lista está vacía
l.append(10)
l.append(5)
l.append(6)
l.append(20)
print(f'¿L está vacía? { l.is_empty()}')
l.transversal()
