anos = int(input("Digite a quantidade de anos que é cliente"))
valor = float(input("Digite o valor da sua compra"))
quantidade = int(input("Digite a quantidade de compras no mês"))

if anos >10:
    descontoAnos = 15
else:
    descontoAnos = 0
if valor > 1500:
    descontoValor = 17
else:
    descontoValor = 0
if quantidade > 5:
    descontoQuantidade = 13
else:
    descontoQuantidade = 0

descontoTotal= descontoAnos + descontoValor + descontoQuantidade

aPagar = valor*descontoTotal/100 + valor

print ("O desconto foi de" , descontoTotal)
print ("O valor a pagar é de" , aPagar)
                       
