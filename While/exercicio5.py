
contador = 0

while contador<50:
    p1=float(input("Digite a nota da sua prova P1"))
    p2=float(input("Digite a nota da sua prova P2"))
    pap=float(input("Digite a nota do seu PAP"))
    atividade=float(input("Digite a nota da atividade"))
    media = p1 *0.3 + p2*0.3 + pap*0.2 + atividade*0.2
    contador = contador +1
    print("A sua média é " , media)

    if media <4:
        print("Reprovado")
    elif media<6:
        print("avaliação final")
    else:
        print ("Aprovado")
    
    
                        
    
