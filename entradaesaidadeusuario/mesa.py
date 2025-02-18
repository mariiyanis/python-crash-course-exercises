#Exercício 2: Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo para jantar.
#Se a resposta for maior que oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
#contrário, informe que sua mesa está pronta.

people = input("Quantas pessoas irão jantar convosco?")
people = int(people)

if people > 8:
    print("\nEsperem uma mesa ficar livre para comportar todos.")
else:
    print("\nA mesa de vocês está pronta!")
