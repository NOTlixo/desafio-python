from random import randint
print("Escolha o numero de 0 a 10:")
pensamento = randint(0, 10)
condicao = False
while not condicao:
    jogador = int(input("Qual seu palpite?:"))
    if jogador == pensamento:
        condicao = True
    else:
        if jogador < pensamento:
            print("É maior que esse numero.")
        elif jogador > pensamento:
            print("É menor que esse numero")
print("Acertou!!!")
