# --- Criando classe ---
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nome: {self.restaurant_name.title()}")
        print(f"Tipo: {self.cuisine_type.title()}")
        print(f"Nº pedidos: {self.get_number_served()}")

    def open_restaurant(self):
        print(f"O restaurante {self.restaurant_name.title()}, está aberto.")

    def get_number_served(self):
        return self.number_served

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, client):
        self.number_served += client


