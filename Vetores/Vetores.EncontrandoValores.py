arqReais = open("Reais.txt", "r")
vetReais = []
vetReais = arqReais.readlines()

for x in vetReais:
    tamanho = len(vetReais)
valor = float(input("Digite o valor que procura: "))
contador = 0
posicao = -1
while contador < tamanho:
    vetReais[contador] = float(vetReais[contador])
    if valor == vetReais[contador]:
        posicao = contador
    contador = contador + 1
if posicao ==  -1:
    print("O valor não foi encontrado !")
else:
    print("O valor foi encontrado na posição: ",posicao)
    vetReais.pop(posicao)

