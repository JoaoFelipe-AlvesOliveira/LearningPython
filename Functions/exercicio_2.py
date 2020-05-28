def calculaBonusSalario(salario,faltas,atrasos):
    if faltas == 0 and atrasos <=3:
        bonus = salario*5/100
    else:
        bonus = salario*3/100
    return bonus

salario = float(input("Digite o valor do salário"))
faltas = int(input("Digite o numero de faltas"))
atrasos = int(input("Digite o numero de atrasos"))
bonus = calculaBonusSalario(salario,faltas,atrasos)
bonus = salario+bonus
print ("O valor do seu salario com bonus foi de", bonus)
