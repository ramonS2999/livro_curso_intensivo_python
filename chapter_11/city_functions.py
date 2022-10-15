
"""função para retornar a cidade e país."""
from itertools import count


def city_country(city, country, population=''):

    if population:
        # Variável para concatenar os nomes de cidade, país e população.
        location = f"{city}, {country} - population = {population}"
    else:
        # Variável para concatenar os nomes de cidade e país.
        location = f"{city}, {country}" 

    return location.title() 