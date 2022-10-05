print('''
            9.14 – Dados: O módulo random contém funções que geram números aleatórios
            de várias maneiras. A função randint() devolve um inteiro no intervalo
            especificado por você. O código a seguir devolve um número entre 1 e 6: from
            random import randint x = randint(1, 6)
            Crie uma classe Die com um atributo chamado sides, cujo valor default é 6.
            Escreva um método chamado roll_die() que exiba um número aleatório entre
            1 e o número de lados do dado. Crie um dado de seis dados e lance-o dez
            vezes.
            Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez
            vezes.
''')

# --- Começamos importando a função randint do módulo random. ---
from random import randint

# --- criando a classe Die ---
class Die():
    def __init__(self):
        self.sides = 6 # --- inicializando o atributo sides ---
    
    # --- criando o método roll_die ---
    def roll_die(self):
        return randint(1, self.sides)
    
    def sides_die(self, side):
        self.sides = side

# --- criando as instâncias ---
dado_6_lado = Die()
dado_10_lado = Die()
dado_20_lado = Die()

print("Dado de 6 lados:\n")
for i in range(1, 11):
    print(dado_6_lado.roll_die())

print("\nDado de 10 lados:\n")
dado_10_lado.sides_die(10)
for i in range(1, 11):
    print(dado_10_lado.roll_die())

print("\nDado de 20 lados:\n")
dado_20_lado.sides_die(20)
for i in range(1, 11):
    print(dado_20_lado.roll_die())