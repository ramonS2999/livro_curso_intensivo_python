print('''
            5.13 – Suas ideias: A essa altura, você é um programador mais capacitado do
            que era quando começou a ler este livro. Agora que você tem melhor noção de
            como situações do mundo real são modeladas em programas, talvez esteja
            pensando em alguns problemas que poderia resolver com seus próprios
            programas. Registre qualquer ideia nova que tiver sobre problemas que você
            queira resolver à medida que suas habilidades em programação continuam a
            melhorar. Considere jogos que você queira escrever, conjuntos de dados que
            possa querer explorar e aplicações web que gostaria de criar.
''')

print("Um sistema para calcular estatística.")

dicionario_dos_valores_ponderado = {}
lista_dos_valores = []


def saber_se_e_numererico(valor):
    lista_numerico = valor.split(".")
    quantidade_de_pontos = valor.count(".")

    if quantidade_de_pontos == 1:
        if lista_numerico[1] != None:
            if lista_numerico[1].isdigit():
                if lista_numerico[0].isdigit():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif quantidade_de_pontos == 0:
        if valor.isdigit():
            return True
        else:
            return False
    else:
        return False


def media_aritimedica_poderada(dicionario):
    somatorio = 0

    for chave, valor in dicionario.items():
        somatorio += chave * valor

    media_ponderada = somatorio / sum(dicionario.values())
    return media_ponderada


def media_aritimedica_simples(lista):
    media = sum(lista) / len(lista)
    return media


def solicita_valor_ponderado():
    print("Para sair aperte: N:")
    while True:
        valor = str(input(f"Informe o valor: ")).strip()

        if valor.upper() == 'N':
            break

        peso = str(input(f"Informe o peso: ")).strip()

        if peso.upper() == 'N':
            break
        elif saber_se_e_numererico(valor) and saber_se_e_numererico(peso):
            dicionario_dos_valores_ponderado[float(valor)] = float(peso)
        else:
            print('Verifique os dados, se são todos numericos...')


def solicita_valor_simples():
    print("Para sair aperte: N:")
    while True:
        valor = str(input(f"Informe o valor: ")).strip()

        if valor.upper() == 'N':
            break

        if saber_se_e_numererico(valor):
            lista_dos_valores.append(float(valor))
        else:
            print('Verifique o dado, se é numericos...')


def desvio_padrao(variancia):
    return variancia ** (1 / 2)


def variancia(media, opcao):
    somatorio_da_varianca = 0
    if opcao == 'S':
        for i in lista_dos_valores:
            if i > media:
                somatorio_da_varianca += (i - media) ** 2
            else:
                somatorio_da_varianca += (media - i) ** 2
        variancia = somatorio_da_varianca / len(lista_dos_valores)

    elif opcao == 'P':
        for i in dicionario_dos_valores_ponderado.values():
            if i > media:
                somatorio_da_varianca += (i - media) ** 2
            else:
                somatorio_da_varianca += (media - i) ** 2
        variancia = somatorio_da_varianca / sum(dicionario_dos_valores_ponderado.values())

    return variancia


while True:
    opcao = input('''
            Informe a opção:
            Para média SIMPLIES digite: S
            Para média PONDERADA digite: P
            Para sair aperte: N
                                        -> ''')

    if opcao.upper() == 'S':
        print('''
                MÉDIA SIMPLES!
            ''')
        solicita_valor_simples()
        media = media_aritimedica_simples(lista_dos_valores)
        variancia = variancia(media, opcao.upper())
        desvio_padrao = desvio_padrao(variancia)
        tipo_da_meida = 'Simples'
        break

    elif opcao.upper() == 'P':
        print('''
                MÉDIA PONDERA!
            ''')
        solicita_valor_ponderado()
        media = media_aritimedica_poderada(dicionario_dos_valores_ponderado)
        variancia = variancia(media, opcao.upper())
        desvio_padrao = desvio_padrao(variancia)
        tipo_da_meida = 'Ponderada'
        break

    elif opcao.upper() == 'N':
        print('''                FIM''')
        break

    else:
        print('''                Opção invalida...''')

if opcao.upper() != 'N':
    print(f"Media {tipo_da_meida}: {media:.2f}, Variancia: {variancia:.4f}, Desvio Padrão: {desvio_padrao:.6f}!")