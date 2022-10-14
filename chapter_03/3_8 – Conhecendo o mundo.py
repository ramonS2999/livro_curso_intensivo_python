print('''
            3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
            você gostaria de visitar.
            • Armazene as localidades em uma lista. Certifique-se de que a lista não esteja
            em ordem alfabética.
            • Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
            elegante; basta exibi-la como uma lista Python pura.
            • Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
            lista propriamente dita.
            • Mostre que sua lista manteve sua ordem original exibindo-a.
            • Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar
            a ordem da lista original.
            • Mostre que sua lista manteve sua ordem original exibindo-a novamente.
            • Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
            que sua ordem mudou.
            • Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista
            para mostrar que ela voltou à sua ordem original.
            • Utilize sort() para mudar sua lista de modo que ela seja armazenada em
            ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
            • Utilize sort() para mudar sua lista de modo que ela seja armazenada em
            ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
''')

lista_de_locais_para_viagem = ['Japão', 'EUA', 'Uruguay', 'Egito', 'Alemanha', 'França']
print(lista_de_locais_para_viagem, " - lista_de_locais_para_viagem",)

print(sorted(lista_de_locais_para_viagem), " - sorted(lista_de_locais_para_viagem)",)
print(sorted(lista_de_locais_para_viagem, reverse=True), " - sorted(lista_de_locais_para_viagem, reverse=True)")

print(lista_de_locais_para_viagem, " - lista_de_locais_para_viagem",)

print("\n")

lista_de_locais_para_viagem.reverse()
print(lista_de_locais_para_viagem, " - lista_de_locais_para_viagem.reverse()",)
lista_de_locais_para_viagem.reverse()
print(lista_de_locais_para_viagem, " - lista_de_locais_para_viagem.reverse()",)

print("\n")

lista_de_locais_para_viagem.sort()
print(lista_de_locais_para_viagem, " - lista_de_locais_para_viagem.sort()",)
lista_de_locais_para_viagem.sort(reverse=True)
print(lista_de_locais_para_viagem, " - lista_de_locais_para_viagem.sort(reverse=True)",)
