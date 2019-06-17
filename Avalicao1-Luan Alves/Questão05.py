area = float(input("Qual é o tamanho da area a ser pintada: "))

litroUsado = (area/3)
quantidade = 1
balde = 18

while (quantidade*balde) < litroUsado:
    quantidade += 1

preco = ((quantidade*balde)*80)

print("Valor total: R$ %.2f" %preco)

input()