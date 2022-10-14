print('''
            10.3 – Convidado: Escreva um programa que pergunte o nome ao usuário.
            Quando ele responder, escreva o nome em um arquivo chamado guest.txt.
''')

filename = "guest.txt."

name_user = str(input("informe seu nome: "))

with open(filename, 'a') as file_object:
    file_object.write(name_user + "\n")