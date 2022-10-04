print('''
            8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py, da página
            210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome
            e o sobrenome, além de três outros pares chave-valor que o descrevam.
''')

def build_profile(nome, sobrenome, **descricao):
    nome_completo = nome + ' ' + sobrenome
    print(f'Nome - {nome_completo.title()}')
    for key, value in descricao.items():
        print(f"{str(key).title()} - {str(value).title()}")
    print(f"\n{20*'-=-'}\n")

print(f"\n{20*'-=-'}\n")

build_profile('luis', 'silva', trabalho='TI', idade=31, sexo='masculino')
build_profile('ramon', 'lima', trabalho='analista de TI', idade=32, sexo='masculino')
build_profile('maria', 'eduarda', trabalho='programadora', idade=35, sexo='feminio', estado='piauí')