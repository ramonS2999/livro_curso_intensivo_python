
numeros = list(range(1, 6))
print(f"{numeros} - lista de número feita pela função range()")

numeros_pares = list(range(2, 11, 2))
print(f"{numeros_pares} - Lista de número pares feita pela função range()")

numeros_impares = list(range(1, 10, 2))
print(f"{numeros_impares} - Lista de número impares feita pela função range()")

lista_de_quadrados_perfeitos = []
for valor in range(1, 11):
    lista_de_quadrados_perfeitos.append(valor**2)
print(f"{lista_de_quadrados_perfeitos}  Mostrando o quadrado perfeito de cada número de 1 a 10") # Mostrando o quadrado perfeito de cada número de 1 a 10

lista_de_quadrados_perfeitos_COMPREHENSIONS = [valor**2 for valor in range(1, 11)]
print(f"{lista_de_quadrados_perfeitos_COMPREHENSIONS}  Mostrando o quadrado perfeito de cada número de 1 a 10 - usnado COMPREHENSIONS")