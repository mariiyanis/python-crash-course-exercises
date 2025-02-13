#Exercício 3: Um dicionário Python pode ser usado para modelar um dicionário de verdade.
#No entanto, para evitar confusão, vamos chamá-lo de glossário.
#Pense em cinco palavras relacionadas à programação que você conheceu nos capítulos anteriores.
#Use essas palavras como chaves em seu glossário e armazene seus significados como valores.
#Mostre cada palavra e seu significado em uma saída formatada de modo elegante.
#Você pode exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha
#e então exibir seu significado indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
#para inserir uma linha em branco entre cada par palavra-significado em sua saída.

glossario = {'lacos': 'for',
             'dicionarios': 'chave',
             'concatenar': 'adicionar',
             'listas': 'itens',
             'string': 'caracteres',
            }

print("Quando lembro de laços, me recordo de: " + glossario['lacos'] + ".")
print("Quando lembro de dicionários, me recordo de: " + glossario['dicionarios'] + ".")
print("Quando lembro de concatenar, me recordo de: " + glossario['concatenar'] + ".")
print("Quando lembro de listas, me recordo de: " + glossario['listas'] + ".")
print("Quando lembro de string, me recordo de: " + glossario['string'] + ".")
