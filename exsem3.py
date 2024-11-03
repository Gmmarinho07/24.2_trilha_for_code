from datetime import datetime

class Chamado:
    def __init__(self, id_chamado, descricao, solicitante):
        self.id_chamado = id_chamado
        self.descricao = descricao
        self.solicitante = solicitante
        self.data_abertura = datetime.now()
        self.status = "Aberto"
        self.tecnico_responsavel = None
        self.data_conclusao = None

    def atribuir_tecnico(self, tecnico):
        if self.status == "Aberto":
            self.tecnico_responsavel = tecnico
            self.status = "Em Atendimento"
            print(f"Técnico {tecnico.nome} atribuído ao chamado {self.id_chamado}.")
        else:
            print(f"Chamado {self.id_chamado} não está disponível para atribuição.")

    def resolver(self):
        if self.status == "Em Atendimento" and self.tecnico_responsavel:
            self.status = "Concluído"
            self.data_conclusao = datetime.now()
            print(f"Chamado {self.id_chamado} resolvido por {self.tecnico_responsavel.nome}.")
        else:
            print(f"Chamado {self.id_chamado} não está em atendimento.")

    def __str__(self):
        return f"Chamado {self.id_chamado}: {self.descricao} (Status: {self.status})"


class Tecnico:
    def __init__(self, nome):
        self.nome = nome
        self.chamados_atribuidos = []

    def atribuir_chamado(self, chamado):
        chamado.atribuir_tecnico(self)
        self.chamados_atribuidos.append(chamado)

    def __str__(self):
        return f"Técnico {self.nome}"


class SistemaChamados:
    def __init__(self):
        self.chamados = []
        self.tecnicos = []

    def abrir_chamado(self, descricao, solicitante):
        id_chamado = len(self.chamados) + 1
        chamado = Chamado(id_chamado, descricao, solicitante)
        self.chamados.append(chamado)
        print(f"Chamado {id_chamado} aberto para {solicitante}: {descricao}")
        return chamado

    def adicionar_tecnico(self, nome):
        tecnico = Tecnico(nome)
        self.tecnicos.append(tecnico)
        print(f"Técnico {nome} adicionado ao sistema.")
        return tecnico

    def listar_chamados(self):
        for chamado in self.chamados:
            print(chamado)

    def listar_tecnicos(self):
        for tecnico in self.tecnicos:
            print(tecnico)


# Exemplo de uso do sistema

sistema = SistemaChamados()

# Adicionando técnicos
tecnico1 = sistema.adicionar_tecnico("Gabriel Maia")
tecnico2 = sistema.adicionar_tecnico("João Victor")

# Abrindo chamados
chamado1 = sistema.abrir_chamado("Problema na conexão de internet", "Quarto 101")
chamado2 = sistema.abrir_chamado("Computador não liga", "Recepção")

# Atribuindo e resolvendo chamados
tecnico1.atribuir_chamado(chamado1)
chamado1.resolver()

tecnico2.atribuir_chamado(chamado2)
chamado2.resolver()

# Listando todos os chamados e técnicos
sistema.listar_chamados()
sistema.listar_tecnicos()
