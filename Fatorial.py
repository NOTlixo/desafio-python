numero = int(input("Digite um numero para calcular seu fatorial: "))
f = 1
while numero > 0:
    print(f"{numero}",end= '')
    print(" x " if numero > 1 else " = ", end='')
    f *= numero
    numero -= 1
print(f"{f}")