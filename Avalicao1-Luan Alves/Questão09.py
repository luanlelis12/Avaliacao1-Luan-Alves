QMorango = int(input("Quantidades (em Kg) de morangos: "))
QMaca = int(input("Quantidade (em Kg) de maçãs: "))

if QMorango <= 5:
    PrecoMorango = 2.50 * QMorango
elif QMorango > 5:
    PrecoMorango = 2.20 * QMorango

if QMaca <= 5:
    PrecoMaca = 1.80 * QMaca
elif QMaca > 5:
    PrecoMaca = 1.50 * QMaca

if QMorango > 8 or PrecoMorango > 25:
    PrecoMorango *= 0.90 

if QMaca > 8 or PrecoMaca > 25:
    PrecoMaca *= 0.90 

print("Preço Total dos morangos: R$ %.2f" %PrecoMorango)
print("Preço Total das maçãs: R$ %.2f" %PrecoMaca)

input()