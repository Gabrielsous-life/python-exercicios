from random import randint

tentativa = 0
computador = randint (1, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegeu acertar qual foi? ')
acertou = False
while not acertou:
    jogador = int(input('Digite seu numero: '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Errou, o número é maior, tente novamente: ")
        elif jogador > computador:
            print('Errou, o número é menor, tente novamente: ')
print('Acertou')
print('Foram {} tentativas'.format(tentativa))
