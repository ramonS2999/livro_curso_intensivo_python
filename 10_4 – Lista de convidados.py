print('''
            10.4 – Lista de convidados: Escreva um laço while que pergunte o nome aos
            usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
            acrescente uma linha que registre a visita do usuário em um arquivo chamado
            guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
            arquivo.
''')

filename = "guest_book.txt"
with open(filename, 'a') as file_object:
    while True:
        print("Para sair digite 0")
        name = str(input("Informe seu nome: "))
        
        if name != '0':
            print(f"muito prazer em ter você, {name}")
            print(50*" =")
            file_object.write(name + "\n")
        else:
            break
