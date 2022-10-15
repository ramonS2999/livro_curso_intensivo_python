cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print (cars, "Mostra a lista ordenada.") # Mostra a lista ordenada.

cars.sort(reverse=True) # Mostra a lista ordenada reversa.
print(cars, "Mostra a lista ordenada reversa.")

print('\n')

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(sorted(cars), "Mostra a lista temporariamente ordenada.") # Mostra a lista temporariamente ordenada.
print(sorted(cars, reverse=True), "Mostra a lista temporariamente ordenada reversa.") # Mostra a lista temporariamente ordenada reversa.
print(cars, "A lista continua Original.") # A lista continua Original.

print('\n')

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()  # Ele simplesmente inverte a ordem da lista.
print(cars)
