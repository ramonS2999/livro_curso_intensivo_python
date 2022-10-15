def make_pizza(size, *toppings):
    print(f"Making a {str(size)}-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

def build_profile(nome, sobrenome, **descricao):
    nome_completo = nome + ' ' + sobrenome
    print(f'Nome - {nome_completo.title()}')
    for key, value in descricao.items():
        print(f"{str(key).title()} - {str(value).title()}")


