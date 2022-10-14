print('''
            6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
            de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
            dicionário. Pense em um número favorito para cada pessoa e armazene cada
            um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu
            número favorito. Para que seja mais divertido ainda, faça uma enquete com
            alguns amigos e obtenha alguns dados reais para o seu programa.
''')

pessoa = {
    'luis': 5,
    'ramon': 3,
    'silva': 10,
    'lima': 30,
    'maria': 100
}

for nome in pessoa:
    print(f"O número vaforito de {nome} é {pessoa[nome]}")
