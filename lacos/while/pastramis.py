#Exercício 4: Crie uma lista chamada sandwich_orders e a preencha com os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
#finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e mostre uma mensagem para cada pedido,
#por exemplo, Preparei seu sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
#sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
#mensagem que liste cada sanduíche preparado.

pedidosanduiche = ['big mac', 'pastrami', 'rodeio duplo', 'whopper', 'pastrami', 'pitts lanche', 'sertanejo', 'pastrami']
print(pedidosanduiche)
print("A lanchonete está sem pastramis.")

while 'pastrami' in pedidosanduiche:
    pedidosanduiche.remove('pastrami')

print(pedidosanduiche)
