import math
import numpy as np
import random

matrix = []
matrixaux = []

#Criando a matriz com números inteiros aleatórios de -10 a 65
matrix = np.random.randint(-10,65,size = (4,5))

print('A matriz gerada é: ')
for i in matrix:
    print(i)
print('\n')



#a) Valor absoluto dos elementos da matriz
for i in range(4):
    aux = []
    for j in range(5):
        aux.append(abs(matrix[i][j]))   
    matrixaux.append(aux)

print('O valor absoluto dos elementos dessa matriz é: ')
for i in matrixaux:
    print(i)
print('\n')




#b) Seno dos valores da primeira linha
print('O seno dos valores contidos na primeira linha dessa matriz é:')
aux.clear() 
for i in range(5):
  num = round(math.sin(matrix[0][i]),4)
  aux.append(num)
print(f'{aux}\n')




#c) Valor máximo das colunas
aux.clear()
print('O valor máximo das colunas da matriz é') 
for j in range(5):
    maior = int(matrix[0][j])
    for i in range(4):
        if (int(matrix[i][j]) > maior):
            maior = matrix[i][j]
            maior = int(maior)
    aux.append(maior)
print(f'{aux}\n')




#d) A soma dos elementos em cada coluna da matriz
aux.clear()
print('A soma dos elementos em cada coluna é:')
for j in range(5):
    soma=0
    for i in range(4):
        soma += matrix[i][j]
    aux.append(soma)
print(f'{aux}\n')




#e) A soma dos elementos em cada linha da matriz
aux.clear()
print('A soma dos elementos em cada linha é:')
for i in range(4):
    soma=0
    for j in range(5):
        soma += matrix[i][j]
    aux.append(soma)
print(f'{aux}\n')




#f) Calcule o produto entre os elementos de cada coluna
print('O produto entre os elementos de cada coluna é:')
aux.clear()
for j in range(5):
    produto =1
    for i in range(4):
        produto *= matrix[i][j]
    aux.append(produto)
print(f'{aux}\n')