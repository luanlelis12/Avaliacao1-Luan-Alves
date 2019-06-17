n1 = []
n2 = []
n3 = []
n4 = []
media = []
alunoMaior = 0

for i in range(0,10):
    valor = float(input("Insira sua 1º nota: "))
    n1.append(valor)
    valor = float(input("Insira sua 2º nota: "))
    n2.append(valor)
    valor = float(input("Insira sua 3º nota: "))
    n3.append(valor)
    valor = float(input("Insira sua 4º nota: "))
    n4.append(valor)
    media.append((n1[i]+n2[i]+n3[i]+n4[i])/4)

    if media[i]>=7:
        alunoMaior += 1

print("%i alunos ficaram maior ou igual que 7" %alunoMaior)

input()