print('Quantos dias?')
dias = int(input())
print('Quantas horas?')
horas = int(input())
print('Quantos minutos?')
minutos = int(input())
print('Quantos segundos?')
segundos = int(input())

soma = segundos + 60*minutos + 60*(60*horas) + 60*60*24*dias

print(f'O total em segundos é {soma}')