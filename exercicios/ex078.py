valores = list()
for cont in range(0, 5):
    valores.append(input('\nDigite um valor: '))

print(f'\n Você digitou os valores {valores}')
print(f'\n O maior valor digitado foi {max(valores)}')
print(f'\n O menor valor digitado foi {min(valores)}')
print(f'\n A posição do maior valor é {valores.index(max(valores))}')
print(f'\n A posição do menor valor é {valores.index(min(valores))}')
