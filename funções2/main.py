# Crie uma função chamada calcular_imovel que aceita os parâmetros area, tipo_imovel (com valor padrão 'apartamento') e tipo_negocio (com valor padrão 'venda'). A função deve imprimir uma frase descrevendo a transação. Chame a função de três maneiras diferentes: Usando apenas argumentos posicionais. Usando argumentos nomeados para tipo_negocio e tipo_imovel. Usando uma combinação de argumentos posicionais e nomeados, alterando apenas o tipo_imovel.
# def calcular_imovel(area, tipo_imovel = 'apartamento', tipo_negocio = 'venda'):
    
#     print(f'''
# A area do imovel é {area}
# O tipo do imovel é {tipo_imovel}
# o tipo do negocio é {tipo_negocio}
#           ''')

# calcular_imovel(80)
# calcular_imovel(50, tipo_imovel= 'barracão', tipo_negocio= 'compra')
# calcular_imovel(area = 60, tipo_imovel= 'casa')

# Crie uma função chamada executar_pipeline que recebe uma lista de dados e uma função de transformação. A função deve aplicar a transformação em cada item da lista e retornar o resultado. Crie duas funções de transformação, uma que dobra um número e outra que adiciona 5. Use sua função executar_pipeline para aplicar primeiro a função que dobra na lista [1, 2, 3], depois aplique a função que adiciona 5 no resultado anterior. Imprima o resultado de cada aplicação.

# def executar_pipeline(dados, transformação):
#     return[transformação(dado) for dado in dados]
# lista = [1, 2, 3]

# def dobrar(elemento):
#     return elemento * 2
# def adicionar(elemento):
#     return elemento + 5

# print(f'''
# o dobro da lista é {executar_pipeline(lista,dobrar)}
# o soma da lista é {executar_pipeline(lista,adicionar)}
#       ''')


# Crie um módulo chamado calculos.py que contém duas funções: calcular_media(lista) e calcular_soma(lista). A primeira deve retornar a média dos números em uma lista e a segunda deve retornar a soma. Em outro arquivo, chamado main.py, importe as duas funções do módulo calculos.py. Crie uma lista de números [10, 20, 30, 40] e use as funções importadas para imprimir a média e a soma da lista.

from calculo import calcular_media
from calculo import calcular_soma
from calculo import numeros

print(f'''
 a media da lista é {calcular_media(numeros)}
 o soma da lista é {calcular_soma(numeros)}
       ''')





