from random import randint
from time import sleep
print("="*30)
print("VAMOS JOGAR PAR OU ÍMPAR ")
print("="*30)

sleep(2)

print("""mas antes as regras:
jogamos ate eu ganhar e é isso """)

print("="*30)
parimpar =" "
vitorias = 0

while True:

    while parimpar not in "PI":
        parimpar = str(input("Par ou Ímpar? [P/I]:")).upper()[0]

    numero = int(input("Digite um numero:"))
    computador = randint(0,10)
    comparacao = (numero + computador) %2

    if parimpar == "P":
        print("Você escolheu Par e o resulta é...")
        sleep(2)

        if comparacao == 0:
                print("=" * 30)
                print(f"Você jogou {numero} e o computador {computador}. Total de {numero + computador} DEU PAR")
                print("=" * 30)
                print("VOCÊ GANHOU!")
                sleep(1)
                print("vamos tentar de novo...")
                vitorias += 1
        else:
                print("=" * 30)
                print(f"Você jogou {numero} e o computador {computador}. Total de {numero + computador} DEU IMPAR" )
                print("=" * 30)
                print("VOCÊ PERDEU!")
                break

    elif parimpar == "I":
        print("Você escolheu Impar e o resultado é...")
        sleep(2)

        if comparacao == 1:
            print("=" * 30)
            print(f"Você jogou {numero} e o computador {computador}. Total de {numero + computador} DEU IMPAR")
            print("=" * 30)
            print("VOCÊ GANHOU!")
            sleep(1)
            print("vamos tentar de novo...")
            vitorias +=1

        else:
            print("=" * 30)
            print(f"Você jogou {numero} e o computador {computador}. Total de {numero + computador} DEU PAR")
            print("=" * 30)
            print("VOCÊ PERDEU!")
            break
print(f"GAMER OVER!!! Você ganhou {vitorias} vezes")