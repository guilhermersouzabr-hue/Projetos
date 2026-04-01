#exercicio1
lista=[]
lista.append("letra")
lista.append("número")
lista.append("conta")

if "letra" in lista:
    lista.remove("letra")
    print(lista)

for i, item in enumerate(lista, start=1):
    print(f"{i} - {item}")

#exercício2
Alunos = {
    "Guilherme": {"idade":18, "nota":6.5},
    "Laura": {"idade":19, "nota":4.3},
    "Matut": {"idade":17, "nota":7.2},
}
for nome, dados in Alunos.items():
    print(f"{nome} - {dados ['idade']} anos, nota: {dados['nota']}")

#exercicio3
numeros = [3, 1, 4, 1, 5]
print("Tamanho da lista:", len(numeros))
print("Soma:", sum(numeros))
print("Lista ordenada:", sorted(numeros))
print("Ocorrências do 1:", numeros.count(1))

#exercicio4
coordenadas = (10, 20)
x, y=coordenadas
print(f"X={x}, Y={y}")

#exercicio5
pessoa = {"nome": "João", "idade": 25}
print("Nome:", pessoa["nome"])
print("Telefone:", pessoa.get("Telefone", "(Não informado)"))

#exercicio6
matriz=[[(i+1) * (j+1) for j in range(5)] for i in range(5)]
for linha in matriz:
    print(linha)

#exercicio7
lista_números = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
positivos_quadrados = [x**2 for x in lista_números if x>0]
print(positivos_quadrados)

#exercicio8
notas = {"João": 8.5, "Maria": 6.0, "Pedro": 9.0}
aprovados= {nome: nota for nome, nota in notas.items() if nota>=7}
print(aprovados)

#exercicio9
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Maria: 5.5\n")
    f.write("Guilherme: 6.0\n")
notas=[]
with open("notas.txt", "r", encoding="utf-8") as f:
    for linha in f:
        nome, nota_str = linha.strip().split(":")
        nota=float(nota_str)
        notas.append(nota)
    print(f"{nome}: {notas}")
media= sum(notas)/len(notas)
print(f"\n A média das notas é: {media}")

#exercicio10
dados = [
    {"Nome": "Guilherme", "Idade": 18, "Cidade": "São Paulo"},
    {"Nome": "Jefferson", "Idade": 27, "Cidade": "Rio de Janeiro"},
    {"Nome": "Enzo", "Idade": 12, "Cidade": "Belo Horizonte"},
]
campos = ["Nome", "Idade", "Cidade"]
import csv
with open("pessoas.csv", "w", encoding="utf-8", newline="") as f:
    writer=csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerows(dados)
print("Arquivo pessoas.csv criado")

with open("pessoas.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    pessoas=list(reader)
maiores=[maior for maior in pessoas if int(maior["Idade"])>=18]
with open("pessoas_maiores.csv", "w", encoding="utf-8", newline="") as f:
    writer=csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerows(maiores)
print(f"Arquivo de pessoas maiores criado: {len(maiores)} registros")



