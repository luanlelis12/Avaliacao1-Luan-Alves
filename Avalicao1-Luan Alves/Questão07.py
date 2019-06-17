salario = float(input("Insira o salário do colaborador:"))

if salario <= 280:
    perAumento = 0.20
    aumento = salario*perAumento
    nSalario = salario+aumento
elif salario > 280 and salario < 700:
    perAumento = 0.15
    aumento = salario*perAumento
    nSalario = salario+aumento
elif salario > 700 and salario < 1500:
    perAumento = 0.10
    aumento = salario*perAumento
    nSalario = salario+aumento
elif salario > 1500:
    perAumento = 0.05
    aumento = salario*perAumento
    nSalario = salario+aumento

print("Salário antigo: R$ %.2f" %salario)
print("Percentual de aumento: %.2f" %perAumento)
print("Aumento: R$ %.2f" %aumento)
print("Salário novo: R$ %.2f" %nSalario)

input()