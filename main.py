nome = input('digite seu nome completo: ')
idade = int(input('digite sua idade: '))
salario = float(input('digite seu salario mensal: '))
salario_anual = salario * 12
if idade >= 18:
    
    print(f'maior de idade e seu salario anual é {salario_anual}')    
else:
    print(f'voce é menor de idade')


quantidade = int(input('quantos itens deseja adicionar: '))
lista = []
for q in range(quantidade):
    item = input('qual o item deseja adicionar')
    lista.append(item)
    if lista.count(item):
        print('esse item ja está na lista')
print(lista)
remover = input('deseja remover algum item da lista s/n: ')
if remover == 's':
    remover_item = input('qual item deseja remover?')
    lista.remove(remover_item)
    print(lista)
else:
    print('prosseguir compra')

    



frutas = ('banana, maça, uva, laranja, mexirica')
print(f'frutas disponiveis {frutas}')
nome_fruta = input('qual a fruta que você deseja: ')
if nome_fruta in frutas: 
    print(f'possui {frutas.count(nome_fruta)}')
else:
    print('nao possui')
