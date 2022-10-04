print('''
        3.9 – Convidados para o jantar: Trabalhando com um dos programas dos
        Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma
        mensagem informando o número de pessoas que você está convidando para o
        jantar.
''')

lista_de_convidados = ['Luis', 'Maria', 'Ana']

for nome_do_convidado in lista_de_convidados:
    print(nome_do_convidado , end=' | ')

print('\n')
print(f'\nSeja muito bem vindo {lista_de_convidados[0]}! fique a vontate.')
print(f'{lista_de_convidados[1]}, é um prazer tela aqui conosco.')
print(f'A sua prezensa é sempre uma grande honra, {lista_de_convidados[2]}.')

print(f"\nA lista tem {len(lista_de_convidados)} convidados.")
