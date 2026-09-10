# class Pessoa:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
# class Carro:
#     def __init__(self, modelo):
#         self.modelo = modelo

#     def acelerar(self):
#         print(f'{self.modelo} está acelerando.')

# p1 = Pessoa('Junior', 'Muniz')
# # p1.name = 'Junior'
# # p1.surname = 'Muniz'

# print(p1.name, p1.surname)

# p2 = Pessoa('Maria', 'Vitória')
# # p2.name = 'Maria'
# # p2.surname = 'Vitória'

# print(p2.name, p2.surname)

# kombi = Carro('Kombi')
# kombi.acelerar()

# celta = Carro('Celta')
# celta.acelerar()

# Carro.acelerar(celta)

# print(str.upper(kombi.modelo))
# print(str.upper(p1.name))
# print(str.upper(p1.surname))

class Camera:
    def __init__(self, name, filmando=False):
        self.name = name
        self.film = filmando

    def filmar(self):
        if self.film:
            print(f'{self.name} Já estar filmando.')
            return
        
        print(f'{self.name} Começou a filmar.')
        self.film = True

    def parar_film(self):
        if not self.film:
            print(f'{self.name} Não está filmando.')
            return

        print(f'{self.name} está parando de filmar...')
        self.film = False
    
    def fotografar(self):
        if self.film:
            print(f'{self.name} Não pode fotografar filmando.')
            return

        print(f'{self.name} está fotografando...')
            
c1 = Camera('CANON')
c2 = Camera('SONY')

c1.filmar()
c1.fotografar()
c1.parar_film()
c1.fotografar()
