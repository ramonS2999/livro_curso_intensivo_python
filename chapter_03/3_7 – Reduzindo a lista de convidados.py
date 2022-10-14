print('''
        3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
        mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
        dois convidados.
        • Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
        mostre uma mensagem informando que você pode convidar apenas duas
        pessoas para o jantar.
        • Utilize pop() para remover os convidados de sua lista, um de cada vez, até
        que apenas dois nomes permaneçam em sua lista. Sempre que remover um
        nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
        saiba que você sente muito por não poder convidá-la para o jantar.
        • Apresente uma mensagem para cada uma das duas pessoas que continuam
        na lista, permitindo que elas saibam que ainda estão convidadas.
        • Utilize del para remover os dois últimos nomes de sua lista, de modo que você
        tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
        uma lista vazia no final de seu programa.
''')

lista_de_convidados = ['Luis', 'Maria', 'Ana']

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')

print(f'\nSeja muito bem vindo {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.')

print(f"\nO confidado {lista_de_convidados[1]}, não poderá comparecer a vesta.\n")

lista_de_convidados[1] = "Paula"

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')

print(f'\nSeja muito bem vindo {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.\n')

print(f'Encontrei uma mesa de jantar maior. Então dá pra convidar mais 3 pessoas.\n')

lista_de_convidados.insert(0,"Julha")
lista_de_convidados.insert(2, "João")
lista_de_convidados.append("Fernanda")

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')

print(f'\nSeja muito bem vinda {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer telo aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.')
print(f'{lista_de_convidados[3]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[4]}.\n')

print(f'A mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.\n')

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')
print('\n')
for i in range (len(lista_de_convidados) - 2):
    print(f'{lista_de_convidados.pop()},Sinto muito por não poder lhe convidar para o jantar')

print('\n')
for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')
print('\n')
for nome_do_convidado in lista_de_convidados:
    if nome_do_convidado.upper() == "Julha".upper():
        print(f'{nome_do_convidado}, você ainda está convidada.')
    else:
        print(f'{nome_do_convidado}, você ainda está convidado.')

print('\n')

del lista_de_convidados[0]
del lista_de_convidados[0]

print(lista_de_convidados)
for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')