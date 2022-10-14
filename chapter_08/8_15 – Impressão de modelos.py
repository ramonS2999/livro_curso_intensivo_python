print('''
            8.15 – Impressão de modelos: Coloque as funções do exemplo print_models.py
            em um arquivo separado de nome printing_functions.py. Escreva uma instrução
            import no início de print_models.py e modifique o arquivo para usar as funções
            importadas.
''')

import modolo_001 as m

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

m.print_models(unprinted_designs, completed_models)
m.show_completed_models(completed_models)
