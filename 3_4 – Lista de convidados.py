print('''
        3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o
        jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
        que você gostaria de convidar para jantar. Em seguida, utilize sua lista para
        exibir uma mensagem para cada pessoa, convidando-a para jantar.
''')

lista_de_convidados = ['Luis', 'Maria', 'Ana']

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')

print('\n')
print(f'\nSeja muito bem vindo {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.')
