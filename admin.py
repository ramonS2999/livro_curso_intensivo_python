# --- Importando classe User ---
from user import User
from privileges import Privileges

# --- criando a classe Admin ---
class Admin(User):
    def __init__(self, first_name, last_name, age, sexo):
        super().__init__(first_name, last_name, age, sexo)
        self.privileges = Privileges()