ganhoHora = float(input("Quanto você ganho por hora: "))
hora = float(input("Quantas horas você trabalho por mês: "))

salarioBruto = (ganhoHora*hora)
ir = (salarioBruto*0.11)
inss = (salarioBruto*0.08)
sindicato = (salarioBruto*0.05)
salarioLiquido = (salarioBruto-ir-inss-sindicato)

print("Salário Bruto: R$ %f" %salarioBruto)
print("IR: R$ %f" %ir)
print("INSS: R$ %f" %inss)
print("Sindicato: R$ %f" %sindicato)
print("Salário Liquido: R$ %f" %salarioLiquido)

input()