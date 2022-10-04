print('''
            8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
            nome de uma cidade e seu país. A função deve exibir uma frase simples, como
            Reykjavik está localizada na Islândia. Forneça um valor default ao
            parâmetro que representa o país. Chame sua função para três cidades
            diferentes em que pelo menos uma delas não esteja no país default.
''')


def describe_city(cidade, pais='Brasil'):
    return f"{cidade.title()} está localizada no {pais.title()}."


city1 = describe_city('teresina')
city2 = describe_city('são luis')
city3 = describe_city('new york', 'EUA')

print(city1)
print(city2)
print(city3)