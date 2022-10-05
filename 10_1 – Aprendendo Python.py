print('''
            10.1 – Aprendendo Python: Abra um arquivo em branco em seu editor de texto e
            escreva algumas linhas que sintetizem o que você aprendeu sobre Python até
            agora. Comece cada linha com a expressão Em Python podemos.... Salve o
            arquivo como learning_python.txt no mesmo diretório em que estão seus
            exercícios deste capítulo. Escreva um programa que leia o arquivo e mostre o
            que você escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo,
            uma vez percorrendo o objeto arquivo com um laço e outra armazenando as
            linhas em uma lista e então trabalhando com ela fora do bloco with.
''')

filename = "learning_python.txt"
lista = []
with open(filename) as file_object:
    
    print("DENTRO DO BLOCO 'with'")
    print(50*" =")
    lines = file_object.readlines()
    print(lines)
    print(50*" =")

    for line in lines:
        print(line.rstrip())
        lista.append(line.rstrip())
    print(50*" =")

print("\n\nFORA DO BLOCO 'with'")
for line in lista:
    print(line)
print(50*" =")

    
 