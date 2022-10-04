print('''

            7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
            fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
            fornecido. À medida que cada ingrediente é especificado, apresente uma
            mensagem informando que você acrescentará esse ingrediente à pizza.
''')

pizza = {}
adicionais = []

mensagens = [
    'Infomre o sabor da Pizza: ',
    'Infomre o que gostaria de adicionar: '
]

active1 = True
while active1:
    sabor_da_pizar = input(mensagens[0])

    active2 = True
    if sabor_da_pizar.lower() != 'quit':

        while active2:
            adicionais_da_pizza = input(mensagens[1])
            adicionais.append(adicionais_da_pizza)

            if adicionais_da_pizza == 'quit':
                active2 = False
                del adicionais[:]
            else:
                pizza[sabor_da_pizar] = [opcao for opcao in adicionais]

    if sabor_da_pizar == 'quit':
        print()
        active1 = False

for sabor, adicionais in pizza.items():
    print(f"O sabor é {sabor.title()} ")
    for adicional in adicionais:
        print(f"\tAdicional de {adicional}")
    print()