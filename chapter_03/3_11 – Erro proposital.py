print('''
        3.11 – Erro proposital: Se você ainda não recebeu um erro de índice em um de
        seus programas, tente fazer um erro desse tipo acontecer. Altere um índice em
        um de seus programas de modo a gerar um erro de índice. Não se esqueça de
        corrigir o erro antes de fechar o programa.
''')

lista = ['Ana', "Maria", 'Janaina', 'Luis', 'Matheus', 'João', 'Fernanda']

print(lista)
print(f'O tamnaho da lista é de {len(lista)}, e o codigo usado foi "print(lista[22])"\n')

try:
    print(lista[22])
except Exception as e:
    print(f'Mensagem de erro, diz que \'indice da lista fora de alcanse\': ', repr(e))