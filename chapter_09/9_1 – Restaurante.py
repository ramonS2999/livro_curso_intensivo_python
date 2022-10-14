print('''
            9.1 – Restaurante: Crie uma classe chamada Restaurant. O método __init__()
            de Restaurant deve armazenar dois atributos: restaurant_name e
            cuisine_type. Crie um método chamado describe_restaurant() que mostre
            essas duas informações, e um método de nome open_restaurant() que exiba
            uma mensagem informando que o restaurante está aberto.
            Crie uma instância chamada restaurant a partir de sua classe. Mostre os
            dois atributos individualmente e, em seguida, chame os dois métodos.
''')

# --- Criando classe ---
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

