print('''

            7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
            que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
            Acrescente um código próximo ao início de seu programa para exibir uma
            mensagem informando que a lanchonete está sem pastrami e, então, use um
            laço while para remover todas as ocorrências de 'pastrami' e
            sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
            finished_sandwiches.
''')

sandwich_orders = ['pastrami', 'x-burger', 'x-eggs', 'pastrami', 'triplo-x', 'x-lasanha', 'pastrami', 'x-tudo']
finished_sandwiches = []

print(" --- Estamos sem sanduíche de 'pastrami'. --- ")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    auxiliar = sandwich_orders.pop()
    print(f"Preperei seu {auxiliar}.")
    finished_sandwiches.append(auxiliar)

print()

print(" --- sandwichs finalizados --- ")
for sandwich in finished_sandwiches:
    print(sandwich, end='; ')