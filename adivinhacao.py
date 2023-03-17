import random

def jogar():
    print("------------------------------------------------ ")
    print("\n\t\tBem vindo ao jogo de Adivinhação!\n")
    print("------------------------------------------------ ")

    # gerando o numero secreto pela funçao random
    # o randrange() determina de onde se deve começa e terminar
    numero_secreto = random.randrange(1, 101)#gera num de 0.0 e 1.0
    tentativa = 0
    pontos = 1000

    print("Qual nível de dificuldade?  ")
    print("""
    |1| - Fácil
    |2| - Médio
    |3| - Difícil\n""")
    nivel = int(input("Defina o nível:  "))

    # vericar o nivel do jogo , apartir da escolha do usuario
    if (nivel == 1 ):
        tentativa = 20
    elif (nivel == 2 ):
        tentativa = 10
    else:
        tentativa = 5

    #verificando e realizando o loop,
    print(numero_secreto)
    for contador in range(1, tentativa + 1):

        print(f"\nTentativas {contador} de {tentativa}\n")
        chute = int(input("Digite um numero entre 1 e 100: "))


        if chute < 1 or chute > 100:
            print("\n_______________________________________________________")
            print("\t\tNúmero invalido!!!\n\t\tDeve-se digitar entre 1 a 100")
            print("_______________________________________________________")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print(f"O número que você digitou: {chute}\n")

        if (acertou):
            print(f"Parabéns, acertou!!\nChute {chute} e número secreto {numero_secreto}")
            print("E fez {} pontos ".format(pontos))
            break

        else:
            if (maior):
                print("Você ERROU!\nO seu chute foi maior que o valor!")
            elif (menor):
                print("Voce ERROU!\nO seu chute foi menor que o valor!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(10 * "---")
    print("\n\t\tFIM DE JOGO!!!")
    print(10 * "---")
if (__name__ == "__main__"):
        jogar()
