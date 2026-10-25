comida = ('LANCHE', 'PIZZA', 'PASTEL', 'BRIGADEIRO')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in comida:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra.lower():
        if letra in vogais:
            print(letra, end=' ')
