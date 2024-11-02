texto = """ Python é um linguagem de programação de alto nível."""

novo_texto = " "
lista_de_palavras = texto.split(' ')

for indice in range(len(lista_de_palavras)):
    if lista_de_palavras[indice] == "Python":
        lista_de_palavras[indice] = "Fython"

    

for palavra in lista_de_palavras:
    novo_texto = novo_texto + palavra + " "


print(novo_texto)