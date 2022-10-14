print('''

            7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário
            qual tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse
            carro, por exemplo, “Deixe-me ver se consigo um Subaru para você.”

''')
mensagem = 'Que tipo de carro você gostaria de alugar? '

carro = input(mensagem)

print(f"Deixe-me ver se consigo um {carro.title()} para você.")