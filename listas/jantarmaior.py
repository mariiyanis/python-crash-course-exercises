#Exercício 6: Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível.
#Pense em mais três convidados para o jantar.
#Comece com seu programa do Exercício 3.4 ou do Exercício 3.5.
#Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.
#Utilize insert() para adicionar um novo convidado no início de sua lista.
#Utilize insert() para adicionar um novo convidado no meio de sua lista.
#Utilize append() para adicionar um novo convidado no final de sua lista.
#Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.

encontro = ['Liniker', 'Prince', 'Whitney']
print("Gente, naquele canto perto da janela tem outra mesa com mais cadeiras do que nessa em que estamos. Vamos?")

encontro.insert(0, 'Luedji Luna')
encontro.insert(2, 'Barry White')
encontro.append('Elza Soares')

convite4 = "Olá, " + encontro[0] + "! " + "Tudo bem? Você gostaria de tomar um cafezinho da tarde vendo o pôr do sol de Genipabu? Me mande uma resposta. Xêro!"
convite5 = "Olá, " + encontro[2] + "! " + "Tudo bem? Você gostaria de tomar um cafezinho da tarde vendo o pôr do sol de Genipabu? Me mande uma resposta. Xêro!"
convite6 = "Olá, " + encontro[-1] + "! " + "Tudo bem? Você gostaria de tomar um cafezinho da tarde vendo o pôr do sol de Genipabu? Me mande uma resposta. Xêro!"

print(convite4)
print(convite5)
print(convite6)
print(encontro)
