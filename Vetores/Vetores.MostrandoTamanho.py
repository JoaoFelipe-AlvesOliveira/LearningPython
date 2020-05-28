print ("\nMostrando o tamanho do vetor")

vetPrecos = []

contador = 0
while contador <5:
    valor = float(input("Digite o valor"))
    vetPrecos.insert(0,valor)
    contador = contador +1
print ("Tamanho do vetor =", len(vetPrecos))
