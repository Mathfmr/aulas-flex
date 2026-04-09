# Você deve criar um programa simples em Python para simular um pipeline de vendas.
#  O programa deve seguir os seguintes passos: 
# Criar uma função para cadastrar os produtos disponíveis, armazenando-os em um dicionário no formato: 
# {"nome_produto": preco_unitario} 
# Os produtos já estão definidos: 
# Camiseta – R$ 50,00 Tênis – R$ 200,00 Boné – R$ 40,00 Mochila – R$ 120,00 Jaqueta – R$ 300,00 
# Criar uma função que receba o nome do produto e a quantidade, retornando o valor total sem desconto. 
# Criar uma função que aplique um desconto de acordo com o tipo de pagamento: 
# Pix → 10% de desconto Débito → 5% de desconto Crédito → 
# sem desconto Criar uma função principal (processar_venda) que receba: 
# Nome do produto Quantidade Tipo de pagamento E devolva o valor final da compra já com desconto aplicado.
#  Saída Esperada (exemplo) Produto: Camiseta | Quantidade: 2 | Pagamento: pix | Valor final: R$ 90.00 Crie 5 vendas.
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

while True:   
    print("\nProdutos disponíveis:", produtos_iniciais)
    desejo = input('Deseja comprar algum produto? (sim/não) ').lower()
    
    if desejo != 'sim':
        break 
    comprap = input('Qual produto deseja adicionar ao seu carrinho? ').lower()
    
    if comprap not in produtos_iniciais:
        print('Produto não está cadastrado. Tente novamente.')
        continue   
    quantidade = int(input('Qual a quantidade do produto? '))
    if comprap in carrinho:
        carrinho[comprap] += quantidade
  
    else:
        carrinho[comprap] = quantidade
        
    print(f'-> Adicionado com sucesso!')
    
    finalizar_compra = input('Deseja finalizar a compra e ir para o caixa? (sim/não) ').lower()
    if finalizar_compra == 'sim':
        break 



if carrinho: 
    print('\n--- SEU CARRINHO ---')
    print(carrinho)
    
    tipo_pagamento = input('\nQual o tipo de pagamento para toda a compra? (pix/debito/credito) ').lower()
    confirmar = input('Deseja confirmar a compra? (sim/não) ').lower()
    
    if confirmar == 'sim':
        print('\n--- PROCESSANDO RECIBO ---')
        for produto, qtd in carrinho.items():
            processar_venda(produto, qtd, tipo_pagamento)
            
        print('\nObrigado por visitar nossa loja!')
    else:
        print('\nCompra cancelada.')
else:
    print('\nObrigado por visitar nossa loja!')



    




    
