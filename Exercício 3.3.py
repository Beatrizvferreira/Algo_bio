def multiplo():
    a = int(input('Digite um número: \n'))
    b = int(input('Digite outro número: \n')) 
    if b==0 or a%b != 0: #excluindo a divisão por 0
        return False
    else:
        return True

print(multiplo())





