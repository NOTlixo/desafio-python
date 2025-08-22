digita = int(input("quantos numeros você quer mostrar?"))
num1= 0
num2= 1
print(f"{num1} -> {num2}",end=" ->")
cont = 3
while cont <=digita:
    inicio = num1 + num2
    print(f"{inicio} ->", end="")
    num1 = num2
    num2 = inicio
    cont += 1
print("acabou")