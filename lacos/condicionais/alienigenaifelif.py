#Exercício 5: Transforme sua cadeia if-else do Exercício 5.4 em uma cadeia if-elif-else.
#Se o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos.
#Se o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos.
#Se o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos.
#Escreva três versões desse programa, garantindo que cada mensagem seja exibida para a cor apropriada do alienígena.
cor_alienigena = 'Amarelo'
if cor_alienigena == 'Verde':
    print("O jogador acabou de ganhar cinco pontos!")
elif cor_alienigena == 'Amarelo':
    print("O jogador acabou de ganhar dez pontos!")
elif cor_alienigena == 'Vermelho':
    print("O jogador acabou de ganhar quinze pontos!")

cor_alienigena = 'Verde'
if cor_alienigena == 'Verde':
    print("O jogador acabou de ganhar cinco pontos!")
elif cor_alienigena == 'Amarelo':
    print("O jogador acabou de ganhar dez pontos!")
elif cor_alienigena == 'Vermelho':
    print("O jogador acabou de ganhar quinze pontos!")

cor_alienigena = 'Vermelho'
if cor_alienigena == 'Verde':
    print("O jogador acabou de ganhar cinco pontos!")
elif cor_alienigena == 'Amarelo':
    print("O jogador acabou de ganhar dez pontos!")
elif cor_alienigena == 'Vermelho':
    print("O jogador acabou de ganhar quinze pontos!")
