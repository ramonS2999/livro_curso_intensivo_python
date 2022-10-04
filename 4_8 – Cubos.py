print('''
        4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por
        exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
        primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
        para exibir o valor de cada cubo.
''')

lista_de_numeros_ao_cubo = [valor**3 for valor in range(1, 11)]
print(lista_de_numeros_ao_cubo)


