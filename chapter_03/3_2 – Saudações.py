print('''
        3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
        simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas.
        O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve
        estar personalizada com o nome da pessoa.
''')

lista = ['Ana', "Maria", 'Janaina', 'Luis', 'Matheus', 'João', 'Fernanda']

print(f'Lista dos nomes -> {lista}')

for nome in lista:
    print(f'Olá grande {nome.title()}, saiba que gosto muito de você')