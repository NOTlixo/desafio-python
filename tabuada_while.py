while True:
    num = int(input("Qual tabuada vc quer ver?:"))
    if num < 0:
        print("numero invalido",end="")
        break
    print(f"{f"TABUADA DO: {num} ":=^40}")
    for cont in range(1,11):
        print(f"{num} x {cont} = {num * cont}")

