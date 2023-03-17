import adivinhacao
import forca


def escolhe_jogo():

    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("""\n|1| - FORCA\n|2| - ADIVINHAÇÃO\n""")

    jogo_escolha = int(input("Qual o jogo? "))

    if jogo_escolha == 1:
        print("\t\tJOGO DA FORCA!!!!!!!!")
        forca.jogar()
    elif (jogo_escolha == 2):
        print("Jogo da ADIVINHAÇÃO")
        adivinhacao.jogar()
    else:
        print("Opção inválida!\nTente novamnte.")
if (__name__ == "__main__"):
    escolhe_jogo()
