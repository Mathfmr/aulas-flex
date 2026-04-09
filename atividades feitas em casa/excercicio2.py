#Crie um programa que solicite ao usuário: Idade da pessoa Se possui carteira de motorista (True ou False) 
#O programa deve verificar se a pessoa pode dirigir. Para isso, a pessoa precisa ter 18 anos ou mais e ter carteira. 
#Exiba na tela: "Pode dirigir" se a pessoa atender aos critérios "Não pode dirigir" caso contrário Dica: use os operadores >= e and.

#idade = int(input('digite sua idade'))
#carteira = input('tem carteira')
idade = int(input('digite sua idade'))
if idade < 18:
    print('não pode dirigir')
else:

    tem_carteira = input('possui carteira de motorista s/n')

if idade >= 18 and tem_carteira == 's':
    print('pode dirigir')