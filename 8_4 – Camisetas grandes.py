print('''
            8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
            camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
            uma camiseta grande e outra média com a mensagem default, e uma camiseta
            de qualquer tamanho com uma mensagem diferente.
''')


def make_shirt(tamanho='grande', texto='Eu amo Python'):
    return f"A camiseta tem tamanho {tamanho}, com a estampa '{texto}'."


camiseta1 = make_shirt('grande')
camiseta2 = make_shirt('média')
camiseta3 = make_shirt('pequena', 'I love you')

print(camiseta1)
print(camiseta2)
print(camiseta3)