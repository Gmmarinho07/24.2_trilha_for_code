def rpin():
    senha = input("Digite seu PIN: ")
    try:

        senha = int(senha)

    except:
        print("Senha inválida, tente um número!")
        senha = input("Digite seu PIN: ")
    
    print(senha)    

rpin()
