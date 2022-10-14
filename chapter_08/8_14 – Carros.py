print('''
            8.14 – Carros: Escreva uma função que armazene informações sobre um carro
            em um dicionário. A função sempre deve receber o nome de um fabricante e um
            modelo. Um número arbitrário de argumentos nomeados então deverá ser
            aceito. Chame a função com as informações necessárias e dois outros pares
            nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
            apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’,
            color=’blue’, tow_package=True) Mostre o dicionário devolvido para garantir
            que todas as informações foram armazenadas corretamente.
''')

def make_car(fabricante, modelo, **descricao):
    print(f'Fabricante - {fabricante.title()}')
    print(f'Modelo - {modelo.title()}')
    for key, value in descricao.items():
        print(f"{str(key).title()} - {str(value).title()}")
    print(f"\n{20*'-=-'}\n")

print(f"\n{20*'-=-'}\n")

make_car('subaru', 'outback', color='blue', tow_package=True)
make_car('toyota', 'hi lux', color='red', tow_package=True)
make_car('fiat', 'uno', color='pink', tow_package=True)