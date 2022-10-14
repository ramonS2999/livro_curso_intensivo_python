print('''
            8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
            Exercício 8.9. Escreva uma função chamada make_great() que modifique a
            lista de mágicos acrescentando a expressão o Grande ao nome de cada
            mágico. Chame show_magicians() para ver se a lista foi realmente modificada.
''')


def show_magicians(magicians):
    for name in magicians:
        print(name.title())


def make_great(magicians):
    lista_auxiliar = magicians[:]
    del magicians[:]
    while lista_auxiliar:
        valor = f'Grande {lista_auxiliar.pop()}'
        magicians.insert(0, valor)


magicians = ['aroudo', 'godinne', 'msr m', 'cris anjelo']

make_great(magicians)
show_magicians(magicians)