print('''
            8.16 – Importações: Usando um programa que você tenha escrito e que
            contenha uma única função, armazene essa função em um arquivo separado.
            Importe a função para o arquivo principal de seu programa e chame-a usando
            cada uma das seguintes abordagens: import nome_do_módulo from
            nome_do_módulo import nome_da_função from nome_do_módulo import
            nome_da_função as nf import nome_do_módulo as nm from nome_do_módulo import
            *
''')

import modolo_001
from modolo_001 import build_profile
from modolo_001 import build_profile as bp
import modolo_001 as m
from modolo_001 import*

print(f"\n{20*'-=-'}\n")
modolo_001.build_profile('luis', 'silva', trabalho='TI', idade=31, sexo='masculino')

print(f"\n{20*'-=-'}\n")
build_profile('ramon', 'lima', trabalho='analista de TI', idade=32, sexo='masculino')

print(f"\n{20*'-=-'}\n")
bp('maria', 'eduarda', trabalho='programadora', idade=35, sexo='feminio', estado='piauí')

print(f"\n{20*'-=-'}\n")
m.build_profile('vanessa', 'gullart', trabalho='dev', idade=25, sexo='feminio', estado='rio grande do norte')
print(f"\n{20*'-=-'}\n")
