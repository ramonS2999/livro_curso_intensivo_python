print('''
            5.3 – Cores de alienígenas #1: Suponha que um alienígena acabou de ser
            atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um
            valor igual a 'green', 'yellow' ou 'red'.
            • Escreva uma instrução if para testar se a cor do alienígena é verde. Se for,
              mostre uma mensagem informando que o jogador acabou de ganhar cinco
              pontos.
            • Escreva uma versão desse programa em que o teste if passe e outro em que
              ele falhe. (A versão que falha não terá nenhuma saída.
''')

alien_color = 'green'

if alien_color.lower() == "green":
    print(f"A cor do Alien é verde. o jogador acabou de ganhar 5 pontos!")
if alien_color.lower() == "red":
    pass
