from classes import Produto, Venda

jogador1 = Produto('Marcos',45.00,10)
venda1 = Venda(jogador1.get_nome(), jogador1.get_precounit(), jogador1.get_qtdcomprada(), 2, 10)
print(venda1.venda_vista())
