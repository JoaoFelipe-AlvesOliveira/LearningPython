print("\nPercorrendo todo o vetor mostrando seus itens")
vetPrecos = []

contador = 0
while contador <5:
    valor = float(input("Digite o valor: "))
    vetPrecos.append(valor)
    contador = contador + 1
    print(vetPrecos)

for x in vetPrecos:
    print(x)
