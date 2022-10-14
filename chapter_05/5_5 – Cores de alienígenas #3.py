print('''
            5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
            em uma cadeia if-elif-else.
            • Se o alienígena for verde, mostre uma mensagem informando que o jogador
              ganhou cinco pontos.
            • Se o alienígena for amarelo, mostre uma mensagem informando que o
              jogador ganhou dez pontos.
            • Se o alienígena for vermelho, mostre uma mensagem informando que o
              jogador ganhou quinze pontos.
            • Escreva três versões desse programa, garantindo que cada mensagem seja
              exibida para a cor apropriada do alienígena.
''')

alien_color = 'green'
if alien_color.lower() == "green":
    print(f"A cor do Alien é verde. o jogador acabou de ganhar 5 pontos por atingir o alienígena!")
elif alien_color.lower() == "yellow":
    print(f"A cor do Alien é amarelo. o jogador acabou de ganhar 10 pontos por atingir o alienígena!")
else:
    print(f"A cor do Alien é vermelho. o jogador acabou de ganhar 15 pontos por atingir o alienígena!")
print(f'\n{100*"="}\n')

alien_color = 'Yellow'
if alien_color.lower() == "green":
    print(f"A cor do Alien é verde. o jogador acabou de ganhar 5 pontos por atingir o alienígena!")
elif alien_color.lower() == "yellow":
    print(f"A cor do Alien é amarelo. o jogador acabou de ganhar 10 pontos por atingir o alienígena!")
else:
    print(f"A cor do Alien é vermelho. o jogador acabou de ganhar 15 pontos por atingir o alienígena!")
print(f'\n{100*"="}\n')

alien_color = 'red'
if alien_color.lower() == "green":
    print(f"A cor do Alien é verde. o jogador acabou de ganhar 5 pontos por atingir o alienígena!")
elif alien_color.lower() == "yellow":
    print(f"A cor do Alien é amarelo. o jogador acabou de ganhar 10 pontos por atingir o alienígena!")
else:
    print(f"A cor do Alien é vermelho. o jogador acabou de ganhar 15 pontos por atingir o alienígena!")
print(f'\n{100*"="}\n')