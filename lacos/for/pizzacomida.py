#Exercício 12: Todas as versões de foods.py nesta seção evitaram usar laços for para fazer exibições a fim de economizar espaço.
#Escolha uma versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

pizzas = ['Palha Italiana', 'Frango com Catupiry', 'Carne de Sol']

print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza)

comida = pizzas[:]
comida.append('Portuguesa')

print("\nAs pizzas favoritas de meu amigo são:")
for pizza in comida:
    print(pizza)
