#Exercício 4: Crie uma lista chamada sandwich_orders e a preencha com os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
#finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e mostre uma mensagem para cada pedido,
#por exemplo, Preparei seu sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
#sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
#mensagem que liste cada sanduíche preparado.

pedidosanduiche = ['big mac', 'rodeio duplo', 'whopper', 'pitts lanche', 'sertanejo']
sanduichefinalizado = []

while pedidosanduiche:
    sanduiche = pedidosanduiche.pop()
    print(f"Preparei seu sanduiche de {sanduiche}")
    sanduichefinalizado.append(sanduiche)

print("\nOs sanduíches finalizados são esses: ")
for sanduiches in sanduichefinalizado:
    print(sanduiches.title())
