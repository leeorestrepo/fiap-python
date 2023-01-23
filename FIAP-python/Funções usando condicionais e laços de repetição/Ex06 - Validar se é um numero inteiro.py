ultimo = 1
penultimo = 1
sucesso = False

tentativa = int(input("Informe um número inteiro: "))

if (tentativa == 1) or (tentativa == 2) or (tentativa == 3):
    sucesso = True
else:
    contador = 3
    while contador <= tentativa:
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual

        if (atual == tentativa):
            sucesso = True
        
        contador += 1
    
if sucesso:
    print("Ação bem-sucedida")
else:
    print("A ação falhou...")