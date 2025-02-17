#Exercício 10: Modifique o seu programa do Exercício 6.2 (página 147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
#apresente o nome de cada pessoa, juntamente com seus números favoritos.

favoritenumbers = {'Clarissa': [7, 8],
                   'Jorge': [1, 2],
                   'Emanuel': [9, 0],
                   'Arthur': [3, 4],
                   'Sophia': [5, 6]
                   }

for person, numbers in favoritenumbers.items():
    print(f"Os números favoritos de {person} são: {numbers}")
