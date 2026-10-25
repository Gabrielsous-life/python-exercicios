print('-'*30)
print('     LOJA SUPER BARATÃO')
print('-'*30)
total = 0
totalmil = 0
menorvalor = 0
barato = 0
cont = 0
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do Produto: '))
    cont += 1
    total = total + valor
    if valor >= 1000:
        totalmil += 1
    if cont == 1:
        menorvalor = valor
    else:
        if valor < menorvalor:
            menorvalor = valor
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('----------- FIM DO PROGRAMA -----------')
print(f'O total da compra foi de RS: {total}')
print(f'Temos {totalmil} produtos custando mais de RS1000')
print(f'O produto mais barato foi a {barato} que custa RS{menorvalor}')
