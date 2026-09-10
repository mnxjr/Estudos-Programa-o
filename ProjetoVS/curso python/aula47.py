from os import system

secret_word = 'VAASCO'
right_letter = ''
cont = 0

print('-=' * 20)
print(f'{"PALAVRA SECRETA":^40}')
print('-=' * 20)

while True:
    letter = input('Escolha uma letra:').upper()
    cont += 1
    if len(letter) <= 1 and letter.isalpha():
        if letter in secret_word:
            right_letter += letter
            print('Acertou!')
        else:
            print('Errou, mas tente novamente.')
        
        formed_word = ''
        for secret_letter in secret_word:
            if secret_letter in right_letter:
                formed_word += secret_letter
            else:
                formed_word += '*'

        print('Palavra formatada: ', formed_word)
        print('-'*28)
        if secret_word == formed_word:
            system('cls')
            print(f'PARABÉNS!!! Você ganhou com um total de {cont} '
                    'tentativas.')
            print('A palavra era:', secret_word)
            cont = 0
            right_letter = ''
            print('-=' * 20)
    else:
        print('Digite apenas uma letra e somente letras!')
        