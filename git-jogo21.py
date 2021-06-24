## JOGOS DO LOBO ##
from operator import itemgetter
from random import choice
from time import sleep

# BASE DE CRIAÇÃO
naipes = ['Copas', 'Espadas', 'Ouro', 'Paus']
valor_carta = {'Copas': {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                         'R': 10, 'J': 10, 'Q': 10},
               'Espadas': {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                           'R': 10, 'J': 10, 'Q': 10},
               'Ouro': {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                        'R': 10, 'J': 10, 'Q': 10},
               'Paus': {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                        'R': 10, 'J': 10, 'Q': 10}}
aux = []


# DECLARAÇÃO FUNÇÕES
def sorteio_carta(name):
    """
    :param name: recebe como parâmetro o nome do jogador, para sinalizar quem está jogando.
    :return:
    """
    pontuacao = 0
    x = choice(naipes)
    for naipe, dic_tipo_carta in valor_carta.items():
        if naipe == x:
            for nome, valor in dic_tipo_carta.items():
                aux.append(nome)

    carta_sorteada = choice(aux)
    for naipe, dic_tipo_carta in valor_carta.items():
        if naipe == x:
            for nome, valor in dic_tipo_carta.items():
                if carta_sorteada == nome:
                    print(f' A sua carta sorteada foi {carta_sorteada} do naipe {naipe}')
                    pontuacao += valor
                    del dic_tipo_carta[nome]
                    aux.clear()
                    return pontuacao
                else:
                    continue
        else:
            continue


def qtd_jogadores():
    """
    :return: retorna um valor inteiro da quantidade de jogadores que irão participar do game. MIN/Máx.: 2 devido tempo de
    desenvolvimento do jogo
    """
    quantos = int(input('Quantos irão jogar?\n'))
    while quantos <= 0 or quantos > 6:
        quantos = int(input('Impossível... Tente com jogar com  um ou dois jogadores\n'
                            'Entendeu? :( \n '))
    else:
        jogadores = []
        for i in range(0, quantos):
            jogadores.append(input(f"Informe o nome do {i + 1}º Jogador: "))
        return jogadores


jogadores = qtd_jogadores()
print(f'Então... Esse jogo tem um preço... Só quem tirar 21 pontos estará livre dos jogos do Lobo..')
sleep(2)
print('Caso contrário...')
sleep(2)
print('Lobo Come... Tente ganhar... :)')
sleep(2)

deck = []
pontuacao = {}
contador = 3

for namer in range(0, len(jogadores)):
    sleep(2)
    print('Vez do jogador {}'.format(jogadores[namer]))
    nome_player = jogadores[namer]

    while contador > 0:
        deck.append(sorteio_carta(nome_player))
        contador -= 1
        sleep(2)
    else:
        print(f'{nome_player} você possui {sum(deck)} de pontos.')
        if sum(deck) > 21:
            contador = 3
            pontuacao[nome_player] = sum(deck)
            deck.clear()
            continue
        else:
            opcao = input(f'Você tem {sum(deck)} de pontos, desejar comprar outra carta?\n'
                          f'Se deseja continuar digite "Y" ou qualquer coisa interromper').lower()
            while opcao == "y":
                if sum(deck) <= 21:
                    deck.append(sorteio_carta(nome_player))
                    sleep(2)
                    opcao = input(f'Você tem {sum(deck)} de pontos, desejar comprar outra carta?\n'
                                  f'Se deseja continuar digite "Y" ou qualquer coisa interromper').lower()
                else:
                    opcao = 0
            else:
                print(f'O {nome_player} encerrou a partida com {sum(deck)} e comprou {len(deck)}')
                contador = 3
                pontuacao[nome_player] = sum(deck)
                deck.clear()
                continue
sorted(pontuacao.items(), key=itemgetter(-1), reverse=True)
for indice, valor in pontuacao.items():
    if valor == 21:
        sleep(2)
        print(f'Por incrível que pareça, {indice} venceu, portanto, está livre')
    else:
        sleep(2)
        print(f'Acho que {indice} não conseguiu a pontuação... :) Logo, Lobo come!')


