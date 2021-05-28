lista = [1,2,3,4,5,6,7,8]
aux = []

for i in range(len(lista)):
    if i == 0:
        aux.append(lista[i])
    elif i%2 == 0:
        aux.append(lista[i])

print(aux)