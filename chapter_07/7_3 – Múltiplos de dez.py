print('''

            7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
            número é múltiplo de dez ou não.

''')

mensagem = 'Digite um número: '

numero = input(mensagem)
numero = int(numero)

if numero % 10 == 0:
    print(f"{numero} é múltiplo de dez.")
else:
    print(f"{numero} não é múltiplo de dez.")