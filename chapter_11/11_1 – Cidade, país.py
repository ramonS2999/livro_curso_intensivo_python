print('''
            11.1 – Cidade, país: Escreva uma função que aceite dois parâmetros: o nome
            de uma cidade e o nome de um país. A função deve devolver uma única string
            no formado Cidade, País, por exemplo, Santiago, Chile. Armazene a função
            em um módulo chamado city_functions.py.
            Crie um arquivo de nome test_cities.py que teste a função que você acabou
            de escrever (lembre-se de que é necessário importar unittest e a função que
            você quer testar). Escreva um método chamado test_city_country() para
            conferir se a chamada à sua função com valores como 'santiago' e 'chile'
            resulta na string correta. Execute test_cities.py e garanta que
            test_city_country() passe no teste.
''')

import unittest # importando o módolo que realiza o teste.
from city_functions import city_country # Importanto o módolo que será testado.

"""Clase do teste"""
class TestLocation(unittest.TestCase):

    def test_city_country(self):

        # Variável que armazena o resultado da fução 'city_country'.
        location = city_country('santiago', 'chile') 

        # Teste para verificar a iguadade dos valores esperados.
        self.assertEqual(location, 'Chile, Santiago')

# Chamada do teste
unittest.main()
