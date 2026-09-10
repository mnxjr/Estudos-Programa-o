import json
from ex206_salvar_classesA import Pessoa, file_path


with open(file_path, 'r', encoding='utf8') as file:
    pessoas = json.load(file)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    print(p1.name)
    print(p2.name)
