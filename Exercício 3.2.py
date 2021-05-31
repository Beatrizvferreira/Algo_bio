def maxnum(*numeros):
  maior = numeros[0]
  for i in numeros:
    if maior < i:
      maior = i
  return maior

numeros = input('Digite os números separados por espaço:\n')
conjunto = []

for i in numeros.split():
  conjunto.append(float(i))

print(conjunto)

print(f'O maior elemento é {maxnum(*conjunto)}')