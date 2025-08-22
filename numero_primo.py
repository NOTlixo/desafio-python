num = int(input("Digite um numero:"))
cont = 0
for c in range(1,num+1):
    if num % c ==0:
        print("\033[33m",end=' ')
        cont+=1
    else:
        print(f"\033[31m",end=' ')
    print(f"{c}", end=' ')
print(f"\n\033[mo numero {num} foi divisivel {cont} vezes")
if cont == 2:
    print("Por isso que ele é primo")
else:
    print("Por isso ele não é primo")
