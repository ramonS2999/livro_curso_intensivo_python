print('''
            9.8 – Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
            atributo privileges que armazene uma lista de strings conforme descrita no
            Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie
            uma instância de Privileges como um atributo da classe Admin. Crie uma nova
            instância de Admin e use seu método para exibir os privilégios.
            
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