print('''
            4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar
            laços for para fazer exibições a fim de economizar espaço. Escolha uma
            versão de foods.py e escreva dois laços for para exibir cada lista de comidas.
''')

lista_de_pizza = ['calabresa', 'muçarela', 'pepperoni']
friend_pizzas = ['pizza', 'falafel', 'carrot cake']

print(f"Minhas pizzas favoritas são:")
for pizza in lista_de_pizza:
    print(pizza)

print(f"\nAs comidas favoritas de meu amigo são:")
for pizza in friend_pizzas:
    print(pizza)

