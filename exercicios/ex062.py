print('Gerador de PA')
print('-='*10)
pr = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
termo = pr
cont = 1
total = 0
mais = 5
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += ra
        cont+= 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('Fim')
print('Progreção finalizada com {} termos'.format(total))