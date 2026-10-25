s = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados invalidos, Digite novamente:  ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))
