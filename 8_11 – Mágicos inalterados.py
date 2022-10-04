print('''
            8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
            Chame a função make_great() com uma cópia da lista de nomes de mágicos.
            Como a lista original não será alterada, devolva a nova lista e armazene-a em
            uma lista separada. Chame show_magicians() com cada lista para mostrar que
            você tem uma lista de nomes originais e uma lista com a expressão o Grande
            adicionada ao nome de cada mágico.
''')


def show_magicians(magicians):
    for name in magicians:
        print(name.title())


def make_great(magicians_copy):
    lista_auxiliar = []
    while magicians_copy:
        valor = f'Grande {magicians_copy.pop()}'
        lista_auxiliar.insert(0, valor)
    return lista_auxiliar


originas_magicians = ['aroudo', 'godinne', 'msr m', 'cris anjelo']
modificada_magicians = make_great(originas_magicians[:])

print(" --- Lista original --- ")
show_magicians(originas_magicians)
print("\n --- Lista modificada --- ")
show_magicians(modificada_magicians)