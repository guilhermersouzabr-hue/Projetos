for numero in (1,2,3,4,5,6,7,8,9,10):
    print(numero)

#exercico2
num=0
while num <= 5:
    print(f"contador: {num}")
    num = num + 1

#exercicio3
for notas in (7.5, 8.0, 9.5, 6.0, 8.5):
    media=(7.5+8.0+9.5+6.0+8.5)/5
    print(f"média: {media}")

#exercicio 4
for i in range(1,11):
    multiplicação = i*7
    print(f"{i} x 7 = {multiplicação}")

#exercicio5
for par in range(0,21,2):
    print(par)

#exercicio6
listanumeros=[5, 12, 8, 3, 15, 7]
for lisnumeros in listanumeros:
    if lisnumeros>10:
        print(f"Número maior que 10: {lisnumeros}")
        break #quando encontrar o primeiro numero maior que 10 automaticamente ja para o comando por conta do break

#exercicio7
lista=[-2, 5, -1, 8, -3, 10]
for positivo in lista:
    if positivo<=0:
        continue
    print(f"Números positivos: {positivo}")

#exercicio8
Palavra="Python"
vogais="aeiouAEIOU"
contvogais=0
for letra in Palavra:
    if letra in vogais:
        contvogais=contvogais+1
        print(f"A palavra {Palavra} contém {contvogais} vogais")

#exercicio9
lnum=[15, 8, 23, 4, 42, 11, 7, 19]
soma=0
maior = lnum[0]
menor = lnum[0]
contador_pares = 0
contador_impares = 0
for n in lnum:
    soma=soma+n
    media = soma/len(lnum)
    if n%2==0:
        contador_pares=contador_pares+1
    else:
        contador_impares=contador_impares+1
    if n>maior:
        maior=n
    if n<menor:
        menor=n
print(f"A soma é {soma}, a média é {media:.2f}, o maior número é {maior} e o menor é {menor}.")
print(f"Contém {contador_pares} pares e {contador_impares} impares")

