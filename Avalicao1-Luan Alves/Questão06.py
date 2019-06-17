resposta = str(input("Olá aluno(a), em qual turno você estuda (matutino - M, vespetino - V, noturno - N)? "))

if resposta == "M":
    print("Bom Dia!")
elif resposta == "V":
    print("Boa Tarde!")
elif resposta == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

input()