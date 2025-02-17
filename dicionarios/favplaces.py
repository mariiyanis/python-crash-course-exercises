#Exercício 9: Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves do dicionário
#e armazene de um a três lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante,
#peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o dicionário com um laço e apresente o
#nome de cada pessoa e seus lugares favoritos.

favoriteplaces = {
    'lia': ['galinhos' 'salvador', 'lar'],
    'ria': ['campinas', 'maxaranguape', 'recife'],
    'lho': ['afonso bezerra', 'paraiba', 'extremoz']
}

for person, places in favoriteplaces.items():
    print("Os lugares favoritos de " + person + " são:")
    for place in places:
        print(place)
    print()
