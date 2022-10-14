print('''
            5.12 – Estilizando instruções if: Revise os programas que você escreveu neste
            capítulo e certifique-se de que os testes condicionais foram estilizados de forma
            apropriada.
''')

print("Sim, os códigos foram estilizados de forma apropriada!")

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for nomero in lista_de_numeros:
    if nomero == 1:
        print(f"{nomero}st\n")
    elif nomero == 2:
        print(f"{nomero}nd\n")
    elif nomero == 3:
        print(f"{nomero}rd\n")
    else:
        print(f"{nomero}th\n")