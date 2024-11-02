import random
opcoes = ["pedra", "papel", "tesoura"]
vitorias_jogador = 0
vitorias_computador = 0

while vitorias_jogador < 3 and vitorias_computador < 3:
    escolha_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    if escolha_jogador not in opcoes:
        print("Escolha inválida! Tente novamente.")
        continue

    escolha_computador = random.choice(opcoes)
    print(f"Computador escolheu: {escolha_computador}")

    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
            (escolha_jogador == "papel" and escolha_computador == "pedra") or \
            (escolha_jogador == "tesoura" and escolha_computador == "papel"):
        print("Você ganhou esta rodada!")
        vitorias_jogador += 1
    else:
        print("O computador ganhou esta rodada!")
        vitorias_computador += 1

    print(f"Placar - Você: {vitorias_jogador}, Computador: {vitorias_computador}")

    if vitorias_jogador == 3:
        print("Você é o grande vencedor!")
    else:
        print("O computador é o grande vencedor!")

