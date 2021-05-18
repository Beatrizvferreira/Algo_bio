arquivoa = open('seq_a.fasta','r')
arquivob = open('seq_b.fasta','r')

conteudoa = arquivoa.readlines()
conteudob = arquivob.readlines()

arquivoa.close()
arquivob.close()

auxa=[]
auxb=[]

for linha in conteudoa:
     if linha.find('>') != 0: 
       auxa.append(linha)

for linha in conteudob:
     if linha.find('>') != 0:
       auxb.append(linha)

mudaa = ''
mudab = ''

for i in auxa:
    mudaa += i.replace('\n', '')

for i in auxb:
    mudab += i.replace('\n', '')

cont=0

for i in range(200):
    if mudaa[i] != mudab[i]:
      cont += 1
      print(f'a posição {i+1} foi trocado {mudaa[i]} --> {mudab[i]}')

print(f'O numero de nucleotideos diferentes é {cont}')