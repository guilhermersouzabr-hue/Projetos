#exercicio1
def somar(a,b,c):
    return a+b+c

soma=somar(6,7,8)
print(f"Soma: {soma}")

#exercicio2
import math
def calcular_área(raio):
    return math.pi * raio**2
Raio=float(input("Digite o raio: "))
result=calcular_área(Raio)
print(f"A área do raio {Raio} é {result:.2f}")

#exercicio3
def maior_idade(idade):
    if idade>=18:
        return True
    else:
        return False
Idade=int(input("Digite sua idade: "))
if maior_idade(Idade):
    print("Entrada permitida!")
else:
    print("Entrada não permitida!")

#exercicio4
def desconto(valor,percentual=10):
    desconto = valor-(valor * (percentual/100))
    return desconto
preço = float(input("Digite o valor do produto: "))
descont=int(input("Digite o percentual de desconto: "))
final = desconto(preço, descont)
print(f"O valor final com o desconto de {descont}% é R${final:.2f}")

#exercicio5
def nota(n1,n2,n3):
    media=(n1+n2+n3)/3
    aprovado = media >= 7
    return media, aprovado

nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))

media, aprovado=nota(nota1,nota2,nota3)
if aprovado:
    print(f"Aprovado com média: {media:.2f}")
else:
    print(f"Reprovado com média: {media:.2f}")

#exercicio6
dobro=lambda x:(x*2)
n1=int(input("Digite um número inteiro: "))
print(f"Dobro de {n1}: {dobro(n1)}")

#exercicio7
numeros = [1, 3, 6, 8, 2, 9, 4, 7]
maiores_que_5=list(filter(lambda x: x >= 5, numeros))
print(f"Números maiores que 5: {maiores_que_5}")

#exercicio8
import random
print("5 números aleatórios entre 1 e 100:")
for i in range(5):
    numero=random.randint(1,100)
    print(f"{i+1}. {numero}")

#exercicio9
from datetime import datetime
agora = datetime.now()
data_formada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Data e hora atual: {data_formada}")
