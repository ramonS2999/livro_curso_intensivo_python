print('''
            8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
            pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
            tantos itens quantos forem fornecidos pela chamada da função e deve
            apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
            um número diferente de argumentos a cada vez.
''')

def sanduiche(*items):
    print('Seu sanduíche contem os seguintes igredientes.')
    for item in items:
        print(f"- {item}")
    print(f"\n{20*'-=-'}\n")

print(f"\n{20*'-=-'}\n")
sanduiche('pepperone', 'tomate', 'cebola roxa')
sanduiche('queijo prato', 'oregano', 'pimentão verde', 'piclis')
sanduiche('calabresa')