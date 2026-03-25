while True:
    nome=(input("Digite o nome do aluno: "))
    idade=int(input("Digite a idade do aluno: "))
    email=(input("Digite o email do aluno: "))
    rm=int(input("Digite o rm do aluno: "))
    if len(email) >= 5 and "@" in email and " " not in email and len(str(rm))==6 and idade>0 and idade<=100 and nome.strip() !="":
        break
    else:
        print("Dados Inválidos, tente novamente!")

while True:
    n1=float(input(f"Digite a 1° nota do/a {nome}: "))
    n2=float(input(f"Digite a 2° nota do/a {nome}: "))
    n3=float(input(f"Digite a 3° nota do/a {nome}: "))
    media=(n1+n2+n3)/3
    if (n1 >= 0 and n1 <= 10 and
        n2 >= 0 and n2 <= 10 and
        n3 >= 0 and n3 <= 10):
        break
    else:
        print("Notas inválidas, tente novamente!")

if media >= 7:
    print(f"Com média {media:.1f} o aluno/a {nome} está aprovado")
elif media>=5:
    print(f"Com média {media:.1f} o aluno/a {nome} está de recuperação")
elif media<5:
    print(f"Com média {media:.1f} o aluno/a {nome} está reprovado")

MaN=max(n1,n2,n3)
print(f"A maior nota foi {MaN:.1f}")
MeN=min(n1,n2,n3)
print(f"A menor nota foi {MeN:.1f}")