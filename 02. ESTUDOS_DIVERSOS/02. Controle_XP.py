"""
um jogo XYZ a cada item +5% xp
cada fase tem 25 itens, limite 100%
"""
from time import sleep

fases = ['F1', 'F2', 'F3', 'F4', 'F5']
itens = [25, 25, 25, 25, 25, 25]
backup = []
coletado = []


def calculador(fase, qtd_itens):
    while qtd_itens > 25:
        sleep(2)
        qtd_itens = int(input('Insira um valor inferior a 25!\n'))

    else:
        for i in range(0, len(fases)):
            for y in range(0, len(itens)):
                if fases[i] == fase:
                    if sum(coletado) > 100:
                        coletado.pop(0)
                        coletado.append(100)

                    coleta = qtd_itens * 5
                    backup.append(coleta)
                    quantidade = sum(backup)
                    var = itens[y]*5
                    if var > 100:
                        var = 100
                    if quantidade > var:
                        quantidade = 100
                        coletado.append(quantidade)
                        print(f'O usuário possui {quantidade}% de XP')
                        break
                    else:
                        coletado.append(quantidade)
                        print(f'O usuário possui {quantidade}% de XP')
                        break


def end_game():
    sleep(2)
    print('Vamos finalizar agora...')
    sleep(2)
    for i in range(0, len(fases)):
        print(f'Você na fase {fases[i]} ganhou {backup[i]} de XP, equivalente a {int(backup[i] / 5)} itens')
        sleep(2)
    print('Fim da Verificação')


calculador('F1', -1)
calculador('F2', 1)
calculador('F3', 0)
calculador('F4', 3)
calculador('F5', 0)
end_game()