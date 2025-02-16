#Exercício 5: Crie um dicionário que contenha três rios importantes e o país que cada rio corta.
#Um par chave-valor poderia ser 'nilo': 'egito'.
#Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.
#Use um laço para exibir o nome de cada rio incluído no dicionário.
#Use um laço para exibir o nome de cada país incluído no dicionário.

rios = {
    'Amazonas': 'Brasil',
    'Nilo': 'Egito',
    'Yangtze': 'China'
}

for rio in rios:
    print("O rio " + rio + " corre pelo " + rios[rio] + ".")

for rio in rios.keys():
    print(rio)

for pais in rios.values():
    print(pais)
