print('''
            6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
            • Crie uma lista de pessoas que devam participar da enquete sobre linguagem
              favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
              estão.
            • Percorra a lista de pessoas que devem participar da enquete. Se elas já
              tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por
              responder. Se ainda não participaram da enquete, apresente uma mensagem
              convidando-as a responder.
''')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

lista_de_pessoas_para_enquete = ['luis', 'phil', 'maria', 'sarah', 'carlos']

for nome in lista_de_pessoas_para_enquete:
    if nome not in favorite_languages.keys():
        print(f"Olá {nome}! Poderia responder nossa enquete, por gentileza?")
    else:
        print(f"Olá {nome}! Obriagdo por responder nossa enquete!!")
