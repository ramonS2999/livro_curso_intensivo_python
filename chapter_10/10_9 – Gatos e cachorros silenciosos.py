print('''
            10.9 – Gatos e cachorros silenciosos: Modifique o seu bloco except do Exercício
            10.8 para falhar silenciosamente caso um dos arquivos esteja ausente.
''')

# Criando uma função para ler os arquivos
def ler_arquivos(filename):
    # Bloco 'try-except' pra verificar os arquivos 
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

# Lista de arquivos
filename = ['cats.txt', 'dogs.txt']
for name in filename:
    ler_arquivos(name)