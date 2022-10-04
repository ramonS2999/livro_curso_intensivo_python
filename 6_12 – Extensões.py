print('''
            6.12 – Extensões: Estamos trabalhando agora com exemplos complexos o
            bastante para poderem ser estendidos de várias maneiras. Use um dos
            programas de exemplo deste capítulo e estenda-o acrescentando novas chaves
            e valores, alterando o contexto do programa ou melhorando a formatação da
            saída.
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
    print(120 * '_')
    print(f"{cidades.title()}| ")
    print(120 * '-')
    for detalhe, informacao in detalhes.items():
        print(f'\t {detalhe}: ', end='')
        print(f'{informacao}; ')
print(120*'_')
