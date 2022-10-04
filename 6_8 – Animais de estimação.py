print('''
            6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
            dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua
            o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
            chamada pets. Em seguida, percorra sua lista com um laço e, à medida que
            fizer isso, apresente tudo que você sabe sobre cada animal de estimação.
''')

rex = {
    'nome': 'rex',
    'dono': 'luis',
    'age': 5,
    'tipo': 'cachorro'
}

mimi = {
    'nome': 'mimi',
    'dono': 'maria',
    'age': 3,
    'tipo': 'gato'
}

pipo = {
    'nome': 'pipo',
    'dono': 'miguel',
    'age': 4,
    'tipo': 'papagai'
}
pets =[rex, mimi, pipo]

for animal in pets:
    print(f"Nome: {animal['nome'].title()}; Dono: {animal['dono'].title()}; Idade do animal: {animal['age']} anos; "
          f"Espécie: {animal['tipo']}")
