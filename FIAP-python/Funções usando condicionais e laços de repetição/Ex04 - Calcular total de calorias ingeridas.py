qtdAlimentos = int(input("Informe a quantidade de alimentos ingeridos hoje: "))
caloriaTotal = 0.0

for x in range(1, qtdAlimentos+1):
    caloriaAtual = float(input("Informe a quantidade de calorias do {}º alimento: ".format(x)))
    caloriaTotal += caloriaAtual

print("O total de caloria ingerida é de {}".format(caloriaTotal))