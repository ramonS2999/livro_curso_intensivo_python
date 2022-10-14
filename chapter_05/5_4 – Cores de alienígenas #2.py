print('''
            5.4 – Cores de alienígenas #2: Escolha uma cor para um alienígena, como foi 
            feito no Exercício 5.3, e escreva uma cadeia if-else.
            • Se a cor do alienígena for verde, mostre uma frase informando que o jogador
              acabou de ganhar cinco pontos por atingir o alienígena.
            • Se a cor do alienígena não for verde, mostre uma frase informando que o
              jogador acabou de ganhar dez pontos.
            • Escreva uma versão desse programa que execute o bloco if e outro que
              execute o bloco else.
''')

alien_color = 'green'
if alien_color.lower() == "green":
    print(f"A cor do Alien é verde. o jogador acabou de ganhar 5 pontos por atingir o alienígena!")
else:
    print(f"A cor do Alien não é verde. o jogador acabou de ganhar 10 pontos por atingir o alienígena!")

print(f'\n({30*")=("})\n')

alien_color = 'red'
if alien_color.lower() == "green":
    print(f"A cor do Alien é verde. o jogador acabou de ganhar 5 pontos por atingir o alienígena!")
else:
    print(f"A cor do Alien não é verde. o jogador acabou de ganhar 10 pontos por atingir o alienígena!")