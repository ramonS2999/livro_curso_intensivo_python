print('''
        3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
        lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
        cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
        crie uma lista contendo esses itens e então utilize cada função apresentada
        neste capítulo pelo menos uma vez.
''')

lista = ['Ana', "Maria", 'Janaina', 'Luis', 'Matheus', 'João', 'Fernanda']

lista.insert(2, "Paula")
lista.append("Gustavo")

for nome in lista:
    print(f'title() : {nome.title()}')
print("")

for nome in lista:
    print(f'upper() : {nome.upper()}')
print("")

for nome in lista:
    print(f'lower() : {nome.lower()}')
print("")

print(f"\nO tamanho da lista é de {len(lista)} elementos.\n")

print(lista)
print(f'\npop(): {lista.pop()}')
print(lista)

del lista[0]
print(f'\ndel lista[0]: {lista}')

print(f'\nsorted(): {sorted(lista)}')

print(f'\nsorted(reverse=True): {sorted(lista, reverse=True)}')

lista.reverse()
print(f'\nreverse(): {lista}')

lista.sort()
print(f'\nsort(): {lista}')

lista.sort(reverse=True)
print(f'\nsort(reverse=True): {lista}')