#exercício1
idade = 20
if idade >= 18:
    print("Maior de idade")

#exercício2
numero = 10
texto = "5"
resultado = numero + int(texto)
print(resultado)

#exercício3
lista = [10, 20, 30]
indice=5
if indice < len(lista):
    print(lista[indice])
else:
    print(f"Erro! O indice {indice} não existe! A lista possui apenas {len(lista)} elementos")

#exercicio4
def dividir_seguro(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print(f"Erro, o divisor precisa ser diferente de 0!")
        return None
    except TypeError:
        print(f"Erro, o divisor precisa ser um número inteiro!")
        return None
print(f"10/0 = {dividir_seguro(10,0)}")
print(f"10/2 = {dividir_seguro(10,2)}")
print(f"10/'abc' = {dividir_seguro(10,'abc')}")

#exercicio5
def converter_numeros(lista_texto):
    numeros=[]
    for texto in lista_texto:
        try:
            numero=float(texto)
            numeros.append(numero)
        except (ValueError, TypeError):
            print(f"Valor '{texto}' ignorado, não é um número válido!")
    return numeros
lista=["1","5.1","48","abc","x","55.4"]
resultado=converter_numeros(lista)
print(f"Lista original: {lista}")
print(f"Números convertidos: {resultado}")

#exercicio6
def validar_idade(idade):
    try:
        idade = int(idade)
    except ValueError:
        raise TypeError("A idade precisa ser um número inteiro")
    if idade<0:
        raise ValueError("Idade não pode ser negativo")
    if idade>150:
        raise ValueError("Idade não pode ser maior que 150")
    return idade
idd=input("Digite a idade:")
print(f"idade {idd}: {validar_idade(idd)}")

#exercicio7
def validar_nota(nota):
    try:
        nota = float(nota)
    except ValueError:
        raise TypeError("A nota precisa ser um número")
    if nota<0:
        raise ValueError("Nota não pode ser negativa")
    if nota>10:
        raise ValueError("Nota não pode ser maior que 10")
    return nota
nota=validar_nota(input("Digite a nota:"))
print(f"Nota: {nota}")

#exercicio8
def acessar_item(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print(f"Erro: Índice {indice} não pertence a lista")
        return None
lista=[3,6,55,4,83]
try:
    indice=int(input("Digite o índice que deseja procurar:"))
    print(f"Índice {indice}: {acessar_item(lista, indice)}")
except ValueError:
        print("Erro: digite um número inteiro válido")

#exercicio9
def calcular_imc(peso,altura):
        peso = float(peso)
        altura = float(altura)
        if peso <= 0 or altura <= 0:
            raise ValueError("Os valores devem ser maiores que zero!")

        imc = peso / (altura**2)
        if imc < 18.5:
            Classificação="Abaixo do peso normal!"
        elif imc<25:
            Classificação="Peso normal!"
        elif imc<30:
            Classificação="Excesso de peso!"
        elif imc<35:
            Classificação="Obessidade nível 1!"
        elif imc<40:
            Classificação="Obessidade nível 2!"
        else:
            Classificação="Obessidade nível 3!"
        return imc, Classificação

try:
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    imc, classif = calcular_imc(peso,altura)
    print(f"IMC = {imc:.2f}. Classificação - {classif}")
except ValueError as e:
    print(f"Erro: {e}")

#exercício10
def calcular_media(notas):
    if len(notas) == 0:
        raise ValueError("Lista de notas vazia, insira as notas!")

    notas_validas=[]

    for nota in notas:
        try:
            nota=float(nota)
        except ValueError:
            print(f"Valor Inválido: {nota}")
        if nota < 0 or nota > 10:
            raise ValueError(f"Nota inválida: {nota:.2f}")

        notas_validas.append(nota)
    media=sum(notas_validas)/len(notas_validas)
    return media

print("Calculo de Média das notas")
try:
    n1=float(input("Primeira nota: "))
    n2=float(input("Segunda nota: "))
    n3=float(input("Terceira nota: "))
    n4=float(input("Quarta nota: "))
    notas=[n1,n2,n3,n4]
    resultado=calcular_media(notas)
    print(f"A média das notas é: {resultado:.2f}")
except ValueError as e:
    print(f"Erro: {e}")
finally:
    print("Processo finalizado!")