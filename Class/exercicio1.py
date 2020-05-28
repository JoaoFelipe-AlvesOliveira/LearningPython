class Personagem:
    def __init__(self,codigo,nome,forca,saude,dinheiro):
        self.codigo = codigo
        self.nome = nome
        self.forca = forca
        self.saude = saude
        self.dinheiro = dinheiro

    def andar(self):
        self.forca = self.forca + 1
        self.saude = self.saude + 1
        return

    def correr(self,valorInteiro):
        self.saude = self.saude + valorInteiro
        return self.saude

    def atacar(self):
        self.forca = self.forca - 2
        return self.forca

    def defender (self):
        self.forca = self.forca - 1
        self.saude = self.saude - 1
        return

    def comprar (self, valorCompra):
        if valorCompra < self.dinheiro:
            self.dinheiro = self.dinheiro  - valorCompra
            return self.dinheiro

    def vender(self, valorVenda):
        self.dinheiro = self.dinheiro + valorVenda
        return self.dinheiro

personagem1 = Personagem (1,"Joao",10,100,300)
personagem2 = Personagem (2,"Lucas",50,40,700)

print("\nPersonagem 1")
print("Código",personagem1.codigo)
print("Nome", personagem1.nome)
print("Força", personagem1.forca)
print("Saude", personagem1.saude)
print("Dinheiro", personagem1.dinheiro)

print("\nPersonagem 2")
print("Código",personagem2.codigo)
print("Nome", personagem2.nome)
print("Força", personagem2.forca)
print("Saude", personagem2.saude)
print("Dinheiro", personagem2.dinheiro)

personagem1.andar()
print("\nPersonagem 1")
print("Código",personagem1.codigo)
print("Nome", personagem1.nome)
print("Força", personagem1.forca)
print("Saude", personagem1.saude)
print("Dinheiro", personagem1.dinheiro)

personagem2.correr(10)
saude = personagem2.correr(10)
print ("\nPersonagem 2")
print("Saude do personagem agora é ", saude)



        

    
    
        
