requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}.")
        print("\nFinished making your pizza!")
else:
    print(f"Are you sure you want a plain pizza?")

print(f"\n{50*' = '}\n")

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
else:
    print(f"Are you sure you want a plain pizza?")
print("\nFinished making your pizza!")