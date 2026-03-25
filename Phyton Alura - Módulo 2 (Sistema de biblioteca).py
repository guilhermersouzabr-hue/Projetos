def devolver_livro(Valor_livro, Dias, usuário):
    eh_estudante = usuário == "estudante"
    if Dias <= 5:
        Total = Valor_livro
        if eh_estudante:
            Desconto = Total * 0.1
            Total -= Desconto
            print(f"Desconto de estudante aplicado R${Desconto:.2f}. Você não possui multas, o preço a ser pago é R${Total:.2f}")
        else:
            print(f"Você não possui multas! O preço a ser pago é R${Total:.2f}")
    else:
        Multa = 0.1 * Valor_livro * (Dias - 5)
        Total = Valor_livro + Multa
        print(f"Você possui uma multa no valor de R${Multa:.2f}. O preço a ser pago é de R${Total:.2f}")

idade=int(input("Digite a sua idade: "))
carteira_biblioteca=(input("Você tem carteira da biblioteca? (S/N): ")).upper()

while True:
    usuário=input("Você é um usuário regular ou é um estudante?: ").lower()
    if usuário in ["regular", "estudante"]:
        break
    else:
        print("Opção inválida! Tente novamente!")

if idade < 12:
    print("Você precisa ter no mínimo 12 anos ou estar acompanhado(a) de um responsável para prosseguir o atendimento!")
    print("Atendimento Finalizado!")
elif carteira_biblioteca == "N":
    print("Você precisa ter a carteira da biblioteca! Favor solicitar no balcão de atendimento!")
    print("Atendimento Finalizado!")
else:
    while True:
        opção = (input("""Escolha uma das opções abaixo: 
1-Devolver Empréstimo 
2-Renovar Empréstimo 
3-Solicitar Empréstimo
"""))
        if opção=="1":
            Valor_livro=float(input("Digite o valor do livro R$: "))
            Dias=int(input("Quantos dias você ficou com o livro?: "))
            devolver_livro(Valor_livro, Dias, usuário)
            print("Atendimento Finalizado!")
            break

        elif opção=="2":
            Valor_livro = float(input("Digite o valor do livro R$: "))
            Qts_Renovação = int(input("Quantas renovações desse livro você ja fez?: "))
            Dias = int(input("Quantos dias você ficou com o livro?: "))
            Valor_renovação=(Valor_livro*0.1)
            if Dias > 5:
                Multa = 0.1 * Valor_livro * (Dias - 5)
            else:
                Multa = 0
            if Qts_Renovação>2:
                print(f"Você não pode realizar renovações, pois já atingiu o limite máximo! Você deve devolver o livro!")
                devolver_livro(Valor_livro, Dias, usuário)
                print("Atendimento Finalizado!")
                break
            elif Dias<=5 and Qts_Renovação>0 and Qts_Renovação<=2:
                Valor_total = (Valor_renovação*Qts_Renovação) + Valor_livro
                print(f"Você não possui multas! O livro pode ser renovado com um aumento de R${Valor_renovação:.2f}. O preço final será de R${Valor_total:.2f}")
            elif Dias>5 and Dias<=7 and Qts_Renovação>0 and Qts_Renovação<=2:
                Valor_total = (Valor_renovação*Qts_Renovação) + Valor_livro + Multa
                print(f"Você possui uma multa no valor de R${Multa:.2f} pelo atraso. Porém o livro pode ser renovado com um aumento de R${Valor_renovação:.2f}. O preço final será de R${Valor_total:.2f}")
            else:
                Valor_total = Valor_livro + Multa
                print(f"Você possui uma multa no valor de R${Multa:.2f} pelo atraso. Você não tem direito a renovação, por conta do longo atraso. O preço final será de R${Valor_total:.2f}")
            print("Atendimento Finalizado!")
            break

        elif opção=="3":
            Valor_livro = float(input("Digite o valor do livro R$: "))
            if usuário=="regular":
                Valor_total=Valor_livro
                print(f"Você tem direito a 5 dias com o livro pelo preço de {Valor_total:.2f}. O atraso na devolução gera uma multa de 10% ao dia, podendo levar a proibição da renovação do livro!")
            else:
                Valor_total=Valor_livro-(Valor_livro*0.1)
                print(f"Você tem direito a 5 dias com o livro, com o desconto de 10% de estudante aplicado. O preço final é de R${Valor_total:.2f}. O atraso na devolução gera a perda do desconto de estudante e uma multa de 10% ao dia, podendo levar a proibição da renovação do livro!")
            print("Atendimento Finalizado!")
            break

        else:
            print("Opção inválida! Tente novamente!")