#Exercício 8: Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação.
#Em cada dicionário, inclua o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista chamada pets.
#Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente tudo que você sabe sobre cada animal de estimação.

coelhete = {
    'tipodeanimal': 'cachorro',
    'nomedodono': 'waki'
}

chica = {
    'tipodeanimal': 'gato',
    'nomedodono': 'nia'
}

ozzy = {
    'tipodeanimal': 'lobo',
    'nomedodono': 'bunny'
}

pets = [coelhete, chica, ozzy]
for pet in pets:
    print("Tipo de animal: " + pet['tipodeanimal'])
    print("Nome do dono: " + pet['nomedodono'])
