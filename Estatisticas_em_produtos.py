soma = 0
contador_custo =  menor_preco = maior_preco=  cont= 0
nome_produto_barato = ""
while True:

    nome_produto = str(input("Nome do Produto:"))
    preco_produto = float(input("Preço:"))
    escolha = ' '
    while escolha not in "SN":
        escolha = str(input("Deseja continuar? [S/N]:")).upper()
    cont +=1
    soma += preco_produto

    if preco_produto >1000:
        contador_custo += 1

    if cont == 1 or preco_produto < menor_preco:
        menor_preco = preco_produto
        nome_produto_barato = nome_produto



    if escolha == "N":
        break

print(f"o total dos produtos é {soma:.2f}")
print(f"{contador_custo} produtos custam mais de R$ 1000.00 ")
print(f"o produto mais barato foi {nome_produto_barato} que custa {menor_preco}")