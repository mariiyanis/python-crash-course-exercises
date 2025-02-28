#Exercício 9: : Crie uma lista de nomes de mágicos. Passe a lista para uma função chamada show_magicians()
#que exiba o nome de cada mágico da lista.

def show_magicians(nomes):
    """ Exibe o nome dos mágicos """
    for nome in nomes:
        print(f"Olá {nome.title()}! Seja bem vindo ao circo!")

magicos = ['marcelo', 'jonas', 'margarida', 'joaquina']
show_magicians(magicos)
