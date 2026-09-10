# teste seus conhecimentos

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
quant = len(nome.replace(' ', ''))

if nome == '' or idade == '':
    print('Desculpe, você deixou campos vazios.')
else:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print('Seu nome têm espaços.') if ' ' in nome else print('Seu nome NÃO têm espaços.')
    print(f'Seu nome têm {quant} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
    