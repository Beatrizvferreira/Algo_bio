import matplotlib.pyplot as plt
import numpy as np
import math

num = int(input('Digite um número inteiro de pontos:'))

x = np.random.rand(1,num)
y = np.random.rand(1,num)
plt.scatter(x, y)
plt.xlabel('Raio')
plt.ylabel('Raio')
plt.title(f'Monte Carlo calcula de pi usando {num} pts')

plt.xlim([-0.05,1.05])
plt.grid()

x1 = np.arange(0,1,0.000001)
x2 = (1 - x1**2)**(1/2)

#a)
array_booleano = list(map(lambda x1,x2 : x1**2+x2**2 <1,x,y)) #Verifica se o ponto está dentro ou fora do círculo sem usar for nem while
soma_dentro_circulo = np.sum(array_booleano)
pi = 4*soma_dentro_circulo/num
print(f'A estimativa para a área do círculo é {pi:.3f}')

#b) Nesse caso, não há restrição sobre o uso do laço for, desta forma, para colorir os pontos faremos:

for i in range(num):
  z=x[0][i]**2 + y[0][i]**2
  if z<1:
    plt.plot(x[0][i],y[0][i],'o',color='red')
  else:
    plt.plot(x[0][i],y[0][i],'o',color='blue')



plt.plot(x1,x2,color='black',linewidth=4)
plt.show()import matplotlib.pyplot as plt
import numpy as np
import math

num = int(input('Digite um número inteiro de pontos:'))

x = np.random.rand(1,num)
y = np.random.rand(1,num)
plt.scatter(x, y)
plt.xlabel('Raio')
plt.ylabel('Raio')
plt.title(f'Monte Carlo calcula de pi usando {num} pts')

plt.xlim([-0.05,1.05])
plt.grid()

x1 = np.arange(0,1,0.000001)
x2 = (1 - x1**2)**(1/2)

#a)
array_booleano = list(map(lambda x1,x2 : x1**2+x2**2 <1,x,y)) #Verifica se o ponto está dentro ou fora do círculo sem usar for nem while
soma_dentro_circulo = np.sum(array_booleano)
pi = 4*soma_dentro_circulo/num
print(f'A estimativa para a área do círculo é {pi:.3f}')

#b) Nesse caso, não há restrição sobre o uso do laço for, desta forma, para colorir os pontos faremos:

for i in range(num):
  z=x[0][i]**2 + y[0][i]**2
  if z<1:
    plt.plot(x[0][i],y[0][i],'o',color='red')
  else:
    plt.plot(x[0][i],y[0][i],'o',color='blue')



plt.plot(x1,x2,color='black',linewidth=4)
plt.show()