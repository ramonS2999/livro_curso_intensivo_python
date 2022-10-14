print('''

            7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
            quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
            oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
            contrário, informe que sua mesa está pronta.

''')
mensagem = 'Quantas pessoas estão para jantar? '

pessoas = input(mensagem)
pessoas = int(pessoas)

if pessoas > 8:
    print(f"Deverão esperar uma mesa.")
else:
    print("A mesa está pronta.")