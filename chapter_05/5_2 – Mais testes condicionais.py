print('''
            5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
            criar em dez. Se quiser testar mais comparações, escreva outros testes e
            acrescente-os em conditional_tests.py. Tenha pelo menos um resultado True e um
            False para cada um dos casos a seguir:
            • testes de igualdade e de não igualdade com strings; 
            • testes usando a função lower(); 
            • testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior 
              ou igual a e menor ou igual a; 
            • testes usando as palavras reservadas and e or; 
            • testes para verificar se um item está em uma lista; 
            • testes para verificar se um item não está em uma lista.
''')

lista_de_locais_para_viagem = ['Japão', 'EUA', 'Uruguay', 'Egito', 'Alemanha', 'França']
car = 'subaru'

print(f"Is 'subaru' == 'subaru'? I predict {'subaru' == 'subaru'}.")
print(f"Is 'subaru' != 'subaru'? I predict {'subaru' != 'subaru'}.")

print(f"Is car == 'SUBARU'.lower()? I predict {car == 'SUBARU'.lower()}.")
print(f"Is car != 'SUBARU'.lower()? I predict {car != 'SUBARU'.lower()}.")

print(f"Is 1 == 1? I predict {1 == 1}.")
print(f"Is 1 != 1? I predict {1 != 1}.")

print(f"Is 1 > 0? I predict {1 > 0}.")
print(f"Is 1 < 0? I predict {1 < 0}.")

print(f"Is 1 >= 0? I predict {1 >= 0}.")
print(f"Is 1 <= 0? I predict {1 <= 0}.")

print(f"Is 1 >= 1 and 1 < 2? I predict {1 >= 1 and 1 < 2}.")
print(f"Is 1 <= 1 and 1 > 2? I predict {1 <= 1 and 1 > 2}.")

print(f"Is 1 >= 0 or 1 < 2? I predict {1 >= 0 or 1 < 2}.")
print(f"Is 1 <= 0 or 1 > 2? I predict {1 <= 0 or 1 > 2}.")

print(f"Is 'Japão' in lista_de_locais_para_viagem? I predict {'Japão' in lista_de_locais_para_viagem}.")
print(f"Is 'Brasil' in lista_de_locais_para_viagem? I predict {'Brasil' in lista_de_locais_para_viagem}.")

print(f"Is 'Brasil' not in lista_de_locais_para_viagem? I predict {'Brasil' not in lista_de_locais_para_viagem}.")
print(f"Is 'Japão' not in lista_de_locais_para_viagem? I predict {'Japão' not in lista_de_locais_para_viagem}.")
