#Crie um programa que: Solicite ao usuário três notas (use input() e converta para float). 
#Calcule a média aritmética dessas três notas. 
#Exiba a situação acadêmica do aluno seguindo as regras: "Aprovado" → média maior ou igual a 7.0 "Recuperação" → média maior ou igual a 5.0 e menor que 7.0""
#"Reprovado" → média menor que 5.0
nota1 = float(input('digite a primeira nota'))
nota2 = float(input('digite a segunda nota'))
nota3 = float(input('digite a terceira nota'))

media = float((nota1 + nota2 + nota3)/3)
if media >= 7:
    print(f'sua media foi {media:.2f} você está aprovado')
elif media >= 5:
    print(f'sua media foi {media:.2f} você está em recuperação')
else:
     print(f'sua media foi {media:.2f} você está reprovado')
