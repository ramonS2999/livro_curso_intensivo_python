print('''
            Exemplo de Funções...
''')


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extracheese')

print(f"\n{20 * '-=-'}\n")


def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print(f"\n{20 * '-=-'}\n")


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

print(f"\n{20 * '-=-'}\n")

from modolo_001 import make_pizza as mp

mp(16, 'pepperoni')
print()
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

print(f"\n{20 * '-=-'}\n")