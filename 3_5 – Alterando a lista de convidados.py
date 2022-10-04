print('''
        3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
        convidados não poderá comparecer ao jantar, portanto será necessário enviar
        um novo conjunto de convites. Você deverá pensar em outra pessoa para
        convidar.
        • Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
        no final de seu programa, especificando o nome do convidado que não
        poderá comparecer.
        • Modifique sua lista, substituindo o nome do convidado que não poderá
        comparecer pelo nome da nova pessoa que você está convidando.
        • Exiba um segundo conjunto de mensagens com o convite, uma para cada
        pessoa que continua presente em sua lista.
''')

lista_de_convidados = ['Luis', 'Maria', 'Ana']

for nome_do_convidado in lista_de_convidados: print(nome_do_convidado , end=' | ')

print(f'\nSeja muito bem vindo {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.')

print(f"\nO confidado {lista_de_convidados[1]}, não poderá comparecer a festa.\n")

lista_de_convidados[1] = "Paula"

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')

print(f'\nSeja muito bem vindo {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.')