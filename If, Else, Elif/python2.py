medida1 = float(input("Digite a primeira medida"))
medida2 = float(input("Digite a segunda medida"))
medida3 = float(input("Digite a terceira medida"))

if medida3 > medida2 and medida1:
    print ("É um triangulo")
elif medida1 == medida2 and medida2 == medida3:
    print ("É um equilatero")
elif medida1 == medida2 or medida2 == medida3 or medida3 == medida1:
    print ("Triangulo isóceles")
else:
    print ("É um triangulo escaleno")
    
