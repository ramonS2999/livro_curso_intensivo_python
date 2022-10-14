print('''

            7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
            ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos
            de 3 anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o
            ingresso custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15
            dólares. Escreva um laço em que você pergunte a idade aos usuários e, então,
            informe-lhes o preço do ingresso do cinema.
''')

mensagem = [
    'Qual é a sua idade? ',
    'Você pode entrar de graça.\n',
    'O ingresso custa 10 dólares.\n',
    'O ingresso custa 15 dólares.\n',
    'Informe um valor válido!\n'
]

active = True
while active:
    idade = input(mensagem[0])

    if idade == 'sair':
        print("Fim")
        active = False

    elif idade.isdigit():
        idade = int(idade)
        if idade < 3:
            print(mensagem[1])
        elif idade <= 12:
            print(mensagem[2])
        else:
            print(mensagem[3])

    else:
        print(mensagem[4])
