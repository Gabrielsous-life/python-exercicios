#tupula aceita tanto str como int como float
lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'
print(lanche)#aparece com ('')


for comida in lanche:
    print(f'Eu vou comer {comida}')#aparece cru com o print
print(len(lanche))#da os valores que tem na tupula


for cont in range(0, len(lanche)):#aparece cru sem print
    print(lanche[cont])


for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]} na posição {i}') # da os valores com o print e a posição do valor


for pos, comida2 in enumerate(lanche):
    print(f'Eu vou comer {comida2} na posição {pos}')

print(sorted(lanche))#valores em ordem, mostra o lanche em ordem


a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a
print(c)# mostra a, logo depois b
print(sorted(c))# mostra o a + b em ordem
print(c.count(2))#conta quantas vezes o valor selecionado aparece na tupula
print(c.index(8))#mostra a posição do valor selecionado, e pega apenas a primeira ocorrencia
print(c.index(5, 1))#valor 5 e começa na pos 1
#pessoa = 'Gustavo', 39, 'M', 99.88
#del(pessoa) deleta a tupula selecionada

#lanche[1] = 'Macarrão' erro pois não se pode atribuir valores a tupulas fora das proprias tupulas
#print(lanche)