print('''
            6.3 – Glossário: Um dicionário Python pode ser usado para modelar um
            dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de
            glossário.
            • Pense em cinco palavras relacionadas à programação que você conheceu
              nos capítulos anteriores. Use essas palavras como chaves em seu glossário e
              armazene seus significados como valores.
            • Mostre cada palavra e seu significado em uma saída formatada de modo
              elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
              significado, ou apresentar a palavra em uma linha e então exibir seu
              significado indentado em uma segunda linha. Utilize o caractere de quebra
              de linha (\\n) para inserir uma linha em branco entre cada par palavra-
              significado em sua saída.
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
               "\"era ele quem detinha o c.\"\n"
}

for siginificado in glossario:
    print(f"O siginificado de  {siginificado.upper()} é {glossario[siginificado]}")
