print ("\nSubstituindo itens")
vetPrecos = []

contador = 0
while contador <5:
    valor = float(input("Digite o valor: "))
    vetPrecos.append(valor)
    contador = contador + 1
    print(vetPrecos)

valor3 = float(input("Digite o valor: "))
vetPrecos[3] = valor3
print(vetPrecos)
    
