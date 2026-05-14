# frutas=["maça", "banana", "laranga"]
# frutas[0]="banana"
# frutas[0:3]
# frutas.append("morango")
# frutas[0]="pera"
#
# for i,item in enumerate(frutas, start=1):
#     print(f"{i} - {item}")
#
# #tupla
# coordenadas = (10, 20)
# x,y = coordenadas
# print(x,y)
# try:
#     coordenadas[0]=99
# except:
#     print("Não é possível alterar o valor da tupla")
#
# #dicionário
# pessoa = {"nome": "Guilherme", "idade": "18"}
# print(f"A idade de {pessoa["nome"]} é {pessoa["idade"]} anos")
# print(pessoa.get("telefone", "Telefone não informado"))
# pessoa["celular"] = "11959637215"
# print(pessoa)
#
# for chave, valor in pessoa.items():
#     print(f"{chave} - {valor}")
#
# pessoa.pop("celular")
# for chave, valor in pessoa.items():
#     print(f"{chave} - {valor}")
#

# #31/03/26
#
# lista1=[1,2,3]
# lista2=[4,5,6]
# lista3=[7,8,9]
# matriz=[lista1,lista2,lista3]
# print(matriz[2][1])
#
# matriz[1][0]=10
# print(matriz)
# for i, linhas in enumerate(matriz):
#     for j, coluna in enumerate(linhas):
#         print(f"{[i]}, {[j]} = {coluna}")
#
# lista = []
# for i in range(5):
#     lista.append(i**2)
# print(lista)
#
# numeros = [-2, -1, 0, 1, 2, 3]
# lista3 = [x**2 for x in range(5) if x>0]
# print(lista3)
#
# matriz = [[1, 2], [3, 4]]
# lista4= [v for linha in matriz for v in linha]
# print(lista4)
#
# nomes=["João", "Maria", "Pedro"]
# idades = [25, 30, 22]
# pessoas={nome:idade for nome, idade in zip(nomes, idades)}
# print(pessoas)
#
# notas = {"João": 8.5, "Maria": 6.0, "Pedro": 9.0}
# Aprovados={nome:nota for nome, nota in notas.items() if nota>=7}
# print(f"Os aprovados são: {Aprovados}")

# #Leitura e escrita de arquivos
# arquivo_nome = "exemplo.txt"
# with open("arquivo_nome", "w", encoding="utf-8") as arquivo:
#     arquivo.write("Essa mensagem é um teste.\nTeste segunda linha.\nTerceira linha.")
#
# #usando append p adicionar
# with open("arquivo_nome", "a", encoding="utf-8") as arquivo:
#     arquivo.write("\nNova linha.")
#
# with open("arquivo_nome", "r", encoding="utf-8") as arquivo:
#     for i, linha in enumerate(arquivo, start=1):
#         print(f"linha {i}: {linha}".rstrip())

# CSV
dados = [
    {"Nome":"Guilherme", "Idade":18, "Cidade":"São Paulo"},
    {"Nome":"Neuza", "Idade":57, "Cidade":"Caetité"}
    ]
campos = ["Nome", "Idade", "Cidade"]

#importando csv
import csv

nome="pessoas.csv"
with open("pessoas.csv", "w", encoding="utf-8", newline="") as f:
    writer=csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerows(dados)
print("Arquivo .CSV criado com sucesso")

with open("pessoas.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    print(list(reader))

pessoas=list(reader)
Maiores=[pessoa for pessoa in pessoas if int(pessoa["idade"])>=30]
with open("pessoas_maiores.csv", "w", encoding="utf-8", newline="") as f:
    writer=csv.DictWriter(f, fieldnames=Maiores)
    writer.writeheader()
    writer.writerows(Maiores)



