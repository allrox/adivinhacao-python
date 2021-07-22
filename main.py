print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numSecreto = 42
contador = 1
palpite = ""

while (contador <= 3) and (palpite != numSecreto):

    palpite = input("Digite seu palpite: ")
    palpite = int(palpite)
    print("Seu palpite foi:", palpite)

    acertou = palpite == numSecreto
    maior = palpite > numSecreto
    menor = palpite < numSecreto

    if (acertou):
        print("Parabéns, você acertou na sua",contador,"ª tentativa!\n")
    else:
        if (maior):
            print("Você errou sua",contador,"ª tentativa.")
            print("Seu número é maior que o número secreto.\n")
        elif (menor):
            print("Você errou sua", contador, "ª tentativa.")
            print("Seu número é menor que o número secreto.\n")

        contador += 1

print("Fim do jogo")