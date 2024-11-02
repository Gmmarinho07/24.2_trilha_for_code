palavra_secreta = ['f', 'o','r','c','o','d','e']
letras_certas = []
print('-'*5 ,'Jogo da Forca', '-'*5)

for i in range(0, len(palavra_secreta)):
    letras_certas.append('-')


acertou = False

while acertou == False:
    letra = str(input("Digite uma letra: "))

    for i in range(0,len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_certas[i] = letra
        print(letras_certas[i])
   
   
    acertou = True


    for x in range(0, len(letras_certas)):
        if letras_certas[x] == "-":
            acertou = False
            

print('Parabéns')


