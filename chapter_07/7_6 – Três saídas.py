print('''

            7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício
            7.5 que faça o seguinte, pelo menos uma vez: 
            • use um teste condicional na instrução while para encerrar o laço; 
            • use uma variável active para controlar o tempo que o laço executará; 
            • use uma instrução break para sair do laço quando o usuário fornecer o valor 'quit'.
''')

mensagem = [
    'Qual é a sua idade? ',
    'Você pode entrar de graça.\n',
    'O ingresso custa 10 dólares.\n',
    'O ingresso custa 15 dólares.\n',
    'Encerrando o programa por informações incorretas!\n'
]

active = True
while active:
    idade = input(mensagem[0])

    if idade == 'quit':
        print("Fim")
        break

    elif idade.isdigit():
        idade = int(idade)
        if idade < 3:
            print(mensagem[1])
        elif idade <= 12:
            print(mensagem[2])
        else:
            print(mensagem[3])

    else:
        active = False
        print(mensagem[4])
