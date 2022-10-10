print('''
            10.8 – Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo
            menos três nomes de gatos no primeiro arquivo e três nomes de cachorro no
            segundo arquivo. Escreva um programa que tente ler esses arquivos e mostre o
            conteúdo do arquivo na tela. Coloque seu código em um bloco try-except
            para capturar o erro FileNotFound e apresente uma mensagem simpática caso
            o arquivo não esteja presente. Mova um dos arquivos para um local diferente
            de seu sistema e garanta que o código no bloco except seja executado de
            forma apropriada.
''')

# Criando uma função para ler os arquivos
def ler_arquivos(filename):
    # Bloco 'try-except' pra verificar os arquivos 
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = f"Arquivo {filename} não foi encontrado."
        print(msg)
    else:
        print(contents)

# Lista de arquivos
filename = ['cats.txt', 'dogs.txt']
for name in filename:
    ler_arquivos(name)