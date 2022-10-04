print('''
            8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
            tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
            A função deve exibir uma frase que mostre o tamanho da camiseta e a
            mensagem estampada.
            Chame a função uma vez usando argumentos posicionais para criar uma
            camiseta. Chame a função uma segunda vez usando argumentos nomeados.
''')


def make_shirt(tamanho, texto):
    return f"A camiseta tem tamanho {tamanho}, com a estampa '{texto}'."


camiseta1 = make_shirt('media', 'I love you')
camiseta2 = make_shirt(texto='Take your time', tamanho='grande')

print(camiseta1)
print(camiseta2)