#Exercício 4: Agora que você já sabe como percorrer um dicionário com um laço, limpe o código do Exercício 6.3 (página 148),
#substituindo sua sequência de instruções print por um laço que percorra as chaves e os valores do dicionário.
#Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de Python ao seu glossário.
#Ao executar seu programa novamente, essas palavras e significados novos deverão ser automaticamente incluídos na saída.

glossario = {'lacos': 'for',
             'dicionarios': 'chave',
             'concatenar': 'adicionar',
             'listas': 'itens',
             'string': 'caracteres',
            }

for palavra in glossario:
    print("Quando lembro de " + palavra + ", me recordo de: " + glossario[palavra] + ".")
