from random import randint

print('=-'* 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'* 20)
cont = 0
jog = 0
while True:
    jog = int(input('Diga um valor: '))
    comp = randint(0,11)
    total = jog + comp
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador jogou {comp} o total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar denovo...')
print(f'Game over, você venceu um total de {cont}')