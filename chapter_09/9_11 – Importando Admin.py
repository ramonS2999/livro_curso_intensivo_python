print('''
            9.11 – Importando Admin: Comece com seu programa do Exercício 9.8 (página
            241). Armazene as classes User, Privileges e Admin em um módulo. Crie um
            arquivo separado e uma instância de Admin e chame show_privileges() para
            mostrar que tudo está funcionando de forma apropriada.
''')

# --- Importando classe Admin ---
from admin import Admin

# --- Criando instância de IceCreamStand ---
admin = Admin('raimundo', 'soldado', 50, 'masculino')

admin.privileges.show_privileges()