import random
import math

matrix = []
matrixaux = []

for i in range(4):
  aux = []
  for j in range(5):
    valor = random.randint(-10,65)
    aux.append(valor)
  matrix.append(aux)
'''
for item in matrix:
    matrixaux.append(item)
'''

matrixaux = matrix[:]
print('A matriz gerada é: ')
print(matrix)

#a) Valor absoluto dos elementos da matriz
for i in range(4): 
    for j in range(5):
        matrixaux[i][j] = abs(matrixaux[i][j])     

print('O valor absoluto dos elementos dessa matriz é: ')
print(matrixaux)
#b) Seno dos valores
print('O seno dos valores contidos na primeira linha dessa matriz é:')
aux.clear() 
for i in range(5):
  aux.append(math.sin(matrix[1][i]))
print(aux)

#c) Valor máximo das colunas
aux.clear()
print('O valor máximo das colunas da matriz é') 
for j in range(5):
    maior = int(matrix[0][j])
    for i in range(3):
        if (int(matrix[i][j]) > maior):
            maior = matrix[i][j]
            maior = int(maior)
    aux.append(maior)

print(aux)



#d) A soma dos elementos em cada coluna da matriz
aux.clear()
print('A soma dos elementos em cada coluna é:')
for j in range(5):
    soma=0
    for i in range(3):
        soma += matrix[i][j]
    aux.append(soma)
print(aux)




#e) A soma dos elementos em cada linha da matriz
aux.clear()
print('A soma dos elementos em cada linha é:')
for i in range(3):
    soma=0
    for j in range(5):
        soma += matrix[i][j]
    aux.append(soma)
print(aux)



#f) Calcule o produto entre os elementos de cada coluna
print('O produto entre os elementos de cada coluna é:')
aux.clear()
for j in range(4):
    produto =1
    for i in range(3):
        produto *= matrix[i][j]
    aux.append(produto)
print(aux)




