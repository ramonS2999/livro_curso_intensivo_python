print('''
            9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
            first_name e last_name e, então, crie vários outros atributos normalmente
            armazenados em um perfil de usuário. Escreva um método de nome
            describe_user() que apresente um resumo das informações do usuário. Escreva
            outro método chamado greet_user() que mostre uma saudação personalizada
            ao usuário.
            Crie várias instâncias que representem diferentes usuários e chame os dois
            métodos para cada usuário.
''')

# --- criando a clsasse User ---
class User():
    def __init__(self, first_name, last_name, age, sexo):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sexo = sexo
    
    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Nome completo: {full_name.title()}")
        print(f"Idade: {self.age}")
        print(f"Sexo: {self.sexo.title()}")
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Olá {full_name.title()}, prazer em ter você aqui!")

user1 = User(first_name='luis', last_name='lima', sexo='mascolino', age=31)
user2 = User(first_name='ramon', last_name='silva', sexo='mascolino', age=25)
user3 = User(first_name='ana', last_name='alice', sexo='feminino', age=23)
user4 = User(first_name='maria', last_name='eduarda', sexo='feminino', age=21)

print(20*'-=-')
user1.greet_user()
print()
user1.describe_user()

print(20*'-=-')

user2.greet_user()
print()
user2.describe_user()

print(20*'-=-')

user3.greet_user()
print()
user3.describe_user()

print(20*'-=-')

user4.greet_user()
print()
user4.describe_user()

print(20*'-=-')