print('''
            10.2 – Aprendendo C: Você pode usar o método replace() para substituir
            qualquer palavra por uma palavra diferente em uma string. Eis um exemplo
            rápido que mostra como substituir a palavra 'dog' por 'cat' em uma frase:
            >>> message = "I really like dogs."
            >>> message.replace('dog', 'cat') 'I really like cats.'
            Leia cada linha do arquivo learning_python.txt que você acabou de criar e
            substitua a palavra Python pelo nome de outra linguagem, por exemplo, C.
            Mostre cada linha modificada na tela.
''')

filename = "learning_python.txt"
with open(filename) as file_object:
    print(50*" =")
    lines = file_object.readlines()
    
    for line in lines:
        print(line.rstrip().replace("Python", "C"))
    print(50*" =")
