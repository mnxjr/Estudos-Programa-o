import json

class Pessoa:

    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

p1 = Pessoa('John', 'Textor', 21, 'Male')
p2 = Pessoa('Mary', 'Foster', 49, 'Female')

dados = [vars(p1), vars(p2)]

file_path = 'ex206.json'

def fazer_dump():
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(
            dados,
            file,
            ensure_ascii=False,
            indent=2)

if __name__ == '__main__':
    fazer_dump()
