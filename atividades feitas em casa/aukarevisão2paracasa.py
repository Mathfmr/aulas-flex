# Crie uma função que receba uma lista de preços de produtos e retorne uma nova lista com os preços já com 10% de desconto. 
# Faça primeiro usando uma função normal e depois usando uma função lambda com map. Exemplo de lista de 
preços = [50.0, 120.0, 35.5, 80.0, 15.0]
# def transformar_lista (preços):
#     return [preço * 0.9 for preço in preços]




# preços_com_desconto = transformar_lista(preços)
# print("Preços com desconto usando função normal:", preços_com_desconto)

def transformar_lista(preços):
    return list(map(lambda x: x * 0.9, preços))

preços_com_desconto = transformar_lista(preços)
print("Preços com desconto usando função lambda e map:", preços_com_desconto)



