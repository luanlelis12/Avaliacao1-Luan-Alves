nome = str(input("Insira seu nome: "))

senha = str(input("Insira sua senha: "))

if senha == nome:
    while senha == nome:
        print("Erro! Por favor insira novamente as informações.")
        
        nome = str(input("Insira seu nome: "))

        senha = str(input("Insira sua senha: "))
