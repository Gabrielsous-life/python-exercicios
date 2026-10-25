print('Gerador de PA')
print('-='*10)
pr = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
termo = pr
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += ra
    cont+= 1
print('Acabou')