import random

def jogar():
    #mengaem de inicializaçao de jogo
    imprime_mensagem_abertura()

    #escolha da palavra apartir de um arquivo
    palavara_secreta = carrega_palavra_secreta()
    # palavras encontrads
    palavra_encontrada = incializa_letras_encontradas(palavara_secreta)
    """laço para verificar se o usuario nao enforcou e nao acertou, o jogo
       continuaa """
    print(palavra_encontrada)

    enforcou = False
    acertou = False
    erros =  0

    while (not acertou and not enforcou):
        print("\nAinda possui -> {} tentativas".format(erros))
        chute = pede_chute_letra()

        #verificar se o chute existe
        if (chute in palavara_secreta):
            marca_chute_correto(chute,palavra_encontrada,palavara_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        #verificar se o número de erros foi igual a seis, no caso for TRUE é encerrado
        enforcou = erros == 7

        #verificar se a Variável acertou "_", primeira maneira de ecerra o loop
        # ENQUANTO NAO EXISTIR ->  "_"  O PROGRMA ENCERRA
        acertou = "_" not in palavra_encontrada

        #Mostraando os espaços ocupados
        print("-------------------------------------------")
        print("\n->{}".format(palavra_encontrada))
        print("-------------------------------------------")



    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_pededor(palavara_secreta)

#funçoes
def incializa_letras_encontradas(palavra):
    # Neste for, vamos acrescentar o número de caracteres, apartir do número de letras
    return ["_" for letra in palavra]


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

def carrega_palavra_secreta():
    arquivoteste = open("palavras.txt", "r")
    palavras = []
    # lendo cada linha do arquivo
    for linha in arquivoteste:
        linha = linha.strip()  # tirando \n
        palavras.append(linha)

    # fechar leitura do arquivo
    arquivoteste.close()

    # Selecionando a palavra
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pede_chute_letra():
    chute_palavra = input("\nQual a letra: ")
    # tirando o espaço do inicio e final, e colocando em letra maiuscula
    chute_palavra = chute_palavra.strip().upper()
    return chute_palavra

def marca_chute_correto(chute,palavra_encontrada,palavara_secreta):
    index = 0
    for letra in palavara_secreta:
        if (chute.upper() == letra.upper()):
            # colocando elemento em uma lista
            palavra_encontrada[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("\nParabéns!Você GANHOU!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_pededor(palavra_secreta):
    print("OPS!Não foi dessa fez!\nocê foi enforcado!!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()
