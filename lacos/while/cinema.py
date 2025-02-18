#Exercício 2: Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
#anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso custará 10 dólares;
#se tiver mais de 12 anos, o ingresso custará 15 dólares. Escreva um laço em que você pergunte a idade aos usuários e,
#então, informe-lhes o preço do ingresso do cinema.

while True:
    idade = input("Quantos anos você tem? (ou digite 'quit' para encerrar): ")

    if idade.lower() == 'quit':
        print("Fechando a compra.")
        break

    # Converte a entrada para int
    idade = int(idade)

    if idade < 3:
        print("O ingresso é gratuito!")
    elif idade <= 12:
        print("O ingresso custa R$ 10!")
    else:
        print("O ingresso custa R$ 15!")
