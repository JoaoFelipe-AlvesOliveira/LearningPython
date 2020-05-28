contador = 0
contAnos = 0
soma = 0

while contador<5:
    idade=int(input("Digite a idade"))
    soma = soma+idade
    if idade >=18:
        contAnos=contAnos + 1
    else:
        contador = contador +1
        media = soma/80
        print ("A média de idade é", media)
        print ("A quantidade de adultos é",contAnos)
