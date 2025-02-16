#Exercício 6: Utilize o código em favorite_languages.py (página 150).
#Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita.
#Inclua alguns nomes que já estejam no dicionário e outros que não estão.
#Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete,
#mostre uma mensagem agradecendo-lhes por responder. Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

new_people = ['jen', 'sarah', 'edward', 'phil', 'Marília', 'Clara', 'Larissa', 'Santos']
for person in new_people:
    if person in favorite_languages:
        print("Obrigada por ter respondido a enquete, " + person + "!")
    else:
        print("Por favor, responda a enquete, " + person + "!")
