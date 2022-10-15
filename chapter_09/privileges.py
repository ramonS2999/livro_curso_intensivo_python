# --- criando a classe Admin ---
class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    # --- Método que retorna o valor de 'show_privileges' ---
    def show_privileges(self):
        for privilejo in self.privileges:
            print(privilejo)

