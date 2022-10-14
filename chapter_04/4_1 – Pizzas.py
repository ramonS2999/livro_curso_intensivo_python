print('''
        4.1 – Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os
        nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
        pizza.
        • Modifique seu laço for para mostrar uma frase usando o nome da pizza em
          vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha
          na saída contendo uma frase simples como Gosto de pizza de pepperoni.
        • Acrescente uma linha no final de seu programa, fora do laço for, que informe
          quanto você gosta de pizza. A saída deve ser constituída de três ou mais
          linhas sobre os tipos de pizza que você gosta e de uma frase adicional, por
          exemplo, Eu realmente adoro pizza!
''')

lista_de_pizza = ['calabresa', 'muçarela', 'pepperoni']

for pizza in lista_de_pizza:
    print(f"Eu adoro comer pizza de {pizza}.")

print("\nEu realmente adoro pizza!")

