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

print(muda)
