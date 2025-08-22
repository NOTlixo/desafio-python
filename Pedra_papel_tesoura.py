from random import randint
from time import sleep

print('''Suas opcões:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')

jogador = int(input("Qual é a sua jogada?:"))

if jogador != 1 and jogador != 2 and jogador != 3:
    print("OPÇÃO INVALIDA")

if jogador == 1 or jogador == 2 or jogador == 3:
    print("PEDRA")
    sleep(1)

    print("PAPEL")
    sleep(1)

    print("TESOURA!!!")
    sleep(1)

    computador = randint(1,3)

    if jogador == 1 and computador == 1:
        print("-=-"*10)
        print("JOGADOR jogou Pedra\nCOMPUTADOR jogou Pedra")
        print("-=-"*10)
        print("EMPATE!!")

    elif jogador == 1 and computador == 2:
        print("-=-"*10)
        print(f"Jogador jogou Pedra\nComputador jogou papel")
        print("-=-"*10)
        print("JOGADOR PERDEU!!")

    elif jogador == 1 and computador == 3:
        print("-=-"*10)
        print("JOGADOR jogou Pedra\nCOMPUTADOR jogou Tesoura")
        print("-=-"*10)
        print("JOGADOR GANHOU!!")

    elif jogador == 2 and computador == 1:
        print("-=-"*10)
        print("JOGADOR jogou Papel\nCOMPUTADOR jogou Pedra")
        print("-=-"*10)
        print("JOGADOR GANHOU!!")

    elif jogador == 2 and computador == 2:
        print("-=-"*10)
        print("JOGADOR jogou Papel\nCOMPUTADOR jogou Papel")
        print("-=-"*10)
        print("EMPATE!!")

    elif jogador == 2 and computador == 3:
        print("-=-"*10)
        print("JOGADOR jogou papel\nCOMPUTADOR jogou Tesoura")
        print("-=-"*10)
        print("JOGADOR PERDEU!!")

    elif jogador == 3 and computador == 1:
        print("-=-"*10)
        print("JOGADOR jogou Tesoura\nCOMPUTADOR jogou Pedra")
        print("-=-"*10)
        print("JOGADOR PERDEU!!")

    elif jogador == 3 and computador == 2:
        print("-=-"*10)
        print("JOGADOR jogou Tesoura\nCOMPUTADOR jogou Papel")
        print("-=-"*10)
        print("JOGADOR GANHOU!!")

    elif jogador == 3 and computador == 3:
        print("-=-"*10)
        print("JOGADOR jogou Tesoura\nCOMPUTADOR jogou Tesoura")
        print("-=-"*10)
        print("EMPATE!!")
