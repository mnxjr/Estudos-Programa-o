from os import system

def listar(l):
    print(f'{"Lista":^39}')
    print('='*39)
    for i, e in enumerate(l):
            print(f'- {i} {e}')


list_shop = []

while True:
    print('='*39)
    print(f"{'COMPRAS':^39}")
    print('='*39)
    print('[1] Adicionar\n[2] Apagar\n[3] Listar\n[4] Sair')
    print('-'*39)
    try:
        opc = int(input('SELECIONE UMA OPÇÃO: '))
        system('cls')
        print('-'*39)
    except:
        print('\033[31mError! Digite apenas números.\033[m')
        continue

    if opc == 1:
        listar(list_shop)    
        element = input('Qual item deseja adicionar? ').title()
        print(f'\033[32mO item "{element}" foi adicionado a sua lista.\033[m')
        list_shop.append(element)
    
    elif opc == 2:
        listar(list_shop)
        element = input('Qual item deseja apagar(escreva o índice)? ')
        try:
            index = int(element)
            print(f'O item "{list_shop[index]}" foi removido da lista.')
            del list_shop[index]
        except ValueError:
            print('Escolha um número inteiro válido.')
        except IndexError:
            print('Índice não encontrado.')
        except Exception:
            print('Erro desconhecido')
    
    elif opc == 3:
        listar(list_shop)
    
    elif opc == 4:
        print('Encerrando...')
        break

    else:
        print('\033[31mError! Escolha uma opção válida.\033[m')
print('Até mais!')
