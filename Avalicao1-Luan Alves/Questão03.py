sexo = str(input("Você é homem ou mulher: "))
h = float(input("Insira a sua altura: "))

if sexo == "homem":
    pesoIdeal = ((72.7*h) - 58)
elif sexo == "mulher":
    pesoIdeal = ((62.1*h) - 44.7)
else:
    print("Opção invalida, digite apenas homem ou mulher")

print("Seu peso ideal é %f" %pesoIdeal)

input()