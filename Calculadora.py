valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
escolha = 0

while escolha != 5:
    print("""[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] sair do programa""")
    print("-="*20)
    escolha = int(input("Qual é a sua opção?:"))
    if escolha > 5:
        print("opção invalida. Tente novamente")

    if escolha == 1:
        somar = valor1 + valor2
        print(f"A soma entre {valor1} + {valor2} é {somar}")
        print("-="*20)

    elif escolha == 2:
        x = valor1 * valor2
        print(f"O resultado entre {valor1} x {valor2} é {x}")
        print("-="*20)

    elif escolha == 3:

        if valor1 > valor2:
            print(f"Entre o {valor1} e {valor2 } o maior numero é {valor1}")

        elif valor1 < valor2:
            print(f"Entre o {valor1} e {valor2} o maior numero é {valor2}")

        else:
            print(f"{valor1} e {valor2} são iguais")
        print("-=" * 20)

    elif escolha == 4:
        valor1 = int(input("Digite o novo valor:"))
        valor2 = int(input("Digite outro valor"))
        print(f"seus novos valores são {valor1} e {valor2}")
    print("-=" *20)

print("Obrigado pela preferencia!!")