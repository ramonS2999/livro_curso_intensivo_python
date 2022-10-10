print('''
            10.12 – Lembrando o número favorito: Combine os dois programas do Exercício
            10.11 em um único arquivo. Se o número já estiver armazenado, informe o
            número favorito ao usuário. Caso contrário, pergunte ao usuário qual é o seu
            número favorito e armazene-o em um arquivo. Execute o programa duas vezes
            para garantir que ele funciona.
''')

import json

def get_novo_numero_favorito():
    filename = 'numero_favorito.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def get_numero():
    username = input("Qual é o seu número favorito? ")
    filename = 'numero_favorito.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def get_numero_favorito():
    
    filename = get_novo_numero_favorito()
    if filename:
        print(f"Eu sei qual é o seu número favorito! É {filename}.")
    else:
        filename = get_numero()
        print(f"O seu número favorito é {filename}.")

get_numero_favorito()