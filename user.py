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