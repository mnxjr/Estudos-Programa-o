# Exercício - sistema de perguntas e respostas
from time import sleep
from perguntas import perguntas
from random import sample

sorteadas = sample(perguntas, 5)



while True:
    cont = 0
    print('=-'*20)
    print('PERGUNTAS E RESPOSTAS'.center(40))
    print('=-'*20)
    
    for i, pergunta in enumerate(sorteadas):
        print(f'{i+1}. {pergunta["Pergunta"]}')
        sleep(0.5)
        
        correct = pergunta['Resposta'][0]
        
        for opção in pergunta['Opções']:
            print(opção)
        opc = input('Resposta: ').lower()
        
        if opc in 'abcde':
            if opc in correct:
                print('\033[32m✔ Parabéns! Você acertou!\033[m')
                cont += 1
            else:
                print('\033[31m❌ Você errou!\033[m')
                print(f'\033[33mA resposta correta era a\n{pergunta["Resposta"]}\033[m')
        else:
            print('\033[31mErro! Escolha uma opção válida.\033[m')
            continue
        print('-'*40)
    
    sleep(1)
    break

print(f'Você acertou {cont} de {len(sorteadas)} perguntas!')
print('=-'*20)
sleep(5)
