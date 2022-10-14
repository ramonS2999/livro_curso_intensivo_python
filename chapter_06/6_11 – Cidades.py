print('''
            6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
            cidades como chaves em seu dicionário. Crie um dicionário com informações
            sobre cada cidade e inclua o país em que a cidade está localizada, a
            população aproximada e um fato sobre essa cidade. As chaves do dicionário
            de cada cidade devem ser algo como country, population e fact. Apresente o
            nome de cada cidade e todas as informações que você armazenou sobre ela.
''')

cities = {
    'teresina': {
        'country': 'brasil',
        'population': 868075,
        'fact': 'O nome da cidade é uma homenagem à Imperatriz Teresa Cristina Maria de Bourbon, esposa de Dom Pedro 2º',
    },
    'parnaíba': {
        'country': 'brasil',
        'population': 153863,
        'fact': 'A Bacia do Parnaíba faz parte das doze regiões hidrográficas de todo o território do Brasil. \n'
                '\t Ela é formada por um grupamento de recursos hídricos que se deslocam para a região banhada pelo \n'
                '\t rio Parnaíba e todos os seus afluentes.',
    },
    'floriano': {
        'country': 'brasil',
        'population': 60111,
        'fact': 'Acidentes geográficos do município: Rio Parnaíba, que banha a cidade e o município em toda sua extensão.\n '
                '\t Seguem-lhe os rios Gurgueia e Itaueira',
    },
}

for cidades, detalhes in cities.items():
    print(f"A cidade de {cidades.title()}: ")
    for detalhe, informacao in detalhes.items():
        print(f'\t {detalhe}: ', end='')
        print(f'{informacao}; ')
    print('\n')
