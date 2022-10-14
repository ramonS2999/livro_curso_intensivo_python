print('''
            9.12 – Vários módulos: Armazene a classe User em um módulo e as classes
            Privileges e Admin em um módulo separado. Em outro arquivo, crie uma
            instância de Admin e chame show_privileges() para mostrar que tudo continua
            funcionando de forma apropriada.
''')

# --- Importando classe Admin ---
from admin import Admin

# --- Criando instância de IceCreamStand ---
admin = Admin('raimundo', 'soldado', 50, 'masculino')

admin.privileges.show_privileges()