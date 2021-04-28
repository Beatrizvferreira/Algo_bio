print(f'Diga, respectivamente, a largura e altura de uma parede em metros:')
largura = float(input())
altura = float(input())

area = largura*altura
tinta = area/3

print(f'A área total a ser pintada é {area}m^2 e serão necessárias {tinta:.2f} litros de tinta')

