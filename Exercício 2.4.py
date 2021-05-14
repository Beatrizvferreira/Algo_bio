print('Digite o DNA:')
genoma = input()
lista = []
aux = 0
contA = 0
contC = 0
contG = 0
contT = 0

for i in genoma:
    if (i != 'A') and (i != 'C') and (i != 'G') and (i != 'T'):
        print('Sequência de DNA inválida.')
        aux = 1
        break
    else:
        lista.append(i)
if aux != 1:
    qnt =len(lista)

    print(f'O número total de nucleotídeos da sequência digitada é {qnt}')
    for i in lista:
        if i == 'A':
            contA +=1
        elif i == 'C':
            contC +=1
        elif i == 'G':
            contG +=1
        elif i == 'T':
            contT +=1

    print('\n')
    print('A sequencia digitada possui:')
    print(f'{contA} Adenina (A)')
    print(f'{contG} Guanina (G)')
    print(f'{contC} Citosina (C)')
    print(f'{contT} Timina (T)')

    print('\n')
    print('A frequência de nucleotideos na sequência é')
    print(f'{(contA/qnt)*100:.2f}% Adenina (A)')
    print(f'{(contG/qnt)*100:.2f}% Guanina (G)')
    print(f'{(contC/qnt)*100:.2f}% Citosina (C)')
    print(f'{(contT/qnt)*100:.2f}% Timina (T)\n')
        
