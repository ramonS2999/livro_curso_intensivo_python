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
