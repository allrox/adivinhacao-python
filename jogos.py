import forca
import adivinhacaoPython

print("---------------------------")
print("|   Escolha o seu jogo!   |")
print("--------------------------\n")

print("[1] Forca [2] Adivinhação")
jogo = int(input("Qual é o jogo desejado?"))

if (jogo == 1):
    print("Forca\n")
    forca.jogar()

elif (jogo ==2 ):
    print("Adivinhação\n")
    adivinhacaoPython.jogar()