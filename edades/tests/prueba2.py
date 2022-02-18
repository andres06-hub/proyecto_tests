import random
# Lista que guarda los numero generados
list_num = []

for i in range(0, 11):
    n = random.randint(0,100)
    list_num.append(n)
# print(list_num)

# Lista en donde se guarda el indice que se tendra para obtener el valor de la lista
lista_index = []
for i in range(0, 3):
    # obtenemos dos indices para saber cual obtener de la lista
    i = random.randint(0,len(list_num) - 1)
    lista_index.append(i)
# print(lista_index)