# Você tem a seguinte lista de produtos, cada um representado como uma tupla com (produto, preço unitário, quantidade): produtos = [ ("Maçã", 3.50, 4), ("Leite", 4.20, 2), ("Pão", 2.50, 6), ("Ovos", 0.80, 12) ] Tarefa: Crie um programa que percorra a lista de tuplas. Para cada produto, calcule o preço total (preço unitário × quantidade). Exiba na tela uma lista mostrando: Nome do produto Quantidade Preço unitário Preço total do produto Dica: você pode usar um loop for para percorrer a lista de tuplas.
# produtos = [ ("Maçã", 3.50, 4), ("Leite", 4.20, 2), ("Pão", 2.50, 6), ("Ovos", 0.80, 12) ]
# for p, preço, q in produtos:
#     valor_total = preço * q
#     print(f'''
# o produto é {p}
# a quantidade é {q}
# o valor unitário é {preço}
# e o valor total é {valor_total:.2f}
#       ''')


# Você recebeu um pequeno texto e precisa analisar a frequência das palavras e identificar quais são únicas. texto = "maçã banana laranja maçã pera banana laranja laranja" Tarefas: Crie uma função chamada contar_palavras que receba o texto como string e retorne um dicionário onde: a chave é a palavra o valor é a quantidade de vezes que a palavra aparece no texto Crie uma função chamada palavras_unicas que receba o dicionário e retorne um set contendo apenas as palavras que aparecem uma única vez no texto. Imprima o dicionário de contagem e o set de palavras únicas. Dica: Para criar o set de palavras únicas, percorra o dicionário e selecione apenas as palavras cujo valor seja 1.
# texto = "maçã banana laranja maçã pera banana laranja laranja"
# palavra=''
# quantidade = 0 
# def contar_palavras(texto):
#     palavra = texto.split()
#     return {p: palavra.count(p) for p in set(palavra)}
# def palavras_unicas(dic):
#     return{p for p, contador in dic.items() if contador ==1 }
# contador = contar_palavras(texto)
# unicas = palavras_unicas (contador)
# print(contador)
# print(unicas)




# Crie uma função que recebe uma lista de números e retorna uma nova lista apenas com os números pares, usando uma função normal e depois usando uma função lambda com filter. Exemplo de lista de números: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# from os import remove


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def informarções(dados, transformar):
#     return [transformar(dado) for dado in dados]
# def numeros_pares(elemento):
#     numero_impar = elemento % 2 != 0
#     if elemento % 2 == 0:
#         return elemento
#     else:
#        return elemento.remove(numero_impar)

# print(informarções(lista, numeros_pares))
# numeros_pares1 = list(filter(lambda x:x % 2 == 0, lista))
# print(numeros_pares1)


def transformar_lista(lista):
    return [x for x in lista if x % 2 == 0]
    # nova_lista = []

    # for num in lista:
    #     if num % 2 == 0:
    #         resultado = num
    #         nova_lista.append(resultado)
    
    # return nova_lista
print(transformar_lista(lista))