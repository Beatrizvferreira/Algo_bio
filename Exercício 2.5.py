genomas = open('Corona_genomic.fasta','r')
aux = []
conteudo = genomas.readlines()

genomas.close()

for i in conteudo:
     if i.find('>') != 0: 
       aux.append(i)

muda = ''

for i in aux:
    muda += i.replace('\n', '')

print(muda)
