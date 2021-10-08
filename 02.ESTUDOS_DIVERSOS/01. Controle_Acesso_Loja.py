from time import sleep


def entrar_loja():
    print('Aguarde um pouco')
    sleep(2)
    print('Você irá continuar para a loja!')


def nome_jogador():
    player1 = input("Qual o nome do jogador?\n")
    while player1 == '':
        player1 = input('Digite um valor válido.\n')
    return player1


def fase1():
    global chance
    question1 = input('Qual é o nome do Eric?\n')
    while question1 != 'Eric':
        question1 = input('Errou, me diz qual é o nome do Eric?\n')
        chance = chance - 1
    else:
        if chance <= 0:
            reward.append(0)
            print('Você não ganhou nada :( Errou demais')
        elif chance < 3:
            reward.append(3)
            print(f'É... Parece finalmente você acertou!\n'
                  f'Portanto ganhou +3 reais.')
        else:
            print('Acertou! Você ganhou +5 reais')
            reward.append(5)


def fase2():
    global chance
    question1 = input('Qual é o nome do Presidente em 2021?')
    while question1 != 'Jair':
        question1 = input('Errou, qual é o nome do presidente?')
        chance = chance - 1
    else:
        if chance <= 0:
            reward.append(0)
            print('Você não ganhou nada :( Errou demais')
        elif chance < 3:
            reward.append(10)
            print(f'É... Parece finalmente você acertou!\n'
                  f'Portanto ganhou +10 reais.')
        else:
            print('Acertou! Você ganhou +15 reais')
            reward.append(15)


def fase4():
    global chance
    question1 = input('Qual é o profissional que cuida da saúde dos pés?\n')
    while question1 != 'Podólogo':
        question1 = input('Errou, qual é o profissional que cuida da saúde dos pés')
        chance = chance - 1
    else:
        if chance <= 0:
            reward.append(0)
            print('Você não ganhou nada :( Errou demais')
        elif chance < 3:
            reward.append(10)
            print(f'É... Parece finalmente você acertou!\n'
                  f'Portanto ganhou +10 reais.')
        else:
            print('Acertou! Você ganhou +25 reais')
            reward.append(25)


def gameover():
    if sum(reward) < 30:
        print('GAME OVER')
    else:
        print('Agora vamos para Loja')


def loja():
    print('Qual o item você deseja comprar?\n'
          f'Hoje nós temos "Carro", "Foguete" e "Casa"\n')
    while True:
        escolha = input('Qual é escolha? Digite 1 para Carro, 2 para Foguete e 3 para Casa')
        if escolha == "1":
            inventario.append('Carro')
            LOJA.pop(0)
            break
        elif escolha == '2':
            inventario.append('Foguete')
            LOJA.pop(1)
            break
        elif escolha == '3':
            inventario.append('Casa')
            LOJA.pop(2)
            break
        else:
            print('Digite um valor válido')


# DECLARAÇÃO DAS VARIÁVEIS
player = nome_jogador()
chance = 5
valor_restante = 50

# ESTRUTURAS DE CONTROLE
reward = []
inventario = []
valor_fase = [
    ["do Eric", 5],
    ["do Presidente", 15],
    ['do Bônus', 5],
    ['do Profissional', 25]
]
LOJA = [
    ["CARRO", 30],
    ['FOGUETE', 50],
    ['CASA', 40]
]
# INICIO DO GAME #
print(f'Então você é "{player}", é realmente um prazer te conhecer!\n'
      f'O jogo é simples, tente acertar ao máximo para comprar o item!')

# FASE 1 #
fase1()
# PÓS-FASE 1 #
valor_restante = valor_restante - valor_fase[0][1]
print(f'Você agora possui R$ {sum(reward)}, você pode ganhar no máximo R$ {valor_restante}.')
# FASE 2 #
fase2()
valor_restante = valor_restante - valor_fase[1][1]
print(f'Você agora possui R$ {sum(reward)}, você pode ganhar no máximo R$ {valor_restante}.')
# FASE 3 #
reward.append(5)
valor_restante = valor_restante - valor_fase[2][1]
sleep(2)
print(f'Você é nota 5,  portanto lhe dei 5 de presente'
      f'agora você possui R$ {sum(reward)}, você pode ganhar no máximo R$ {valor_restante}.')
# PREPARAÇÃO FASE 4 #
sleep(3)
fase4()
# CHECAGEM DE GAME OVER
gameover()
# FASE DE COMPRA DA LOJA#
sleep(3)
entrar_loja()
loja()

#FINAL
for x in inventario:
    final = x
    if x == "Carro":
        print(f'Você comprou um carro, e sobrou {sum(reward)-LOJA[0][1]}\n')
        print(f'Infelizmente, você não tem casa, logo não teve emprego :(')
    elif x == 'Foguete':
        print(f'Você gastou tudo em um Foguete?!!!\n')
        sleep(2)
        print(f'Você morreu no espaço...Sozinho!')
    else:
        print(f'Você teve uma casa, construiu uma família, conseguiu comprar um carro e depois um foguete :3 ')
        sleep(2)
        print('Fim do Jogo')

# CURIOSIDADE
sleep(5)
print('Agora que acabou... Vou te revelar a verdade de quantos valeu caba pontuação.')
for x, y in valor_fase:
    print(f'A fase {x} valeu R$ {y},00')

print('Finalizaremos aqui')

