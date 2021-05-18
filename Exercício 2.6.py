genomas = open('Corona_genomic.fasta','r')
aux = []
conteudo = genomas.readlines()

genomas.close()

for i in conteudo:
     if i.find('>') != 0: # vai ignorar as linhas que não são importantes
       aux.append(i)

muda = ''

for i in aux:
    muda += i.replace('\n', '')

auxiliar = ''
aux.clear()
for i in muda:
  if (i  == 'A'):
    auxiliar += 'T'
  elif (i  == 'C'):
    auxiliar += 'G'
  elif (i  == 'G'):
    auxiliar += 'C'
  else:
     auxiliar += 'A'
 

print(auxiliar)

salvando = open('ex07_a.txt','w')
salvando.write(auxiliar)
salvando.close()
