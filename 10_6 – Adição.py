print('''
            10.6 – Adição: Um problema comum quando pedir entradas numéricas ocorre
            quando as pessoas fornecem texto no lugar de números. Ao tentar converter a
            entrada para um int, você obterá um TypeError. Escreva um programa que
            peça dois números ao usuário. Some-os e mostre o resultado. Capture o
            TypeError caso algum dos valores de entrada não seja um número e apresente
            uma mensagem de erro simpática. Teste seu programa fornecendo dois números
            e, em seguida, digite um texto no lugar de um número.
''')

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