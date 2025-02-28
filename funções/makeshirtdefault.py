#Exercício 4: Modifique a função make_shirt() de modo que as camisetas sejam grandes por default, com uma mensagem Eu amo Python.
#Crie uma camiseta grande e outra média com a mensagem default, e uma camiseta de qualquer tamanho com uma mensagem diferente.

def make_shirt(tamanho='grande', mensagem='Eu amo Python!'):
    """ Exibe o tamanho da camisa e uma mensagem """
    print(f"O tamanho da camisa é: {tamanho} e a mensagem é: {mensagem}.")

make_shirt()

make_shirt(tamanho='média')

make_shirt(tamanho='pequena', mensagem='Python é demais!')
