idade = int(input('qual a sua idade'))
if idade < 18:
    print('não pode dirigir')
else: 
    carteira = input('tem carteira?')
    carro = input('tem carro?')
if idade >= 18:
    if carteira == 'sim':
        if carro == 'sim':
            print('pode dirigir')
        else:
            print('precisa de um carro')
    else:
        print('precisa de carteira')
17