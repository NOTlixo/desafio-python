numero = int(input("digite um numero qualquer:"))
print('''Qual sera a forma de conversão desse numero?
1- Binário
2- Octal
3- Hexadecimal''')
escolha = int(input("Qual sera a escolha?:"))

if escolha == 1:
    print("convertendo para binario...")
    print(f"o numero {numero} em binário é {bin(numero)[2:]}")

elif escolha ==2:
    print("convertendo para Octal")
    print(f"o numero {numero} em Octal é {oct(numero)[2:]}")

elif escolha == 3:
    print("convertendo para hexadecimal")
    print(f" o numero {numero} em hexadecimal é {hex(numero)[2:]}")
else:
    print("opção invalida, tu é idiota???????")