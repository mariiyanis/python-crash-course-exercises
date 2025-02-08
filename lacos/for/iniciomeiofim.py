#Exercício 10: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte:
#Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
#Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.
#Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.

animais = ['Aves', 'Mamíferos', 'Aracnideos', 'Felídeos', 'Répteis']
print("Os três primeiros itens da lista são:")
print(animais[:3])

print("\nOs três itens do meio da lista são:")
print(animais[1:4])

print("\nOs três últimos itens da lista são:")
print(animais[-3:])
