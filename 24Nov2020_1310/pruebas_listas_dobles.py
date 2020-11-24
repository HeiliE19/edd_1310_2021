from listas import DoubleLinkedList

ld = DoubleLinkedList()
print('¿Está vacía?: ', ld.is_empty())
ld.append(10)
ld.append(20)
ld.append(30)
print(f'La lista tiene {ld.get_size()}')
ld.transversal()
ld.reverse_transversal()
ld.remove_from_head(20)
ld.transversal()
