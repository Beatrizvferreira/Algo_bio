def maxnum(*numeros):
  maior = numeros[0]
  for i in numeros:
    if maior < i:
      maior = i
  return maior


lista = {9,2,4,1,6,2,5}
print(f'O maior elemento é {maxnum(*lista)}')