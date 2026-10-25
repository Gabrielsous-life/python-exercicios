val = 0
cont = 0
while True:
    val = int(input('Diga o valor para ver a tabuada: '))
    if val < 0:
        break
    cont += 1
    t1 = val * 1
    t2 = val * 2
    t3 = val * 3
    t4 = val * 4
    t5 = val * 5
    t6 = val * 6
    t7 = val * 7
    t8 = val * 8
    t9 = val * 9
    t10 = val * 10
    print('-'*20)
    print(f'{val} X {cont} = {t1}')
    print(f'{val} X {cont} = {t2}')
    print(f'{val} X {cont} = {t3}')
    print(f'{val} X {cont} = {t4}')
    print(f'{val} X {cont} = {t5}')
    print(f'{val} X {cont} = {t6}')
    print(f'{val} X {cont} = {t7}')
    print(f'{val} X {cont} = {t8}')
    print(f'{val} X {cont} = {t9}')
    print(f'{val} X {cont} = {t10}')
    print('-' * 20)
print('Programa de tabuada encerrado, Volte sempre!')