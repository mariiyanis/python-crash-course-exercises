#Exercício 2: Escreva uma função chamada favorite_book() que aceite um parâmetro title. A função deve exibir uma mensagem
#como Um dos meus livros favoritos é Alice no país das maravilhas. Chame a função e não se esqueça de incluir
#o título do livro como argumento na chamada da função.

def favorite_book(title):
    """ Exibe uma mensagem sobre os nossos livros favoritos """
    print(f"Um dos meus livros favoritos é {title.title()}.")

favorite_book('Os Sete Maridos de Evelyn Hugo')
