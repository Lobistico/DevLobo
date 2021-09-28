import time
import pyautogui

name = ""
mochila = []

"""
Dialogo Inicial
"""
def namer():
    name = input("Qual é o seu nome?")
    while name == '':
        name = input("Você não disse qual é o seu nome?")
        if name != '':
            continue
    else:
        time.sleep(1)
        print(f'Ahh... Então você é o {name}!\n'
              f'É uma pena conhecer você dessa maneira...')
        time.sleep(1)
        print(f'Você ainda está com ela?... É eu sei...')
        time.sleep(1)
        print(f'\n\nVocê não sabe o que fez {name}?')
        time.sleep(1)
        print(f'Entendo... Qual caminho você vai escolher agora?')
        time.sleep(1)
        print(f'Responda "Direita" para a verdade ou "Esquerda" para a mentira\n'
              f'Parar aqui também é uma opção...')
        return name

"""
INICIO DO CAMINHO VERDADE
"""
def escolher(escolha):
    time.sleep(2)
    print('##########\n'
          'VOCÊ PODE ESCOLHER UMA OPÇÃO AGORA\n'
          'ESCREVA "D" para escolher verdade\n'
          'ESCREVA "E" para escolher mentira\n'
          'PARA PARAR ESCREVA "P" ou NADA\n'
          '##########')
    escolha = input(f'Qual é a sua escolha?')
    while escolha.isnumeric():
        escolha = input('Escolha uma opção válida')
    else:
        if len(escolha) > 1:
            print('GAME OVER')
        elif escolha.lower() == "d":
            print('Você escolheu a verdade...\n'
                  '########## VOCÊ ADQUIRE A MOCHILA E GANHOU VERDADE ##########\n')
            mochila.append('Verdade')

        elif escolha.lower() == "E":
            print('Você escolheu mentira...\n'
                  '########## VOCÊ ADQUIRE A MOCHILA E GANHOU MENTIRA ##########\n')
            mochila.append('Mentira')
        else:
            print('Seu programador é um animal! - VOCÊ ENCONTROU ESSE BUG COMO?')
    return escolha

"""
CAMINHO VERDADE - SEGUNDA PARTE
"""
def escolher2(quantidade_certa):
    print(f'Eu não esperava que você fosse escolher a verdade...'
          f'Mas já que escolheu, não tem jeito')
    time.sleep(2)
    try:
        chances = 3
        print('Você sabe qual é a quantidade de letras da maior palavras da língua portuguesa?')
        quantidade_certa = input("A palavra se chama 'Pneumoultramicroscopicossilicovulcanoconiose' \n")
        while not quantidade_certa.isnumeric():
            quantidade_certa = input('Você precisa digitar o valor númerico\n')
            chances -= 1
            if chances <=0:
                print('Você perdeu')
                break

        else:
            if len('Pneumoultramicroscopicossilicovulcanoconiose') == quantidade_certa:
                print('Você adquire o item "ACERTO"')
                mochila.append('Quantidade')
                return quantidade_certa
            else:

                quantidade_certa = input('Você errou o valor númerico... Tente novamente.\n')
                chances -=1
                if chances <= 0:
                    print("Você perdeu")
                    mochila[0] = 'Verdade'
                return quantidade_certa
    except ValueError as Erro:
        print('TIVEMOS UM BUG AQUI')


def valor(var):
    print("insira um valor>")
    b = 2 * var
    b = b + 1
    print(b)
    return var