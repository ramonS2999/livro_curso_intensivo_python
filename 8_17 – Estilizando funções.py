print('''
            8.17 – Estilizando funções: Escolha quaisquer três programas que você escreveu
            neste capítulo e garanta que estejam de acordo com as diretrizes de estilo
            descritas nesta seção.
''')

# --- importando os módolos ---
import modolo_001
from modolo_001 import build_profile
from modolo_001 import build_profile as bp
import modolo_001 as m
from modolo_001 import*

# --- usnado os módolos de formas diversas ---
print(f"\n{20*'-=-'}\n")
modolo_001.build_profile('luis', 'silva', trabalho='TI', idade=31, sexo='masculino')

print(f"\n{20*'-=-'}\n")
build_profile('ramon', 'lima', trabalho='analista de TI', idade=32, sexo='masculino')

print(f"\n{20*'-=-'}\n")
bp('maria', 'eduarda', trabalho='programadora', idade=35, sexo='feminio', estado='piauí')

print(f"\n{20*'-=-'}\n")
m.build_profile('vanessa', 'gullart', trabalho='dev', idade=25, sexo='feminio', estado='rio grande do norte')
print(f"\n{20*'-=-'}\n")
