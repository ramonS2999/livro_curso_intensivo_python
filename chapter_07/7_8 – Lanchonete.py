print('''

            7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
            os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
            finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
            mostre uma mensagem para cada pedido, por exemplo, Preparei seu
            sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
            para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
            prontos, mostre uma mensagem que liste cada sanduíche preparado.
''')

sandwich_orders = ['x-burger', 'x-eggs', 'triplo-x', 'x-lasanha', 'x-tudo']
finished_sandwiches = []

while sandwich_orders:
    auxiliar = sandwich_orders.pop()
    print(f"Preperei seu {auxiliar}.")
    finished_sandwiches.append(auxiliar)

print()
for sandwich in finished_sandwiches:
    print(sandwich, end='; ')