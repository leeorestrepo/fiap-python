valido = False

while (valido == False):
    tipo_assinatura = int(input("[1] Basic 30%\n[2] Silver 20%\n[3] Gold 10%\n[4] Platinum 5%\nInforme o numero da assinatura: "))

    if 5 > tipo_assinatura > 0:
        valido = True
    else:
        print("Informe uma opção válida\n")
        
faturamento_anual = float(input("Informe seu faturamento anual: "))

if tipo_assinatura == 1:
    print("Bônus a pagar: {}".format(faturamento_anual * 0.30))
elif tipo_assinatura == 2:
    print("Bônus a pagar: {}".format(faturamento_anual * 0.20))
elif tipo_assinatura == 3:
    print("Bônus a pagar: {}".format(faturamento_anual * 0.10))
elif tipo_assinatura == 4:
    print("Bônus a pagar: {}".format(faturamento_anual * 0.05))