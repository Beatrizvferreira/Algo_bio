def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        m=1
        for i in range(n,1,-2):
            m *= i*(i-1)
        return m


num=int(input('Digite um número:'))
k = fatorial(num)
print(f'O fatorial de {num} é {k}.')
