print('''
            5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba uma
            frase que descreva o teste e o resultado previsto para cada um. Seu código
            deverá ser semelhante a: car = 'subaru'
            print("Is car == 'subaru'? I predict True.") print(car == 'subaru')
            print("\\nIs car == 'audi'? I predict False.") print(car == 'audi') •
            Observe atentamente seus resultados e certifique-se de que compreende
            por que cada linha é avaliada como True ou False.
            • Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como
              True e outros cinco avaliados como False.
''')

car = 'subaru'

print(f"Is car == 'subaru'? I predict {car == 'subaru'}.")
print(f"Is car != 'audi'? I predict {car != 'audi'}.")
print(f"Is car == 'SUBARU'.lower()? I predict {car == 'SUBARU'.lower()}.")
print(f"Is car != 'audi'? I predict {car != 'audi'}.")
print(f"Is car.title == 'Subaru'? I predict {car.title() == 'Subaru'}.")

print("\n")

print(f"Is car != 'subaru'? I predict {car != 'subaru'}.")
print(f"Is car == 'audi'? I predict {car == 'audi'}.")
print(f"Is car != 'SUBARU'.lower()? I predict {car != 'SUBARU'.lower()}.")
print(f"Is car == 'audi'? I predict {car == 'audi'}.")
print(f"Is car.title != 'Subaru'? I predict {car.title() != 'Subaru'}.")

