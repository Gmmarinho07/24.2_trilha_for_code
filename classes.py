class Carro:
    def __init__(self, marca, cavalos, ligado):
        self.marca = marca
        self.cavalos = cavalos
        self.ligado = ligado


    def chama_marca(self):
        print(self.marca)



ferrari = Carro(marca = "Ferrari", cavalos = 400, ligado = True )

ferrari.chama_marca()