qtdTurma = 50
qtd = 0
soma = 0

alunoChamada = 1
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
while alunoChamada <= qtdTurma:
    if (alunoChamada % 2 ) == 1:
        nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NUMERO {}: \n".format(alunoChamada)))
        qtd += 1
        soma += nota
    alunoChamada += 1
mediaImpar = soma/qtd

alunoChamada = 1
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
while alunoChamada <= qtdTurma:
    
    if (alunoChamada % 2 ) == 0:
        nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NUMERO {}:\n".format(alunoChamada)))
        qtd += 1
        soma += nota

    alunoChamada += 1
mediaPar = soma/qtd

print("A nota média dos alunos de número impar é: {}".format(mediaImpar))
print("A nota média dos alunos de número par é: {}".format(mediaPar))

if (mediaPar > mediaImpar):
    print("Os alunos de número Par tiveram a maior nota")
elif (mediaImpar > mediaPar):
    print("Os alunos de número Impar tiveram a maior nota")
else:
    print("Ambos tiveram as mesmas notas")