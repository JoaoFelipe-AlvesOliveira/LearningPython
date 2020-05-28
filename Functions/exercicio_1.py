def calcularAumentoSalario(salario):
    if salario <1000:
        aumento = salario*10/100
    else:
        aumento = salario*5/100
    return aumento

salario = float(input("Digite o valor do salário"))
aumento = calcularAumentoSalario(salario)
novoSalario = salario+aumento
print ("O valor do salário com o aumento é", novoSalario)
