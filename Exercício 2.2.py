print('Qual o deposito inicial?')
cap = float(input())
print('Qual a taxa de juros por mês de uma poupança? (Digite em porcentagem)') 
tax = float(input())
tax = tax/100

#Juros simples
for i in range(1,25):
    J = i*tax*cap
    Montante = cap + J
    print(f'Mês {i}: R${Montante:.2f}')

print(f'O ganho total foi de R${J:.2f}')