# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json

def listar(l):
    print('='*39)
    print(f"\033[34m{'Lista de Tarefas':^40}\033[m")
    print('='*39)
    for e in l:
            print(f'- {e}')


def ler(tarefas, ARQUIVO):
    dados = []
    try:
        with open(ARQUIVO, 'r', encoding='utf8') as file:
            dados = json.load(file)
            print('Arquivo Carregado')
    except FileNotFoundError:
        print('Arquivo Criado.')
        salvar(tarefas, ARQUIVO)
    return dados


def salvar(tarefas, ARQUIVO):
    dados = tarefas
    with open(ARQUIVO, 'w', encoding='utf8') as file:
        dados = json.dump(tarefas, file, indent=2, ensure_ascii=False)
    return dados


ARQUIVO = 'ex192_lista_taf.json'
primary = ler([], ARQUIVO)
secondary = []


while True:
    
    listar(primary)
    print('-'*39)

    print('Comandos: Desfazer e Refazer.')
    opc = input('Digite uma nova tarefa ou comando: ').title().strip()
    
    if opc == 'quit':
         break
    
    elif opc == 'desfazer':
        secondary.append(primary.pop())
    
    elif opc == 'refazer':
         
         if not secondary:
              continue
         else:
            primary.append(secondary.pop())
    else:
         primary.append(opc)

salvar(primary, ARQUIVO)

