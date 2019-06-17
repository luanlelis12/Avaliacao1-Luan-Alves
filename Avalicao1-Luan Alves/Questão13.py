classe = [0,0,0,0,0,0,0,0,0]

cont = 0

resp = "S"

while resp=="S":

    vendaB  = float(input("Informe sua venda bruta: R$ "))
    
    salario = 200+(vendaB*0.09)

    if 200 <= salario and salario <= 299:
        classe[0] += 1
    elif 300 <= salario and salario <= 399:
        classe[1] += 1
    elif 400 <= salario and salario <= 499:
        classe[2] += 1
    elif 500 <= salario and salario <= 599:
        classe[3] += 1
    elif 600 <= salario and salario <= 699:
        classe[4] += 1
    elif 700 <= salario and salario <= 799:
        classe[5] += 1
    elif 800 <= salario and salario <= 899:
        classe[6] += 1
    elif 900 <= salario and salario <= 999:
        classe[7] += 1
    elif salario >= 1000:
        classe[8] += 1
    
    cont += 1
    
    resp = input("Continuar?(S ou N)")

    if resp == "N":
        break

for i in range(9):
    print("Vendedores de nível %i: %i" %(i+1,classe[i]))

input()