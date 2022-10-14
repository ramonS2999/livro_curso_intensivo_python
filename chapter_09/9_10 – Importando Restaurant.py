print('''
            9.10 – Importando Restaurant: Usando sua classe Restaurant mais recente,
            armazene-a em um módulo. Crie um arquivo separado que importe Restaurant.
            Crie uma instância de Restaurant e chame um de seus métodos para mostrar
            que a instrução import funciona de forma apropriada.
''')

# --- Importando classe User ---
from restaurant import Restaurant

# --- Criando as instâncias ---
restaurant = Restaurant('panpa gaucho', 'churascaria')
restaurant2 = Restaurant('le café', 'padaria')

restaurant.describe_restaurant()
print(20*"-")
restaurant.open_restaurant()
restaurant.set_number_served(5)
restaurant.increment_number_served(2)
restaurant.describe_restaurant()
print()

restaurant2.describe_restaurant()
print(20*"-")
restaurant2.open_restaurant()
restaurant2.set_number_served(3)
restaurant2.increment_number_served(3)
restaurant2.describe_restaurant()
print()