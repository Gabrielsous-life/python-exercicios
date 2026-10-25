num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
num4 = int(input('Digite o ultimo numero: '))
rec = (num1, num2, num3, num4)
print(f'o numero 9 apareceu {rec.count(9)}')
print(f'3 na {rec.index(3) + 1}')
for c in rec:
    if c % 2 == 0:
        print(c, end=', ')
