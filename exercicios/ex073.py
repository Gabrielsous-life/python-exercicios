times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Bragantino',
         'Atléticop-MG', 'Santos', 'Corinthians', 'Vasco da Gama', 'EC Vitória', 'Internacional', 'Ceará SC', 'Fortaleza', 'Juventude', 'Sport Recife' )
print('Os 5 primeiros times:')
for pri in range(0, 5):
    print(times[pri])
print('-='*20)
print('Os ultimos 4 times:')
for ult in range(16, 20):
    print(times[ult])
print('-='*20)
print('Os times em ordem alfabetica')
print(sorted(times))
print('-='*20)
print('A posição de cada time:')
for pos, times in enumerate(times):#ao inves do enumerate poderia ter usado o -len(lanche)
    print(f'O time {times} se esta na posição {pos}')
print('-='*20)
