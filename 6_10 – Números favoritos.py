print('''
            6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
            147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
            apresente o nome de cada pessoa, juntamente com seus números favoritos.
''')

pessoa = {
    'luis': [5, 3, 26, 1],
    'ramon': [3, 10],
    'silva': [10, 33, 21],
    'lima': [30, 6, 78, 150, 44],
    'maria': [100, 50],
}

for nome, numeros in pessoa.items():
    print(f"Os números vaforitos de {nome.title()} são: ", end='')
    for numero in numeros:
        print(f' {numero}; ', end='')
    print('\n')
