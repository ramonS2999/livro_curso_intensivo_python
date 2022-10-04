print('''
            8.7 – Álbum: Escreva uma função chamada make_album() que construa um
            dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
            artista e o título de um álbum e deve devolver um dicionário contendo essas
            duas informações. Use a função para criar três dicionários que representem
            álbuns diferentes. Apresente cada valor devolvido para mostrar que os
            dicionários estão armazenando as informações do álbum corretamente.
            Acrescente um parâmetro opcional em make_album() que permita armazenar
            o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
            valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
            Faça pelo menos uma nova chamada da função incluindo o número de faixas
            em um álbum.
''')

def make_album(artista, titulo_do_album, numeros_de_faixas=12):
    dicionario = {
        'Artista': artista,
        'Título do álbum': titulo_do_album,
        'Número de faixas': numeros_de_faixas,
    }
    return dicionario

artista01 = make_album('neguinho da beija-flor', 'brasil você é lindo')
artista02 = make_album('rei da cacimbinha', 'morisoca pica')
artista03 = make_album('tiririca', 'florentina')
artista04 = make_album('maria da inglaterra', 'e o peru rodô', 15)

lista = []
lista.append(artista01)
lista.append(artista02)
lista.append(artista03)
lista.append(artista04)

for dicionarios in lista:
    for key, value in dicionarios.items():
        print(f"{key}: {value}")
    print()

print("Artista01 -> ", artista01)
print("Artista02 -> ", artista02)
print("artista03 -> ", artista03)
print("artista04 -> ", artista04)