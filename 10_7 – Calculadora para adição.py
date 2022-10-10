print('''
            10.7 – Calculadora para adição: Coloque o código do Exercício 10.6 em um
            laço while para que o usuário possa continuar fornecendo números, mesmo se
            cometerem um erro e digitarem um texto no lugar de um número.
''')

continuar = True # Variável que controla o laço
while continuar:
    # Bloco 'try-except' pra verificar os valores 
    try:
        n1 = int(input("Informe um valor numerico inteiro: "))
        n2 = int(input("Informe outro valor numerico inteiro: "))
    except TypeError:
        print("Digite apenas números inteiros!")
    except ValueError:
        print("Digite apenas números inteiros!")
    else:
        print(f"A soma é {n1+n2}")
    
    print(50*" =")
    opcao = input("Para sair digite 'n': ")
    if(opcao.upper() == "N"):
        continuar = False