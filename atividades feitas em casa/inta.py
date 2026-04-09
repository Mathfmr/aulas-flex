print("Wendel:13")
print("Fabi:22")

wendel1 = 0
fabi1 = 0

while True:
    while (fabi1 + wendel1) == 3:
        print("Votos do Wendel:", wendel1)
        print("Votos do Fabi:", fabi1)
        break
    voto = int(input('Digite seu canditado:'))
    if voto == 13:
        print("Você está votando no Wendel")
        confirma = input("Confirma seu voto no Wendel:")
        if confirma == "Sim": #sim minusculo
            print("Voto no Wendel confirmado")
            wendel1 += 1
            os.system("cls")
            continue
        if confirma == "Nao": #nao minusculo
            os.system("cls")
            continue
    if voto == 22:
        print("Você está votando no Fabi")
        confirma = input("Confirma seu voto no Fabi:")
        if confirma == "Sim": #sim minusculo
            print("Voto no Fabi confirmado")
            fabi1 += 1
            os.system("cls")
            break
        if confirma == "Nao": #nao minusculo
            os.system("cls")
            continue
    else:
        os.system("cls")
        print("Canditado não encontrado")
        continue

