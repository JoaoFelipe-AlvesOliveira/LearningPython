print("\nRemovendo o terceiro item")
vetPrecos = []

contador = 0
while contador <5:
    valor = float(input("Digite o valor"))
    vetPrecos.insert (0,valor)
    contador = contador + 1
    print(vetPrecos)

print("\nRemovendo o terceiro item")
vetPrecos.pop(2)
print(vetPrecos)
