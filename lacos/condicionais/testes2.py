#Exercício 2: Você não precisa limitar o número de testes que criar em dez. Se quiser testar mais comparações, escreva outros testes e
#acrescente os em conditional_tests.py. Tenha pelo menos um resultado True e um False para cada um dos casos a seguir:
#testes de igualdade e de não igualdade com strings;
#testes usando a função lower();
#testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a;
#testes usando as palavras reservadas and e or;
#testes para verificar se um item está em uma lista;
#testes para verificar se um item não está em uma lista.
print("python" == "python")
print("python" != "java")

# Testes usando a função lower()
print("HELLO".lower() == "hello")
print("HELLO".lower() != "HELLO")

# Testes numéricos: igualdade, não igualdade, maior, menor, maior ou igual, menor ou igual
print(5 == 5)
print(5 != 10)
print(10 > 5)
print(5 < 10)
print(10 >= 5)
print(5 <= 10)

# Testes usando as palavras reservadas and e or
print((5 > 3) and (10 > 5))
print((5 > 3) or (2 > 5))
print((5 > 3) and (10 < 5))

# Testes para verificar se um item está em uma lista
print(3 in [1, 2, 3, 4])
print(5 not in [1, 2, 3, 4])
