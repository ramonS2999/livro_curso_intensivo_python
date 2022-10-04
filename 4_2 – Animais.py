print('''
        4.2 – Animais: Pense em pelo menos três animais diferentes que tenham uma
        característica em comum. Armazene os nomes desses animais em uma lista e,
        então, utilize um laço for para exibir o nome de cada animal.
        • Modifique seu programa para exibir uma frase sobre cada animal, por
          exemplo, Um cachorro seria um ótimo animal de estimação.
        • Acrescente uma linha no final de seu programa informando o que esses
          animais têm em comum. Você poderia exibir uma frase como Qualquer um
          desses animais seria um ótimo animal de estimação!
''')

lista_de_animais = ['cachorro', 'gato', 'coelho']

for animal in lista_de_animais:
    print(f"Um {animal} seria um ótimo animal de estimação.")

print("\nQualquer um desses animais seria um ótimo animal de estimação!")

