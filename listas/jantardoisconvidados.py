#Exercício7: Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.
#Comece com seu programa do Exercício 3.6.
#Acrescente uma nova linha que mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.
#Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em sua lista.
#Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por
#não poder convidá-la para o jantar.
#Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda estão convidadas.
#Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia.
#Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu programa.

encontro = ['Luedji Luna', 'Liniker', 'Barry White', 'Prince', 'Whitney', 'Elza Soares']
print("Gente, tive um imprevisto seríssimo e não vou conseguir receber todos aqui. Peço perdão.")

encontro.pop(0)
encontro.pop(0)
encontro.pop(0)
encontro.pop(-1)
print(encontro)

del encontro[0], encontro[-1]
print(encontro)
