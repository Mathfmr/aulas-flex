# Você deve criar um script chamado utilizando_modulos.py que resolva as seguintes tarefas. O objetivo é entender como usar diferentes módulos internos em conjunto para automatizar pequenas rotinas. Requisitos: Módulo math Peça ao usuário um número inteiro e mostre: O fatorial desse número. A raiz quadrada desse número. Módulo random Crie uma lista com pelo menos 5 nomes e sorteie um deles para exibir na tela. Módulo datetime Mostre a data e a hora atuais. Mostre também apenas o ano atual. Módulo os Mostre qual é o diretório atual do script. Crie uma pasta chamada "resultado_modulos" dentro desse diretório. Organize o código em um único arquivo (utilizando_modulos.py) e utilize os módulos exatamente como visto em aula.
import math
import random
import datetime
numero = 9

print(math.factorial(numero))
print(math.sqrt(numero))

lista = ['matheus', 'gabriel', 'marcos', 'jessica', 'rodrigo']

print(random.choice(lista))

agora = datetime.datetime.now().strftime('%d/%m/%Y , %H:%M:%S')
print(agora)

# pip freeze > requeriments.txt
# python -m venv . venv
# .venv/scripts/activate
# pip install -r requeriments.txt
