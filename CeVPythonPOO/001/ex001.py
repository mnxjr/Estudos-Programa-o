class Gafanhoto:

    # Método Construtor  
    def __init__(self):  
        
        # Atributos de Instância
        self.name = ""
        self.idade = 0

    # Métodos de Instância
    
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.name} é Gafanhoto(a) e tem {self.idade} anos de idade"

# Declaração de Obejtos

g1 = Gafanhoto()
g1.name = "Maria"
g1.idade = 20
print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())