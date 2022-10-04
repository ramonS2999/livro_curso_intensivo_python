print('''
            9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
            instâncias diferentes da classe e chame describe_restaurant() para cada
            instância.
''')

# --- importando os módolos ---
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Nome: {self.restaurant_name.title()}")
        print(f"Tipo: {self.cuisine_type.title()}")
    
    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name.title()}, está aberto.")

restaurant1 = Restaurant("lá casa", "churascaria")
restaurant2 = Restaurant("canto do gordo", "lanchonete")
restaurant3 = Restaurant("bueiro dos ratos", "selves-service")


restaurant1.describe_restaurant()
restaurant1.open_restaurant()
print()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()
print()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

