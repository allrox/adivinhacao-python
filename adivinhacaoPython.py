import random

print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

dificuldade = int(input("Digite 1 para o nível fácil, 2 médio ou 3 difícil:"))

if (dificuldade == 1):
    numSecreto = int(random.randrange(1, 5))
    tentativas = 3
    print("Você terá 3 chances para adivinhar o número secreto entre 1 e 5.\n")

elif(dificuldade == 2):
    numSecreto = int(random.randrange(1, 10))
    tentativas = 3
    print("Você terá 3 chances para adivinhar o número secreto entre 1 e 10.\n")

elif(dificuldade == 3):
    numSecreto = int(random.randrange(1, 30))
    tentativas = 6
    print("Você terá 6 chances para adivinhar o número secreto entre 1 e 30.\n")

contador = 1
pontos = 1000
palpite = ""

while (contador <= tentativas) and (palpite != numSecreto):

    palpite = input("Digite seu palpite: ")
    palpite = int(palpite)
    print("Seu palpite foi:", palpite)

    acertou = palpite == numSecreto
    errou = palpite != numSecreto
    maior = palpite > numSecreto
    menor = palpite < numSecreto

    if (acertou):
        print("Parabéns, você acertou na sua {}ª tentativa!\n".format(contador))
    else:
        if (maior):
            print("Você errou sua {}ª tentativa.".format(contador))
            print("Seu número é maior que o número secreto.\n")
        elif (menor):
            print("Você errou sua {}ª tentativa.".format(contador))
            print("Seu número é menor que o número secreto.\n")

        contador += 1
        if (dificuldade == 1) or (dificuldade == 2):
            pontos -= 300
        elif (dificuldade == 3):
            pontos -= 150

if (errou):
    print("O número secreto era:",numSecreto)

print("Você fez {} pontos.".format(pontos))
print("Fim do jogo")