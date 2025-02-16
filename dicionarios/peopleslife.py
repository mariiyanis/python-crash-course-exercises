#Exercício 7: Comece com o programa que você escreveu no Exercício 6.1 (página 147).
#Crie dois novos dicionários que representem pessoas diferentes e armazene os três dicionários
#em uma lista chamada people. Percorra sua lista de pessoas com um laço.
#À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa.

tarsoslife = {
    'first_name': 'tarso',
    'last_name': 'bittencourt',
    'age': '39',
    'city': 'Manhattan'
}

reginaslife = {
    'first_name': 'regina',
    'last_name': 'lima',
    'age': 39,
    'city': 'Madrid'
}

eduardoslife = {
    'first_name': 'eduardo',
    'last_name': 'macedo',
    'age': 40,
    'city': 'Toronto'
}

people = [tarsoslife, reginaslife, eduardoslife]
for person in people:
    print("Nome Completo: " + person['first_name'] + " " + person['last_name'])
    print("Idade: " + str(person['age']) + " anos")
    print("Cidade: " + person['city'])
