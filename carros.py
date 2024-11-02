class Carro:
    def __init__(self, cor, marca, cavalos) -> None:
        self.cor = cor
        self.marca = marca
        self.cavalos= cavalos
        self.ligado = False
        self.desligar = True
        self.velocidade = 0
        pass




    def ligar(self):
        self.ligado = True
        pass


    def desligar(self):
        self.desligar  = False
        pass


    def acelerar(self):
        self.velocidade += 10
        pass



carro1 = Carro('Azul', 'Lamborghini', 450)
print(carro1.cor)
print(carro1.marca)
print(carro1.cavalos)

print(carro1.ligado, carro1.velocidade)
carro1.ligar()
carro1.acelerar()
print(carro1.ligado, carro1.velocidade)
