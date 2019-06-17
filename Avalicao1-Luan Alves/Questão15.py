frase = str(input("Insira uma frase aqui: "))
letra = []
novaFrase = ''

tamanho = len(frase)

for i in range(0,tamanho):
    letra.append(frase[i])

for i in range(0,tamanho):
    
    if letra[i] == 'a' or letra[i] == 'A':
        novaFrase += '4'
    elif letra[i] == 'b' or letra[i] == 'B':
        novaFrase += '13'
    elif letra[i] == 'c' or letra[i] == 'C':
        novaFrase += '('
    elif letra[i] == 'd' or letra[i] == 'D':
        novaFrase += '[)'
    elif letra[i] == 'e' or letra[i] == 'E':
        novaFrase += '3'
    elif letra[i] == 'f' or letra[i] == 'F':
        novaFrase += '|='
    elif letra[i] == 'g' or letra[i] == 'G':
        novaFrase += '9'
    elif letra[i] == 'h' or letra[i] == 'H':
        novaFrase += '|-|'
    elif letra[i] == 'i' or letra[i] == 'I':
        novaFrase += '!'
    elif letra[i] == 'j' or letra[i] == 'J':
        novaFrase += '_|'
    elif letra[i] == 'k' or letra[i] == 'K':
        novaFrase += '|<'
    elif letra[i] == 'l' or letra[i] == 'L':
        novaFrase += '|_'
    elif letra[i] == 'm' or letra[i] == 'M':
        novaFrase += '|Y|'
    elif letra[i] == 'n' or letra[i] == 'N':
        novaFrase += '|\|'
    elif letra[i] == 'o' or letra[i] == 'O':
        novaFrase += '0'
    elif letra[i] == 'p' or letra[i] == 'P':
        novaFrase += '|>'
    elif letra[i] == 'q' or letra[i] == 'Q':
        novaFrase += '0,'
    elif letra[i] == 'r' or letra[i] == 'R':
        novaFrase += '|2'
    elif letra[i] == 's' or letra[i] == 'S':
        novaFrase += '5'
    elif letra[i] == 't' or letra[i] == 'T':
        novaFrase += '7'
    elif letra[i] == 'u' or letra[i] == 'U':
        novaFrase += '[_]'
    elif letra[i] == 'v' or letra[i] == 'V':
        novaFrase += '\/'
    elif letra[i] == 'w' or letra[i] == 'W':
        novaFrase += "\v/"
    elif letra[i] == 'x' or letra[i] == 'X':
        novaFrase += '}{'
    elif letra[i] == 'y' or letra[i] == 'Y':
        novaFrase += '`/'
    elif letra[i] == 'z' or letra[i] == 'Z':
        novaFrase += '2'
    elif letra[i] == ' ':
        novaFrase += ' '

print("%s" %novaFrase)

input()