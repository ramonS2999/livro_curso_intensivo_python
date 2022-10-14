print('''
            4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
            (página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
            Então faça o seguinte: • Adicione uma nova pizza à lista original.
            • Adicione uma pizza diferente à lista friend_pizzas.
            • Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
              favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.
              Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize
              um laço for para exibir a segunda lista. Certifique-se de que cada pizza
              nova esteja armazenada na lista apropriada.
''')

lista_de_pizza = ['calabresa', 'muçarela', 'pepperoni']
friend_pizzas = lista_de_pizza[:]

friend_pizzas.append('4 queijos')

print(f"Minhas pizzas favoritas são:")
for pizza in lista_de_pizza:
    print(pizza)

print(f"\nAs pizzas favoritas de meu amigo são:")
for pizza in friend_pizzas:
    print(pizza)

print("\nEu realmente adoro pizza!")
