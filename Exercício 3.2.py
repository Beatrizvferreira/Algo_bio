dados = {}
pessoas = []
#num = int(input('Quantas pessoas irá cadastrar?'))
for i in range(2):
  dados['Nome'] = str(input('Qual o nome?'))
  dados['Sexo'] = str(input('Qual o sexo? (M/F)'))
  dados['Peso'] = float(input('Qual o peso?'))
  dados['Altura'] = float(input('Qual é a altura?'))
  dados['IMC'] = dados['Peso']/(dados['Altura']*dados['Altura'])
  pessoas.append(dados.copy())

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







