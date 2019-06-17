frase = str(input("Insira a frase aqui: "))

tamanho = len(frase)
vazio = 0
vogal = 0

for i in range(0,tamanho):
    if frase[i] == " ":
        vazio += 1
    elif frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        vogal += 1

print("Nº de espaços em branco: %i" %vazio)
print("Nº de vogais: %i" %vogal)

input()