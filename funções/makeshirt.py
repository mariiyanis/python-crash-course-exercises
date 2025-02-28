#Exercício 3: Escreva uma função chamada make_shirt() que aceite um tamanho e o texto de uma mensagem que deverá ser estampada
#na camiseta. A função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem estampada.
#Chame a função uma vez usando argumentos posicionais para criar uma camiseta.
#Chame a função uma segunda vez usando argumentos nomeados.

def make_shirt(tamanho, mensagem):
    """ Exibe o tamanho da camiseta e uma mensagem """
    print(f"O tamanho da camisa é: {tamanho} e a mensagem é: {mensagem}.")

make_shirt('médio', 'Arrasou!!')
make_shirt(tamanho='grande', mensagem='Arrasastes!!')
