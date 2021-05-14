print('Qual é o primeiro número da progressão?')
num = int(input())
print('Qual a razão?')
razao = int(input())

for i in range(10):
    aux = 0
    aux = num + i*razao
    print(f'{aux}',end =' ')