print('''
            9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva
            uma classe chamada IceCreamStand que herde da classe Restaurant escrita no
            Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer
            versão da classe funcionará; basta escolher aquela de que você mais gosta.
            Adicione um atributo chamado flavors que armazene uma lista de sabores de
            sorvete. Escreva um método para mostrar esses sabores. Crie uma instância de
            IceCreamStand e chame esse método.
''')

# --- Importando classe Restaurant ---
from restaurant import Restaurant

# --- criando a classe IceCreamStand ---
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['baunilha', 'chocolate', 'morango', 'castanha']

    # --- Método que retorna o valor de 'flavors' ---
    def get_flavors(self):
        return self.flavors

# --- Criando instância de IceCreamStand ---
ice_cream = IceCreamStand('zé sorvete', 'sorveteria')

# --- Mostrando um sabor por vez ---
for sabor in ice_cream.get_flavors():
    print(sabor)
