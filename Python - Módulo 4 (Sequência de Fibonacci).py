#Sequência de Fibonacci

numtermos=int(input("Quantos termos você deseja na sequência da Fibonacci?: "))
a=0
b=1
contador=0
while contador < numtermos:
    for numero in range(numtermos):
        print (a, end=" ")
        prox = a+b
        a=b
        b=prox
        contador+1
    break
