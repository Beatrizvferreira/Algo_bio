import math

print(f'Diga, respectivamente, a largura e altura de uma parede em metros:')
largura = float(input())
altura = float(input())

area = largura*altura
tinta = math.ceil(area/3)

print(f'A área total a ser pintada é {area}m^2 e serão necessárias {tinta} litros de tinta')

