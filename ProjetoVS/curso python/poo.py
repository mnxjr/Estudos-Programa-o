class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    # dizer olá
    def dizer_ola(self):
        print(f'Olá, meu nome é {self.nome}, '
              f'tenho {self.idade} anos e {self.altura} de altura.')
    # cozinhar
    def cozinhar(self, receita: str):
        print(f'Meu nome é {self.nome} e estou cozinhando um(a) {receita}!')
    # andar
    def andar(self, metros: int):
        print(f'Meu nome é {self.nome} e ' 
              f'saí para caminhar {metros} metros.')


Pessoa1 = Pessoa('Kaique', 14, 1.65)
Pessoa2 = Pessoa('Julia', 24, 1.60)
Pessoa3 = Pessoa('Rebeca', 49, 1.72)

Pessoa1.dizer_ola()
Pessoa2.cozinhar('inhame')
Pessoa3.andar(2500)
