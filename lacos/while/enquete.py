#Exercício 6: Escreva um programa que faça uma enquete sobre as férias dos sonhos dos usuários.
#Escreva um prompt semelhante a este: Se pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
#apresente os resultados da enquete.

respostas = {}

enqueteativa = True
while enqueteativa:
    nome = input("Nome: ")
    resposta = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")

    respostas[nome] = resposta

    repeat = input("Quer que outra pessoa responda por você? (Digite: sim ou não) ")
    if repeat.lower() == 'não':
        enqueteativa = False
    else:
        continue

print("\n --- Resultados da Enquete ---")
for nome, resposta in respostas.items():
    print(f"{nome} gostaria de ir a {resposta}.")
