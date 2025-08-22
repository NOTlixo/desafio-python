print("-="*20)
print(f"{f"CADASTRO DE PESSOAS":^40}")
print("-=" *20)
contid= contsex= contmu = 0
Sexo =" "
escolha = " "

while True:
    idade = int(input("Idade:"))

    while Sexo not in "MF":
        Sexo = str(input("Sexo [M/F]:")).upper()

    while escolha not in "SN":
        print("="*30)
        escolha = str(input("Deseja continuar? [S/N]:")).upper()
        print("="*30)

    if idade >18:
        contid += 1

    if Sexo == "M":
        contsex += 1

    if idade < 20 and Sexo == "F":
        contmu +=1

    if escolha == "N":
        break
print(f"Temos {contid} pessoas com mais de 18 anos")
print(f"{contsex} homens foram cadastrados")
print(f"{contmu} mulheres tem menos de 20 anos")