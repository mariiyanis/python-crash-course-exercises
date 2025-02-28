#Exercício 6: : Escreva uma função chamada city_country() que aceite o nome de uma cidade e seu país.
#A função deve devolver uma string formatada assim: "Santiago, Chile"
#Chame sua função com pelo menos três pares cidade-país e apresente o valor devolvido.

def city_country(cidade, pais):
    """ Exibe o nome de uma cidade e seu país """
    print(f"{cidade}, {pais}")

city_country('Lyon', 'França')
city_country('Roma', 'Italia')
city_country('Amsterdam', 'Holanda')
