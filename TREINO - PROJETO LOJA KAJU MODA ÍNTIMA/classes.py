# PROJETO LOJA

class Produto:
    """ESSA CLASSE DEFINE O PRODUTO"""
    def __init__(self, nome_produto, preco_unitario, qtd_comprada):
        """
        :param nome_produto: recebe uma string com o nome do produto
        :param preco_unitario: recebe o valor float de um produto
        :param qtd_comprada: recebe o valor int de quantidade de itens que foram comprados
        """
        self.__nome_produto = nome_produto
        self.__preco_unitario = preco_unitario
        self.__qtd_comprada = qtd_comprada

    def set_nome_produto(self, new_name):
        self.__nome_produto = new_name

    def set_preco_unitario(self, new_preco):
        self.__preco_unitario = new_preco

    def set_qtd_comprada(self, new_qtd):
        self.__qtd_comprada = new_qtd

    def get_nome(self):
        return self.__nome_produto

    def get_precounit(self):
        return self.__preco_unitario

    def get_qtdcomprada(self):
        return self.__qtd_comprada

    @staticmethod
    def mensagem_sucesso():
        print('Você finalizou com sucesso')


class Venda(Produto):
    def __init__(self, nome_produto, preco_unitario, qtd_comprada, qtd_venda, valor_venda):
        super().__init__(nome_produto, preco_unitario, qtd_comprada)
        self.qtd_venda = qtd_venda
        self.valor_venda = valor_venda
    def get_valor_venda(self):
        return self.valor_venda

    def venda_vista(self):
        print(f' {self.get_nome()} foi comprado por {self.get_precounit()}')
        print(f' {self.get_nome()} foi vendido por {self.get_valor_venda()}')
        #print(f'{self.get_nome()} no inventário = {(self.get_qtdcomprada() - )}')






    def forma_pagamento(self, forma_pagto):
        pass
            # pic pay
            # pix
            # transf.bancaria
            # a vista
            # dps

    def total_lucro_estoque(self):
        pass
        #total_lucro = self.preco_unitario * self.qtd_estoque
        #return total_lucro

