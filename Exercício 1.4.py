import math

print(f'Quantos cigarros você fuma por dia e por quantos anos?')
qnt, anos = input().split(' ')
qnt = int(qnt)
anos = int(anos)
vida_perdida = qnt*10*30*365 #Quantidade de cigarros fumados em um anos
vida_perdida *= anos #Quantidade de cigarros fumado em n anos

dias = math.floor(vida_perdida/1440)

print(f'Você perdeu {dias} dias de vida')



