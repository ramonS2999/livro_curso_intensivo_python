print('''
            8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
            aceite o nome de uma cidade e seu país. A função deve devolver uma string
            formatada assim: "Santiago, Chile"
            Chame sua função com pelo menos três pares cidade-país e apresente o valor
            devolvido.
''')


def city_country(cidade, pais):
    return f"{cidade}, {pais}.".title()


city1 = city_country('são paulo', 'brasil')
city2 = city_country('santiago', 'chile')
city3 = city_country('new york', 'eua')

print(city1)
print(city2)
print(city3)