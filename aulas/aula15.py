num = 0
s = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s += num
print('A soma vale {}'.format(s))# python 3
print(f'soma vale {s}')# python 3.6+ f strings