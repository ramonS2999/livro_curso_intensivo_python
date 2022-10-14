print('''
            8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
            função chamada show_magicians() que exiba o nome de cada mágico da
            lista.
''')

def show_magicians(magicians):
    for name in magicians:
        print(name.title())

magicians = ['aroudo', 'godinne', 'msr m', 'cris anjelo']

show_magicians(magicians)