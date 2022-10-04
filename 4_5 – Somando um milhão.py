print('''
        4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use 
        min() e max() para garantir que sua lista realmente começa em um e termina em um
        milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é
        capaz de somar um milhão de números.
''')

lista_de_1000000 = [valor for valor in range(1, 1000001)]
print(lista_de_1000000)

print(f"{min(lista_de_1000000)} - min(lista_de_1000000)")
print(f"{max(lista_de_1000000)} - max(lista_de_1000000)")
print(f"{sum(lista_de_1000000)} - sum(lista_de_1000000)")
