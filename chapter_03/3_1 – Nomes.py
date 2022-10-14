print('''
        3.1 – Nomes: Armazene os nomes de alguns de seus amigos em uma lista
        chamada names. Exiba o nome de cada pessoa acessando cada elemento da
        lista, um de cada vez.
''')

lista = ['Ana', "Maria", 'Janaina', 'Luis', 'Matheus', 'João', 'Fernanda']

print(f'Lista dos nomes -> {lista}')

for nome in lista:
    print(nome.title())