print('''

            7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
            férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
            pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
            código que apresente os resultados da enquete.
''')

ferias_dos_sonhos = {}

print(" --- FÉRIAS DOS SONHOS --- ")

active = True
while active:
    nome = input("Informe seu nome: ")
    lugar = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")
    opcao = input("Para continuar digiete (y/n): ")
    ferias_dos_sonhos[nome] = lugar
    if opcao == 'n':
        active = False

for nome, lugar in ferias_dos_sonhos.items():
    print(f"{nome.title()} gostaria de passar as suas férias em {lugar.title()}.")
