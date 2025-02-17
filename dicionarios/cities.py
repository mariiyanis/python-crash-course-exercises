#Exercício 11: Crie um dicionário chamado cities. Use os nomes de três cidades como chaves em seu dicionário.
#Crie um dicionário com informações sobre cada cidade e inclua o país em que a cidade está localizada, a população
#aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
#devem ser algo como country, population e fact. Apresente o nome de cada
#cidade e todas as informações que você armazenou sobre ela.

cities = {
    'Natal': {
        'country': 'Brasil',
        'population': 1000000,
        'fact': 'Primeira cidade que os portugueses invadiram.'
    },
    'Tokyo': {
        'country': 'Japão',
        'population': 13960000,
        'fact': 'Maior área metropolitana do mundo.'
    },
    'Paris': {
        'country': 'França',
        'population': 2161000,
        'fact': 'Famosa pela Torre Eiffel.'
    }
}

for city, info in cities.items():
    print("Cidade: " + city)
    print("Pais: " + info['country'])
    print("Fact: " + info['fact'])
