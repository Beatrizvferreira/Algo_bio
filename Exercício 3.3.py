def multiplo():
    a = int(input('Digite um número: \n'))
    b = int(input('Digite outro número: \n')) 
    if a==0 or b%a != 0:
        return False
    else:
        return True



print(multiplo())





