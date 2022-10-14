print('''
            6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
            que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
            cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
            age e city. Mostre cada informação armazenada em seu dicionário.
''')

pessoa = {
    'first_name': 'luis',
    'last_name': 'lima',
    'age': 31,
    'city': 'teresina'
}

print(f"O primeiro nome é {pessoa['first_name'].title()}, o sobrenome é {pessoa['last_name'].title()}, a idade é "
      f"{pessoa['age']}, a cidade onde mora é {pessoa['city'].title()}")