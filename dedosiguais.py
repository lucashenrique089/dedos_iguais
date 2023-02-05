from random import randint
from time import sleep

print('{}'.format('\033[1;35;40m'), '-=-' * 10, '...DEDOS IGUAIS...', '-=-' * 10, '{}' .format('\033[m'))

print('''
DEDOS IGUAIS!!!
[0]
[1]
[2]
[3]''')


print('-=-' * 10)
itens = (0, 1, 2, 3)
computador = randint(0,3)
jogador = int(input('Digite seu número, se for igual fazremos uma dupla:'))

nome = str(input('Digite seu nome: '))
print('O computador jogou {}' .format([computador]))

print('O jogador jogou {}' .format([jogador]))

print('DEDOS')

sleep(1.0)
print('IGUAIS')

print('JÁ')
sleep(1.0)

print('-=-' * 10)



if computador == 0:

        if jogador == 0:
            print('JOGAREMOS JUNTOS {}'.format(nome))

        elif jogador == 1:
            print('Não jogaremos juntos!')

        elif jogador == 2:
            print('Não Jogaremos juntos!')

        elif jogador == 3:
            print('Não jogaresmos juntos!')

if computador == 1:

        if jogador == 0:
            print('Não Jogaremos juntos!')

        elif jogador == 1:
            print('JOGAREMOS JUNTOS!!! {}'.format(nome))

        elif jogador == 2:
            print('Não jogaremos juntos!')

        elif jogador == 3:
            print('Não jogaremos juntos!')


if computador == 2:

        if jogador == 0:
            print('Não Jogaremos juntos!')

        elif jogador == 1:
            print('Não Jogaremos juntos!')

        elif jogador == 2:
            print('JOGAREMOS JUNTOS!!! {}'.format(nome))

        elif jogador == 3:
            print('Não jogaremos juntos!')

if computador == 3:

        if jogador == 0:
            print(' Não Jogaresmos juntos!')

        elif jogador == 1:
            print('Não Jogaremos juntos!')

        elif jogador == 2:
            print('Não Jogaremos juntos!')

        elif jogador == 3:
            print('JOGAREMOS JUNTOS!!! {}'.format(nome))































