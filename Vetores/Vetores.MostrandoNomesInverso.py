vetAlunos = []

contador = 0
while contador <5:
    nome = (input("Digite o nome: "))
    vetAlunos.append(nome)
    contador = contador + 1
print(vetAlunos)

while (contador > 0):
    contador = contador - 1
    print(vetAlunos[contador])
    
