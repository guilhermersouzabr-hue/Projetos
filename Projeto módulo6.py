def ler_csv(arquivo):
#ler arquivo csv e retronar uma lista de dicionário
    dados=[]
    with open(arquivo, "r", encoding="utf-8") as f:
        cabecalho=f.readline().strip().split(",")
        for linha in f:
            valores=linha.strip().split(",")
            registro={}
            for i, campo in enumerate(cabecalho):
                registro[campo]=valores[i]
            dados.append(registro)
    return dados

dados=ler_csv("dados_vendas.csv")
print(f"Total de registros: {len(dados)}")
print(f"\nLista de Registros:")
for i, registro in enumerate(dados, 1): #aqui organiza a lista
    print(f"{i} - {registro}")

#calcular dados
def criar_tabela_metricas(dados, colunas_numéricas):
    tabela={}
    for coluna in colunas_numéricas:
        valores=[]
        for registro in dados:
            try:
                valor=float(registro[coluna])
                valores.append(valor)
            except (ValueError, KeyError):
                continue

        if valores: #isso no caso do try
            tabela[coluna]= {
                "contagem": len(valores), #quantidade
                "maximo": max(valores),
                "minimo": min(valores),
                "media": sum(valores) / len(valores) #soma pela quantidade
            }
    return tabela

for registro in dados:
    registro["Quantidade"]=float(registro["Quantidade"])
    registro["Preco"]=float(registro["Preco"])
colunas=["Quantidade", "Preco"]
metricas=criar_tabela_metricas(dados, colunas)
# Exibir a tabela
print("\tTabela de Métricas:")
print("-" * 60)
print(f'{"Coluna":<15} {"Contagem":<10} {"Máximo":<12} {"Mínimo":<12} {"Média":<12}')
print("-" * 60)
for coluna, valores in metricas.items():
    print(f"{coluna:<15} {valores["contagem"]:<12} {valores["maximo"]:<12.2f} {valores["minimo"]:<12.2f} {valores["media"]:<12.2f}")

#esse<12, serve pra dar espaço