n = 0
s = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    s += n

print(f'A soma dos Valores foi {s}')