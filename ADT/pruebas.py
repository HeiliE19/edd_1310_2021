from arrays import Array

algo = Array(10)
print(algo.get_item(6363))
algo.set_item(555,3)
print(algo.get_item(3))
print(f"El arreglo tiene {algo.get_lengt()} elementos")
algo.clear(777)
print(algo.get_item(3))
print('---------------')
for x in algo:
    print(x)
