cont = 0
media = 0
soma = 0
maior = 0
nome = ''
for c in range(1,5):
    print(f"{f" {c}° PESSOA ":-^40}")
    Nome = str(input("Nome:"))
    Idade = int(input("Idade:"))
    Sexo = str(input("Sexo [M/F]:")).upper().strip()
    soma += Idade
    media = soma / 4
    if Sexo == "F" and Idade < 20:
        cont += 1

    if Sexo == "M" and Idade > maior:
            maior = Idade
            nome = Nome
print(f"A média de idade do grupo é de {media} ")
print(f"O homem mais velho tem {maior} anos e se chama {nome} ")
print(f"Tivemos {cont} mulheres com menos de 20 anos")
