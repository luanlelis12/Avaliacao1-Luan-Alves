data = str(input("Insira uma data aqui ex:DD/MM/AAAA "))

D = data[:2]

M = data[3:5]

if M == "01":
    strM = "janeiro"
    diaMax = "31"

if M == "02":
    strM = "fevereiro"
    diaMax = "28"

if M == "03":
    strM = "março"
    diaMax = "31"

if M == "04":
    strM = "abril"
    diaMax = "30"

if M == "05":
    strM = "maio"
    diaMax = "31"

if M == "06":
    strM = "junho"
    diaMax = "30"

if M == "07":
    strM = "julho"
    diaMax = "31"

if M == "08":
    strM = "agosto"
    diaMax = "31"

if M == "09":
    strM = "setembro"
    diaMax = "30"

if M == "10":
    strM = "outubro"
    diaMax = "31"

if M == "11":
    strM = "novembro"
    diaMax = "30"

if M == "12":
    strM = "dezembro"
    diaMax = "31"    

A = data[6:10]

if D > diaMax:
    print("ERRO!")
else:
    print("%s de %s de %s" %(D,strM,A))

input()