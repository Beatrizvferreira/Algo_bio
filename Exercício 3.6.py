import numpy as np

lista = []
aux = []

n= int(input('Digite a quantidade de números que deseja na sua lista:'))

lista = np.random.randint(-n,n,size=n) #vetor
print(lista)

for keys in range(n): #pegando os elementos que estão nos índices pares
    if keys%2 == 0:
        aux.append(lista[keys])
