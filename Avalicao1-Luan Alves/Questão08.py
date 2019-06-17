Q1 = str(input("Telefonou para vítima? (Sim ou Não) "))
QSim = 0

if Q1 == "Sim":
    QSim += 1

Q2 = str(input("Esteve no local do crime? (Sim ou Não) "))

if Q2 == "Sim":
    QSim += 1

Q3 = str(input("Mora perto da vítima? (Sim ou Não) "))

if Q3 == "Sim":
    QSim += 1

Q4 = str(input("Devia para a vítima? (Sim ou Não) "))

if Q4 == "Sim":
    QSim += 1

Q5 = str(input("Já trabalhou com a vítima? (Sim ou Não) "))

if Q5 == "Sim":
    QSim += 1

if QSim == 2:
    situacao = "Suspeita"
elif QSim >= 3 and QSim <= 4:
    situacao = "Cúmplice"
elif QSim == 5:
    situacao = "Assassino"
else:
    situacao = "Inocente"

print("Classificado como %s." %situacao)
input()