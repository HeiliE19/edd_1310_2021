from arboles_binarios import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)


abb.transversal('inorden')
abb.transversal('preorden')
abb.transversal('posorden')

res = abb.search(35)
print(f'\nEl resultado es {res} \n')

res2 = abb.search(55)
print(f'\nEl resultado es {res2} \n')

abb.remove(35)
abb.transversal()
