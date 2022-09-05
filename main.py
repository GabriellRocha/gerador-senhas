import random
import characters

password_list = []
print('Bem-vindo(a) ao gerador de senhas Py')
nr_letras = int(input('Quantas letras você gostaria na sua senha?\n'))
nr_simbolos = int(input('Quantos simbolos você gostaria?\n'))
nr_numeros = int(input('Quantos números você gostaria?\n'))
for i in range(nr_letras):
    password_list.append(random.choice(characters.letters))
for i in range(nr_simbolos):
    password_list.append(random.choice(characters.symbols))
for i in range(nr_numeros):
    password_list.append(random.choice(characters.numbers))

password = ''
random.shuffle(password_list)
for char in password_list:
    password += char
print(f'Sua senha é: {password}')
