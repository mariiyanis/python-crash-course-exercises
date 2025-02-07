#Exercício8: Pense em pelo menos cinco lugares do mundo que você gostaria de visitar.
#Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
#Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante; basta exibi-la como uma lista Python pura.
#Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.
#Mostre que sua lista manteve sua ordem original exibindo-a.
#Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.
#Mostre que sua lista manteve sua ordem original exibindo-a novamente.
#Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.
#Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.
#Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
#Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.

viagens = ['Hawaii', 'Amapá', 'Bahia', 'Galinhos', 'Genipabu']
print("Eu queria muito visitar esses lugares: " + str(viagens))

print("Essa é a lista de lugares que quero ir em ordem alfabética:")
print(sorted(viagens))

print("Agora, aqui está a lista original, sem mudança de ordem:")
print(viagens)

print("E se essa lista fosse invertida alfabeticamente?", sorted(viagens, reverse=True))

print("Certo, chega de brincadeira. Não mudei nada! Olha só:")
print(viagens)

viagens.reverse()
print("Agora, eu mudei definitivamente:")
print(viagens)

print("E como eu posso, vou colocar a ordem como estava antes!")
viagens.reverse()
print(viagens)

viagens.sort()
print(viagens)

viagens.sort(reverse=True)
print(viagens)
