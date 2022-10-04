print('''
            6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
            (página 147). Crie dois novos dicionários que representem pessoas diferentes e
            armazene os três dicionários em uma lista chamada people. Percorra sua lista
            de pessoas com um laço. À medida que percorrer a lista, apresente tudo que
            você sabe sobre cada pessoa.
''')

pessoa1 = {
    'first_name': 'luis',
    'last_name': 'lima',
    'age': 31,
    'city': 'teresina'
}

pessoa2 = {
    'first_name': 'maria',
    'last_name': 'silva',
    'age': 19,
    'city': 'são paulo'
}

pessoa3 = {
    'first_name': 'iara',
    'last_name': 'sousa',
    'age': 26,
    'city': 'rio de janeiro'
}
people =[pessoa1, pessoa2, pessoa3]

for dados in people:
    print(f"Nome completo: {dados['first_name'].title()} {dados['last_name'].title()}; "
          f"Idade: {dados['age']} anos; Cidade onde mora: {dados['city'].title()}")
