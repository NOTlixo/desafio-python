frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto)- 1, - 1, - 1):
    inverso += junto[letra]
print(f"a frase normal é {junto} e seu inverso é {inverso}")
if inverso == junto:
    print("É u palindromo")
else:
    print("A frase digitada não é um palindromo")