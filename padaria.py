class Padeiro:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 0
        self.paes = 0 
        pass

    def assar_paes(self, quantidade):
        if quantidade > 6:
            print('A capacidade máxima do forno é 6.')
        else:
            self.paes += quantidade
        pass



class Cliente:
    def __init__(self,nome, dinheiro):
        self.nome  = nome
        self.dinheiro = dinheiro
        self.paes = 0
        pass


    def comprar_paes(self, quantidade, padeiro):
        preco_pao = quantidade * 0.5
        if quantidade > padeiro.paes:
            print('Não há paes o suficiente.')

        elif self.dinheiro < quantidade * 0.5:
            print('Você não dinehiro o suficiente.')

        else:
            self.dinheiro -= preco_pao
            self.paes += quantidade
            padeiro.dinheiro += preco_pao 
            padeiro.paes -= quantidade
            print(f'Compra realizada com sucesso. Agora, {self.nome} tem {self.paes} paes e {self.dinheiro} reais.\
{padeiro.nome} tem {padeiro.paes} paes e {padeiro.dinheiro} reais.')
        pass


padeiro1 = Padeiro('Jorge')
padeiro1.assar_paes(6)
cliente1 = Cliente('Jorgina', 10)
cliente1.comprar_paes(3, padeiro1)

