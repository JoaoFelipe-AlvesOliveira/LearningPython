def restringirDoaçaoMulher(peso,sexo):
    if  peso < 50 or sexo == "f":
       resultado = ("Você não pode doar sangue, pois está abaixo do peso")
    else:
        resultado = ("Você pode doar sangue")
    return resultado
def restringirDoaçaoHomem(peso,sexo):
    if peso < 60 or sexo == "m":
        resultado = ("Você não pode doar sangue, pois está abaixo do peso")
    else:
        resultado = ("Você pode doar sangue")
    return resultado

peso = float(input("Informe o seu peso"))
sexo = (input("Informe o seu sexo apenas com as iniciais"))
resultado = restringirDoaçaoMulher(peso,sexo)
resultado = restringirDoaçaoHomem(peso,sexo)
print (resultado)

             
