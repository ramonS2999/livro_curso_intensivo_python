print('''
        3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como
        motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
        lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter
        uma moto Honda”.
''')

lista = ['Honda', "Yamarra", 'Zuzuky']
message = [f"Gostaria de ter uma moto {lista[0]}", f"As mostos da {lista[1]} são lindas", f"{lista[2]} tem muita força"]

print(f'Lista -> {lista}')

for frase in message:
    print(frase)