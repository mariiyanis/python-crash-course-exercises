#Exercício 8: Comece com o seu programa do Exercício 8.7. Escreva um laço while que permita aos usuários fornecer o nome
#de um artista e o título de um álbum. Depois que tiver essas informações, chame make_album() com
#as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um valor de saída no laço while.

def make_album(artista, titulo, faixa=''):
    """ Constrói um dicionário contendo informações sobre um álbum musical. """
    album = {'artista': artista.title(), 'titulo': titulo.title()}
    if faixa:
        album['faixa'] = faixa
    return album

while True:
    print("\nDigite as informações do álbum (ou digite 'sair' para encerrar).")

    artista = input("Nome do artista: ")
    if artista.lower() == 'sair':
        break

    titulo = input("Título do álbum: ")
    if titulo.lower() == 'sair':
        break

    faixa = input("Número de faixas (pressione Enter para pular): ")
    if faixa.lower() == 'sair':
        break

    #Convertendo faixa para int
    faixa = int(faixa) if faixa.isdigit() else None

    album = make_album(artista, titulo, faixa)
    print("\nÁlbum criado:", album)
