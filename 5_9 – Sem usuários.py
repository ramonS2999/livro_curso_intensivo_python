print('''
            5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir
            que a lista de usuários não esteja vazia.
            • Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
              usuários!
            • Remova todos os nomes de usuário de sua lista e certifique-se de que a
              mensagem correta seja exibida.
''')

lista_de_usuarios = ['admin', 'luis', 'ana', 'vitória', 'roberto', 'joão', 'carlos', 'maria']
del lista_de_usuarios[:]

if lista_de_usuarios:
    for usuario in lista_de_usuarios:
        if usuario == 'admin':
            print(f"Olá {usuario}, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {usuario}, obrigado por fazer login novamente.")
else:
    print('Precisamos encontrar alguns usuários!')