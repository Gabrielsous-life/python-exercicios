totalh = 0
totalm20 = 0
total18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalh += 1
    if sexo == 'F' and idade < 20:
        totalm20 += 1
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {totalh} homens cadastrados')
print(f'E temos {totalm20} mulheres com menos de 20 anos')