print(f"{" MERCADO DO FABIN ":=^40}")

compra = float(input("Qual foi o valor da sua compra?:"))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/ pix
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
escolha = int(input("Digite a  opção desejada:"))
if escolha == 1:
    desconto = compra- (compra * 0.10)
    valor_desconto = compra - desconto
    print(f"""Sua compra foi no valor de R${compra} reais e pagando a vista terá um desconto de R${valor_desconto} reais \ne vc vai pagar R${desconto} reais""")

elif escolha == 2:
    desconto = compra - (compra * 0.05)
    valor_desconto = compra - desconto
    print(f"Sua compra foi no valor de R${compra} reais e pagando a vista no cartão terá um desconto de R${valor_desconto} reais \ne vc vai pagar R${desconto} reais")

elif escolha == 3:
    parcelas =  compra / 2
    print(f"Sua compra foi no valor de R${compra} reais parcelado em 2 vezes sem juros \nsuas parcelas serão de R${parcelas} reais por mês")

elif escolha == 4:
    usuario = int(input("Em quantas vezes deseja parcelar?:"))
    valor_final = compra + (compra *20 /100)
    parcelas = valor_final / usuario
    print(f"parcelando em {usuario}x de R${parcelas:.2f} reais  \ne sua compra de R${compra} reais ficara no valor de R${valor_final}")

else:
    print("opção invalida, tente novamente")
