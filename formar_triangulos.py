reta1 = float(input("Digite o valor da primeira reta:"))
reta2 = float(input("Digite o valor da segunda reta:"))
reta3 = float(input("Digite o valor da terceira reta:"))
if reta1 + reta2 > reta3 and reta1 + reta3 >reta2 and reta2 + reta3> reta1:

    if reta1 == reta2 == reta3:
        print(" É possivel formar um triangulo equilatero")

    if reta1 == reta2 !=reta3 or reta1 == reta3 !=reta2 or reta2 == reta3 != reta1:
        print("É possivel formar um triangulo triangulo isósceles")

    if reta1 != reta2 !=reta3 != reta1:
        print("É possivel formar um triangulo Escaleno")

else:
    print("Os valores das retas são insuficiente para formar o triangulo")