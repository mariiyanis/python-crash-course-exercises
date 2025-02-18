#Exercício 3: Peça um número ao usuário e, em seguida, informe se o número é múltiplo de dez ou não.

number = input("Me informe um número")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} é um múltiplo de 10!")
else:
    print(f"\n{number} não é um múltiplo de 10.")
