print('''
            11.2 – População: Modifique sua função para que ela exija um terceiro
            parâmetro, population. Agora ela deve devolver uma única string no formato
            Cidade, País – população xxx, por exemplo, Santiago, Chile – população
            5000000. Execute test_cities.py novamente. Certifique-se de que
            test_city_country() falhe dessa vez.
            Modifique a função para que o parâmetro population seja opcional. Execute
            test_cities.py novamente e garanta que test_city_country() passe novamente.
            Escreva um segundo teste chamado test_city_country_population() que
            verifique se você pode chamar sua função com os valores 'santiago', 'chile' e
            'population=5000000'. Execute test_cities.py novamente e garanta que esse
            novo teste passe.
''')

import unittest # importando o módolo que realiza o teste.
from city_functions import city_country # Importanto o módolo que será testado.

"""Clase do teste"""
class TestLocation(unittest.TestCase):

    def test_city_country(self):

        # Variável que armazena o resultado da fução 'city_country'.
        location = city_country('santiago', 'chile') 

        # Teste para verificar a iguadade dos valores esperados.
        self.assertEqual(location, 'Santiago, Chile')

    def test_city_country_population(self):

        # Variável que armazena o resultado da fução 'city_country'.
        location = city_country('santiago', 'chile', 5000000)
        
        # Teste para verificar a iguadade dos valores esperados.
        self.assertEqual(location, 'Santiago, Chile - Population = 5000000')


# Chamada do teste
unittest.main()
