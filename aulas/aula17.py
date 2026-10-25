lanche = ['LANCHE', 'PIZZA', 'PASTEL', 'BRIGADEIRO']#lista são mutáveis
print('\n', lanche)
lanche[1] = 'HOT DOG'
print('\n', lanche)
#lanche[4] = 'SUCO' #não existe a posição 4 na lista, só é possível adicionar com append ou insert
lanche.append('SUCO') #adiciona no final da lista
print('\n', lanche)
lanche.insert(2, 'ÁGUA') #adiciona na posição desejada, empurrando os outros elementos para a direita
print('\n', lanche)
lanche.insert(0, 'LANCHE')
print('\n', lanche)
lanche.remove('PASTEL') #remove o elemento desejado
print('\n', lanche)
lanche.pop() #remove o último elemento da lista
lanche.pop() #remove o último elemento da lista
print('\n', lanche)
lanche.pop(1) #remove o elemento da posição desejada
print('\n', lanche)
if 'PAÇOCA' in lanche:
    lanche.remove('PAÇOCA') #remove o elemento desejado
print('\n', lanche)
valores = list(range(4, 11)) #cria uma lista com valores de 4 a 10
print('\n', valores)
valores = list(range(4, 11)) #cria uma lista com valores de 4 a 10
print('\n', valores)
valores.sort() #ordena a lista em ordem crescente
print('\n', valores)
valores.sort(reverse=True) #ordena a lista em ordem decrescente
print('\n', valores)
len(valores)
print('\n', len(valores)) #mostra o tamanho da lista
for c, v in enumerate(valores): 
    print(f'\nNa posição {c} encontrei o valor {v}')
#for cont in range(0, 5):
    #valores.append(int(input('\nDigite um valor: ')))
a = [2, 3, 4, 5]
b = a #ligação entre as listas, qualquer alteração em b altera também a em a
print('\n', f'Lista A: {a}')
print('\n', f'Lista B: {b}')
b[2] = 8
print('\n', f'Lista A após alteração na lista A: {a}')
print('\n', f'Lista B após alteração na lista B: {b}')
b = a[:] #cópia da lista a para b, sem ligação entre as listas
b[2] = 9
print('\n', f'Lista A após alteração na lista A: {a}')
print('\n', f'Lista B após alteração na lista B: {b}')
