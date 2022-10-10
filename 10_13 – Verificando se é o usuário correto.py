print('''
            10.13 – Verificando se é o usuário correto: A última listagem de
            remember_me.py supõe que o usuário já forneceu seu nome ou que o programa
            está executando pela primeira vez. Devemos modificá-lo para o caso de o
            usuário atual não ser a pessoa que usou o programa pela última vez.
            Antes de exibir uma mensagem de boas-vindas de volta em greet_user(),
            pergunte ao usuário se seu nome está correto. Se não estiver, chame
            get_new_username() para obter o nome correto.
''')

import json

"""Obtém o nome do usuário já armazenado se estiver disponível."""
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

"""Pede um novo nome de usuário."""
def get_new_username(): 
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

"""Saúda o usuário pelo nome."""
def greet_user():
    
    username = get_stored_username()
    if username:
        conferir = input(f"O seu nome está correto {username}? Digite 's' para SIM: ")
        if conferir.upper() == "S":
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("Welcome back, " + username + "!")
    else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")

greet_user()