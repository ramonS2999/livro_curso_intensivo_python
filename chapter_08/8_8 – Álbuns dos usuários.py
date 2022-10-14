print('''
            8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
            Escreva um laço while que permita aos usuários fornecer o nome de um artista e
            o título de um álbum. Depois que tiver essas informações, chame make_album()
            com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
            um valor de saída no laço while.
''')

lista = []


def make_album(artista, titulo_do_album, numeros_de_faixas=12):
    dicionario = {
        'Artista': artista,
        'Título do álbum': titulo_do_album,
        'Número de faixas': numeros_de_faixas,
    }
    return dicionario


while True:
    artista = input('Informe o nome do artisita: (aperte "s" para saír a qualquer momento): ')
    if artista.lower() == 's': break

    album = input('Informe o nome do álbum: (aperte "s" para saír a qualquer momento): ')
    if album.lower() == 's': break

    quantidade_de_faixas = input('Informe a quantidade de faixas: (aperte "s" para saír a qualquer momento): ')
    if quantidade_de_faixas.lower() == 's': break

    if quantidade_de_faixas:
        lista.append(make_album(artista, album, quantidade_de_faixas))
    else:
        lista.append(make_album(artista, album))
    print()

print()
for dicionarios in lista:
    for key, value in dicionarios.items():
        print(f"{key}: {value}")
    print()

print("Lista -> ", lista)
