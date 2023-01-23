transacoesQtd = int(input("Informe a quantidade de transações realizadas hoje: "))
transacoesTotal = 0.0

for x in range(1, transacoesQtd+1):
    transacao = float(input("Informe o valor da {}ª transação: R$".format(x)))
    transacoesTotal += transacao

print("O total gasto hoje é de R$ {}".format(transacoesTotal))