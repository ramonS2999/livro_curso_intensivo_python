print('''
            6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com
            um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua
            sequência de instruções print por um laço que percorra as chaves e os valores
            do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais
            cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
            essas palavras e significados novos deverão ser automaticamente incluídos na
            saída.
''')

glossario = {
    "paradigima": "\n1. um exemplo que serve como modelo; padrão. \n"
                  "2. GRAMÁTICA conjunto de formas vocabulares que \n"
                  "servem de modelo para um sistema de flexão ou de "
                  "derivação (p.ex.: na declinação, na conjugação etc.); padrão.\n",

    "programação": "\n1. ação ou resultado de programar. \n"
                   "2. m.q. PROGRAMA ('lista escrita').\n",

    'decisão': "\n1. ato ou efeito de decidir; determinação.\n"
             "2. resolução tomada após julgamento; juízo, sentença.\n",

    'estrutura': "\n1. organização, disposição e ordem dos elementos essenciais \n"
                 "que compõem um corpo (concreto ou abstrato). e. de uma empresa \n"
                 "2. aquilo que dá sustentação a alguma coisa; armação, arcabouço.\n"
                 "\"e. de um prédio\"\n",

    'comando': "\n1. ato ou efeito de comandar; controle.\n"
               "\"perder o c. da situação \"\n"
               "2. poder, função, área de competência ou posto de comandante.\n"
               "\"era ele quem detinha o c.\"\n",

    'processual': '\nadjetivo\n'
                  'Relativo a procedimento (método ou processo); procedimental.\n'
                  '[Jurídico] Por procedimento, seguindo os mecanismos legais para colocar uma causa em juízo.\n'
                  'Jurídico] Relativo a procedura, parte do direito que se dedica ao cumprimento dos prazos.\n'
                  'expressão'
                  '[Informática] Programação Procedural. Sequência de processos que devem ser executados por um \n'
                  'programa, seguindo a linguagem específica que lhe é particular.\n'
                  'Etimologia (origem da palavra procedural). Procedura + al.\n',

    'Orientação a objeto':'\né um conceito que esta relacionado com a ideia de classificar , organizar e abstrair \n'
                          'coisas. Veja a definição formal: "O termo orientação a objetos significa organizar o mundo \n'
                          'real como uma coleção de objetos que incorporam estrutura de dados e um conjunto de operações \n'
                          'que manipulam estes dados.\n',

    'indentação': '\nsubstantivo feminino\n'
                  '1. [Informática, Tipografia]   Ato ou efeito de indentar.\n'
                  '2. [Informática, Tipografia]  Espaço entre a margem e o início do texto num parágrafo.\n',
    
    'função': '\nsubstantivo feminino\n'
              '1. atividade natural ou característica de um órgão, aparelho, engrenagem etc.\n'
              '2. obrigação a cumprir, papel a desempenhar.'
              '"f. de mediador"\n',

    'método': '\nsubstantivo masculino\n'
              '1. procedimento, técnica ou meio de fazer alguma coisa, esp. de acordo com um plano.\n'
              '2. processo organizado, lógico e sistemático de pesquisa, instrução, investigação, apresentação etc.\n'
              '"m. analítico, dedutivo"\n',
}

for palavra, siginificado in glossario.items():
    print(f"O siginificado da palavra {palavra.upper()} é {siginificado}")
