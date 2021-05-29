lista = []
aux = []

print('Digite o conjunto de números, separado-os por espaço:')
lista.append(input().split(' ')) #vetor


for i in lista: #transformar os elementos do vetor em inteiros
    for j in i:
        print(j)
        aux.append(int(j))

lista.clear() 

for i in range(len(aux)): #pegando os elementos que estão nos índices pares
    if i%2 == 0:
        lista.append(aux[i])

print(lista)

