#Exercício 3: Escreva versões diferentes do Exercício 7.4 ou do Exercício 7.5 que faça o seguinte, pelo menos uma vez:
#use um teste condicional na instrução while para encerrar o laço;
#use uma variável active para controlar o tempo que o laço executará;
#use uma instrução break para sair do laço quando o usuário fornecer o valor 'quit'.

active = True
while active:
    ingrediente = input("Você gostaria de adicionar algo na pizza? (Se não, digite 'quit' para encerrar): ")
    if ingrediente.lower() == 'quit':
        print("Finalizando a escolha de ingredientes.")
        active = False
    else:
        print(f"O ingrediente '{ingrediente}' será adicionado à pizza!")
