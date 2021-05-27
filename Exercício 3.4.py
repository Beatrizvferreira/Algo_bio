dados = {}
pessoas = []
aux = 0
#num = int(input('Quantas pessoas irá cadastrar?'))
while aux == 0:
  dados['Nome'] = str(input('Qual o nome?\n'))
  dados['Sexo'] = str(input('Qual o sexo? (M/F)\n'))
  dados['Peso'] = float(input('Qual o peso?\n'))
  dados['Altura'] = float(input('Qual é a altura?\n'))
  dados['IMC'] = dados['Peso']/(dados['Altura']*dados['Altura'])
  pessoas.append(dados.copy())
  aux = str(input('Deseja cadastrar mais alguém? (S/N): \n')).upper()
  if aux == 'S':
    aux = 0
  else:
    aux = 1

print('\n')
num = len(pessoas)
print(f'Foi/foram cadastrada(s) {num} pessoa(s)')

soma_peso = 0
soma_altura =0 
soma_imc =0
for i in pessoas:
  for k,v in i.items():
    if k == 'Peso':
      soma_peso += v
    elif k == 'Altura':
      soma_altura += v
    elif k == 'IMC':
      soma_imc += v

print(f'O peso médio das pessoas é {soma_peso/num:.2f}kg')
print(f'A altura média das pessoas é {soma_altura/num:.2f}m')
print(f'O ICM médio das pessoas é {soma_imc/num:.2f}kg/m^2')







