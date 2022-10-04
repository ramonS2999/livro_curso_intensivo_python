print('''
            9.7 – Admin: Um administrador é um tipo especial de usuário. Escreva uma
            classe chamada Admin que herde da classe User escrita no Exercício 9.3
            (página 226), ou no Exercício 9.5 (página 232). Adicione um atributo
            privileges que armazene uma lista de strings como "can add post", "can
            delete post" "can ban user", e assim por diante. Escreva um método chamado
            show_privileges() que liste o conjunto de privilégios de um administrador. Crie
            uma instância de Admin e chame seu método.
''')

# --- Importando classe User ---
from user import User
from privileges import Privileges

# --- criando a classe Admin ---
class Admin(User):
    def __init__(self, first_name, last_name, age, sexo):
        super().__init__(first_name, last_name, age, sexo)
        self.privileges = Privileges()

# --- Criando instância de IceCreamStand ---
admin = Admin('raimundo', 'soldado', 50, 'masculino')

admin.privileges.show_privileges()


