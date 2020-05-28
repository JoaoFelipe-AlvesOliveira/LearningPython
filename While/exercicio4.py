base= int(input("Digite o numero base da potencia"))
expoente= int(input("Digite o numero expoente da potencia"))

if expoente <0:
    print("Erro: O expoente não pode ser negativo")

else:
        contador= 0
        resultado= 1
        while contador < expoente:
            resultado=resultado*base
            contador=contador+1
            print ("O valor da potencia é " , resultado)



            
