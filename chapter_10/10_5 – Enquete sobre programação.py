print('''
            10.5 – Enquete sobre programação: Escreva um laço while que pergunte às
            pessoas por que elas gostam de programação. Sempre que alguém fornecer um
            motivo, acrescente-o em um arquivo que armazene todas as respostas.
''')

filename = "guest_programming.txt"
with open(filename, 'a') as file_object:
    while True:
        print("Para sair digite 0")
        name = str(input("Por que gosta de programação? "))
        
        if name != '0':
            print(50*" =")
            file_object.write(name + "\n")
        else:
            break