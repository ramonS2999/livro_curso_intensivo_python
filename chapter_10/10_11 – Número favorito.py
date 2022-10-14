print('''
            10.11 – Número favorito: Escreva um programa que pergunte qual é o número
            favorito de um usuário. Use json.dump() para armazenar esse número em um
            arquivo. Escreva um programa separado que leia esse valor e apresente a
            mensagem “Eu sei qual é o seu número favorito! É _____.”.
''')

import json

def get_numero_favorito():
    
    filename = 'numero_favorito.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        username = input("Qual é o seu número favorito? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print(f"O seu número favorito é {username}.") 
    else:
        print(f"Eu sei qual é o seu número favorito! É {number}.")

get_numero_favorito()