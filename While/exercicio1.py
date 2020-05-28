popCod=int(input("Digite a população atual da cidade de Codó"))
popImp=int(input("Digite a populção atual da cidade de Imperatriz"))
quantAnos=0

while popCod<= popImp:
    popCod=popCod*0.04+popCod
    popImp=popImp*0.01+popImp
    quantAnos=quantAnos+1
print ("A quantidade de anos que a cidade de Codó vai demorar para ultrapassar a cidade de Imperatriz é",quantAnos)
