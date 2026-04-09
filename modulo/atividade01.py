produtos_iniciais = {'camiseta': 50, 'tenis': 200, 'bone': 40, 'mochila': 120, 'jaqueta': 300}

def soma_produtos(comprap, quantidade):
    valor_final = comprap * quantidade
    return valor_final

def descontos(valor_final, tipo_pagamento):
    if tipo_pagamento == 'pix':
       return valor_final * (1 - 0.1)
    elif tipo_pagamento == 'debito':
        return valor_final * (1 - 0.05)
    elif tipo_pagamento == 'credito':
        return valor_final
    else:
        print(f'O tipo de pagamento {tipo_pagamento} é invalido')
        return valor_final 

valor_unitario = {}
def processar_venda(nome_produto, quantidade, tipo_pagamento):
    if nome_produto in produtos_iniciais:
        valor_unitario[nome_produto] = produtos_iniciais[nome_produto]
        valor_total = soma_produtos(valor_unitario[nome_produto], quantidade)
        valor_com_desconto = descontos(valor_total, tipo_pagamento)
        print(f'Produto: {nome_produto} | Quantidade: {quantidade} | Pagamento: {tipo_pagamento} | Valor final: R$ {valor_com_desconto:.2f}')
    else:
        print(f'O produto {nome_produto} não está disponível.')
carrinho = {}

print(processar_venda('camiseta', 3 , 'pix'))