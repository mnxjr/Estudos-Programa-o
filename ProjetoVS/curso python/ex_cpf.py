

def validate_cpf(user):

    cpf = user\
        .replace(' ', '')\
        .replace('-', '')\
        .replace('.', '')
    if not cpf.isdigit():
        return False
    if cpf == cpf[0] * len(cpf):
        return False
    return validate1(cpf)

def validate1(cpf):
    nine_digits = cpf[:9]
    result = cont = 0

    for n in range(10, 1, -1): # soma cada element por contagem regressiva começando do 10
        result += n * int(nine_digits[cont]) # resultado da soma de todos dígitos
        cont += 1

    result = result * 10 % 11 # resultado multiplicado por 10 e resto da divisão por 11
    digit1 = result if result <= 9 else 0 # condição: resultado não pode ser maior que 9, else 0 
    return validate2(cpf, digit1)
        
def validate2(cpf, digit1):
    ten_digits = cpf[:10]
    result = cont = 0

    for n in range(11, 1, -1): # soma cada element por contagem regressiva começando do 11
        result += n * int(ten_digits[cont]) # resultado da soma de todos dígitos
        cont += 1

    result = result * 10 % 11 # resultado multiplicado por 10 e resto da divisão por 11
    digit2 = result if result <= 9 else 0 # condição: resultado não pode ser maior que 9, else 0
    cpf_temp = cpf[:9] + str(digit1) + str(digit2)
    if cpf_temp == cpf:
        return True
    else:
        return False

# ex_cpf = 746.824.890-70

print('='*35)
print(f'{"VALIDADOR DE CPF":^35}')
print('='*35)
while True:
    cpf = input('Digite um CPF: ')
    if cpf == 'sair':
        break
    if validate_cpf(cpf):
        print('CPF is valid')
    else:
        print('CPF is invalid')

print('Até mais!')
