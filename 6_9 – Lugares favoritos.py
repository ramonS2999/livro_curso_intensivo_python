print('''
            6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
            três nomes para usar como chaves do dicionário e armazene de um a três
            lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais
            interessante, peça a alguns amigos que nomeiem alguns de seus lugares
            favoritos. Percorra o dicionário com um laço e apresente o nome de cada
            pessoa e seus lugares favoritos.
''')

favorite_places = {
    'luis': ['teresina', 'parnaíba', 'fortaleza'],
    'ana': ['são luiz'],
    'maria': ['são paulo', 'rio de janeiro'],
}

for pessoa, lugares in favorite_places.items():
    print(pessoa.title())
    for lugar in lugares:
        print(f'\t\t{lugar.title()}')
    print(25*' * ')
