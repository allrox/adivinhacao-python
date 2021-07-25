import random

def jogar():

    print("-----------------------------------------")
    print("|   Bem vindo ao jogo de adivinhação!   |")
    print("|       ------------------------        |")
    print("|        Um estudo sobre Python         |")
    print("-----------------------------------------\n")

    dificuldade = int(input("Digite 1 para o nível fácil, 2 médio ou 3 difícil: "))

    if (dificuldade == 1):
        numSecreto = int(random.randrange(1, 6))
        tentativas = 3
        print("Você terá {} chances para adivinhar o número secreto entre 1 e 5.\n".format(tentativas))

    elif(dificuldade == 2):
        numSecreto = int(random.randrange(1, 11))
        tentativas = 3
        print("Você terá {} chances para adivinhar o número secreto entre 1 e 10.\n".format(tentativas))

    elif(dificuldade == 3):
        numSecreto = int(random.randrange(1, 31))
        tentativas = 6
        print("Você terá {} chances para adivinhar o número secreto entre 1 e 30.\n".format(tentativas))

    contador = 1
    pontos = 1000
    palpite = ""

    for contador in range (1,tentativas+1):
        palpite = int(input("Digite seu palpite: "))
        print("Seu palpite foi:", palpite)

        acertou = palpite == numSecreto
        errou = palpite != numSecreto
        maior = palpite > numSecreto
        menor = palpite < numSecreto

        if (acertou):
            print("Parabéns, você acertou na sua {}ª tentativa!\n".format(contador))
            break

        else:
            if (maior):
                print("Você errou sua {}ª tentativa.".format(contador))
                print("Seu número é maior que o número secreto.\n")
            elif (menor):
                print("Você errou sua {}ª tentativa.".format(contador))
                print("Seu número é menor que o número secreto.\n")

            if (dificuldade == 1) or (dificuldade == 2):
                pontos -= abs(round(333.333))
            elif (dificuldade == 3):
                pontos -= abs(round(166.666))

    if (errou):
        print("O número secreto da rodada era {}.".format(numSecreto))

    print("Você fez {:04d} pontos.".format(pontos))
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()