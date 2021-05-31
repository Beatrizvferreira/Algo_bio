def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        m=1
        for i in range(n,1,-1):
            m *= i
        return m


num=int(input('Digite um número NATURAL:'))
k = fatorial(num)
print(f'O fatorial de {num} é {k}.')
