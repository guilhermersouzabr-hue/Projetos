vcomp=float(input("Digite o valor da compra R$: "))
if vcomp>=100:
    vf=vcomp-(vcomp*0.10)
    print(f"Você tem 10% de desconto, o valor da compra é R${vf:.2f}")
elif vcomp>=50:
    vf=vcomp-(vcomp*0.05)
    print(f"Você tem 5% de desconto, o valor da compra é R${vf:.2f}")
else:
    print("Você não tem direito ao desconto")

    