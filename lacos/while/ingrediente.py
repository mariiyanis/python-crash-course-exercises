#Exercício 1: Escreva um laço que peça ao usuário para fornecer uma série de ingredientes para uma pizza
#até que o valor 'quit' seja fornecido. À medida que cada ingrediente é especificado, apresente uma
#mensagem informando que você acrescentará esse ingrediente à pizza.

while True:
    ingrediente = input("Você gostaria de adicionar algo na pizza? (Se não, digite 'quit' para encerrar): ")
    if ingrediente.lower() == 'quit':
        print("Finalizando a escolha de ingredientes.")
        break
    else:
        print(f"O ingrediente '{ingrediente}' será adicionado à pizza!")
