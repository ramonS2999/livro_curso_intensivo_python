print('''
        3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
        portanto agora tem mais espaço disponível. Pense em mais três convidados
        para o jantar.
        • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
        uma instrução print no final de seu programa informando às pessoas que
        você encontrou uma mesa de jantar maior.

        • Utilize insert() para adicionar um novo convidado no início de sua lista.
        • Utilize insert() para adicionar um novo convidado no meio de sua lista.
        • Utilize append() para adicionar um novo convidado no final de sua lista.
        • Exiba um novo conjunto de mensagens de convite, uma para cada pessoa 
	que está em sua lista.
''')

lista_de_convidados = ['Luis', 'Maria', 'Ana']

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado, end=' | ')

print(f'\nSeja muito bem vindo {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.')

print(f"\nO confidado {lista_de_convidados[1]}, não poderá comparecer a festa.\n")

lista_de_convidados[1] = "Paula"

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado, end=' | ')

print(f'\nSeja muito bem vindo {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.\n')

print(f'Encontrei uma mesa de jantar maior. Então dá pra convidar mais 3 pessoas.\n')

lista_de_convidados.insert(0, "Julha")
lista_de_convidados.insert(2, "João")
lista_de_convidados.append("Fernanda")

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado, end=' | ')

print(f'\nSeja muito bem vinda {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer telo aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.')
print(f'{lista_de_convidados[3]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[4]}.')
