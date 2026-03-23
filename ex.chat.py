n1=int(input("Digite o 1° número: "))
n2=int(input("Digite o 2° número: "))
n3=int(input("Digite o 3° número: "))
if n1<n2 and n1<n3 and n2<n3:
    print(f"A ordem crescente é {n1}, {n2} e {n3}")
elif n1>n2 and n1<n3 and n3>n2:
    print(f"A ordem crescente é {n2}, {n1} e {n3}")
elif n1>n2 and n1>n3 and n3>n2:
    print(f"A ordem crescente é {n2}, {n3} e {n1}")
elif n1>n2 and n1>n3 and n2>n3:
    print(f"A ordem crescente é {n3}, {n2} e {n1}")
elif n2>n1 and n2>n3 and n3>n1:
    print(f"A ordem crescente é {n1}, {n3} e {n2}")
elif n2>n1 and n2>n3 and n1>n3:
    print(f"A ordem crescente é {n3}, {n1} e {n2}")

l1=int(input("Digite o 1° lado: "))
l2=int(input("Digite o 2° lado: "))
l3=int(input("Digite o 3° lado: "))
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    print("Os lados formam um triângulo")
    if l1==l2 and l2==l3:
        print("Triângulo equilátero")
    elif l1==l2 or l2==l3 or l3==l1:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os lados não formam um triângulo")

secreto=7
tent=int(input("Digite um número: "))
if tent==secreto:
    print("Parabéns, você acertou o número secreto!")
elif tent>secreto:
    print(f"O número secreto é menor que {tent}")
else:
    tent<secreto
    print(f"O número secreto é maior que {tent}")

pode_entrar= False
idade=int(input("Digite sua idade: "))
if idade>=18:
    pode_entrar= True
elif idade>=16:
    aut=(input("Trouxe autorização dos pais? sim/não: "))
    if aut=="sim":
        pode_entrar= True
if pode_entrar:
    print("Entrada permitida")
else:
    print("Entrada negada")