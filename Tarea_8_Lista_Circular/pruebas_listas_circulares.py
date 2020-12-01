from Listas_Circulares import CircularList
cl = CircularList()
print(f'¿La lista está vacía? {cl.is_empty()}')
cl.insert(8)
cl.insert(8)
cl.insert(3)
cl.insert(5)
cl.insert(6)
cl.insert(9)
cl.insert(49)

cl.transversal()

print(f'¿Existe el dato en la lista?  {cl.search(8)}' )
print(f'¿Existe el dato en la lista?  {cl.search(3)}' )
print(f'¿Existe el dato en la lista?  {cl.search(5)}' )
print(f'¿Existe el dato en la lista?  {cl.search(7)}' )
print(f'¿La lista está vacía? {cl.is_empty()}')

cl.transversal()

cl.remove(8)
cl.remove(49)
cl.remove(3)
cl.remove(5)

cl.transversal()
