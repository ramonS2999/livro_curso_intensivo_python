print('''
            4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
            de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
            • Use um laço for para exibir cada prato oferecido pelo restaurante.
            • Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
            • O restaurante muda seu cardápio, substituindo dois dos itens com pratos
              diferentes. Acrescente um bloco de código que reescreva a tupla e, em
              seguida, use um laço for para exibir cada um dos itens do cardápio
              revisado.
''')

tupla_de_pratos = ('pizza', 'feijoada', 'buchada', 'lasanha', 'macorronada')
print("Cardápio originais")
for prato in tupla_de_pratos:
    print(prato)

try:
    tupla_de_pratos[0] = 'baião de dois'
except Exception as e:
    print(f'\nO erro é esse: {repr(e)}\n')

tupla_de_pratos = ('baião de dois', 'feijoada', 'assado de panela', 'lasanha', 'macorronada')
print("Cardápio revisado")
for prato in tupla_de_pratos:
    print(prato)