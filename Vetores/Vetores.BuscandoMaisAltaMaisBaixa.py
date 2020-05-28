vetTemperaturas = []
arqTemperaturas = open("Temperaturas.txt", "r")
vetTemperaturas = arqTemperaturas.readlines()

maisAlta = float(vetTemperaturas [0])
maisBaixa = float(vetTemperaturas [0])

for x in vetTemperaturas:
    print (x)
    x = float(x)
    if x >maisAlta:
        maisAlta = x
    if x < maisBaixa:
        maisBaixa = x
print ("A temperatura mais alta é ", maisAlta)
print ("A temperatura mais baixa é ", maisBaixa)
        
