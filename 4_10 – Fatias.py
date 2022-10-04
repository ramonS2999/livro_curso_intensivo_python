print('''
            4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
            acrescente várias linhas no final do programa que façam o seguinte:
            • Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use 
              uma fatia para exibir os três primeiros itens da lista desse programa.
            • Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir
              três itens do meio da lista.
            • Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para
              exibir os três últimos itens da lista.
''')

lista_de_locais_para_viagem = ['Japão', 'EUA', 'Uruguay', 'Egito', 'Alemanha', 'França']


print(f"Lista completa: {lista_de_locais_para_viagem}\n")

print(f"Os três primeiros itens da lista são: {lista_de_locais_para_viagem[:3]}\n")

print(f"Três itens do meio da lista são: {lista_de_locais_para_viagem[2:5]}\n")

print(f"Os três últimos itens da lista são: {lista_de_locais_para_viagem[-3:]}\n")