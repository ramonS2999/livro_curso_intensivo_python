print('''
            9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à
            sua classe User do Exercício 9.3 (página 226). Escreva um método chamado
            increment_login_attempts() que incremente o valor de login_attempts em 1.
            Escreva outro método chamado reset_login_attempts() que reinicie o valor de
            login_attempts com 0.
            Crie uma instância da classe User e chame increment_login_attempts()
            várias vezes. Exiba o valor de login_attempts para garantir que ele foi
            incrementado de forma apropriada e, em seguida, chame
            reset_login_attempts(). Exiba login_attempts novamente para garantir que
            seu valor foi reiniciado com 0.
''')

# --- criando a clsasse User ---
class User():
    def __init__(self, first_name, last_name, age, sexo):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sexo = sexo
        self.login_attempts = 0
    
    def describe_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Nome completo: {full_name.title()}")
        print(f"Idade: {self.age}")
        print(f"Sexo: {self.sexo.title()}")
        print(f"Login: {self.login_attempts}")
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Olá {full_name.title()}, prazer em ter você aqui!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User(first_name='luis', last_name='lima', sexo='mascolino', age=31)

print(20*'-=-')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.greet_user()
print()
user1.describe_user()
user1.reset_login_attempts()
print()
user1.describe_user()

print(20*'-=-')
