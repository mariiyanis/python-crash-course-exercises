#Exercício 13: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida.
#Pense em cinco pratos simples e armazene-os em uma tupla.
#Use um laço for para exibir cada prato oferecido pelo restaurante.
#Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
#O restaurante muda seu cardápio, substituindo dois dos itens com pratos diferentes.
#Acrescente um bloco de código que reescreva a tupla e, em seguida, use um laço for para exibir cada um dos itens do cardápio revisado.

buffet = ('Camarão ao molho branco', 'Strogonoff de Frango', 'Crispy Sushi', 'Filé Mignon', 'Temaki hot Sallmão Fresco')
for comida in buffet:
    print(comida)

buffet = ('Camarão ao molho branco', 'Strogonoff de Frango', 'Crispy Sushi', 'Arroz e Feijão', 'Cuscuz com leite de coco')
for comida in buffet:
    print(comida)
