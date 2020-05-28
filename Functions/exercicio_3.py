def calcularPercentualValores(valorPrincipal,valorRecebido):
    porcentagem = valorPrincipal+valorRecebido*100
    return porcentagem

valorPrincipal = float(input("Digite o valor principal"))
valorRecebido = float(input("Digite o valor recebido"))
porcentagem = calcularPercentualValores(valorPrincipal,valorRecebido)

if porcentagem <30:
    print("O percentual recebido é péssimo.","A porcentagem foi de",porcentagem,"%")
elif porcentagem <= 70:
    print ("O percentual recebido é regular.","A porcentagem foi de",porcentagem,"%")
else:
    print ("O percentual recebido é bom.","A porcentagem foi de",porcentagem,"%")
