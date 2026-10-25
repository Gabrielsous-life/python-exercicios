s = 0
print('=' * 30)
print(' 10 PRIMEIROS TERMOS DE UMA PA ')
print('=' * 30)
termo1 = int(input('Priimeiro termo: '))
razao = int(input('Razão: '))
decimo = termo1 + (10 - 1 ) * razao
for c in range(termo1, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou')