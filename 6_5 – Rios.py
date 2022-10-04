print('''
            6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
            cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
            • Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
              pelo Egito.
            • Use um laço para exibir o nome de cada rio incluído no dicionário.
            • Use um laço para exibir o nome de cada país incluído no dicionário.
''')

rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'mississippi': 'eua',
}

for rio, pais in rios.items():
    if pais == 'eua':
        print(f"O {rio.title()} corre pelo {pais.upper()}")
    else:
        print(f"O {rio.title()} corre pelo {pais.title()}")

print()
for rio in rios.keys():
    print(f"Key:  {rio.title()}")

print()
for pais in rios.values():
    print(f"Value:  {pais.title()}")
