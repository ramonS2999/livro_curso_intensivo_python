print('''
        2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
        pessoa e inclua alguns caracteres em branco no início e no final do nome.
        Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos
        uma vez.
''')

famous_person = "\n\tMartin Luther King\t\n"

print(f"Apresentando a variável original: {famous_person}")
print(f"Removendo caracteres em branco lado esquerdo: {famous_person.lstrip()}")
print(f"Removendo caracteres em branco lado direito: {famous_person.rstrip()}")
print(f"Removendo caracteres em branco todos os lados: {famous_person.strip()}")
