segunda = int(input("Informe a qtd. de votos para Segunda-feira"))
terca = int(input("Informe a qtd. de votos para Terça-feira"))
quarta = int(input("Informe a qtd. de votos para Quarta-feira"))
quinta = int(input("Informe a qtd. de votos para Quinta-feira"))
sexta = int(input("Informe a qtd. de votos para Sexta-feira"))

maior = 0
diaLive = ""

if segunda > maior:
    maior = segunda
    diaLive = "Segunda-feira"
if terca > maior:
    maior = terca
    diaLive = "Terça-feira"
if quarta > maior:
    maior = quarta
    diaLive = "Quarta-feira"
if quinta > maior:
    maior = quinta
    diaLive = "Quinta-feira"
if sexta > maior:
    maior = sexta
    diaLive = "Sexta-feira"

print("O dia vencedor é {} com {} votos".format(diaLive, maior))