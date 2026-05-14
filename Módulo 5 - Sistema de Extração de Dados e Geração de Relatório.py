import csv
Loja="vendas.csv"
vendas = []
with open(Loja, "r", encoding="utf-8", newline="") as arquivo:
    reader = csv.DictReader(arquivo)
    for linha in reader:
        linha ["Quantidade"] = int(linha["Quantidade"])
        linha ["Preco"] = float(linha["Preco"])
        vendas.append(linha)
    print(f"Total de vendas cadastradas: {len(vendas)}")

erros=[]
if not vendas:
    print("Erro: Nenhuma venda foi encontrada")
else:
    for i, venda in enumerate(vendas):
        produto=venda.get("Produto", "").strip()
        if not produto:
            erros.append(f"Linha {i+1}: Produto inválido")
        if venda["Quantidade"] <=0:
            erros.append(f"Linha {i+1}: A quantidade deve ser maior que 0")
        if venda["Preco"] <=0:
            erros.append(f"Linha {i+1}: O preço deve ser maior que 0")
if erros:
    for erro in erros:
        print(erro)
else:
    print("Verificação concluída, nenhum erro foi encontrado")

for venda in vendas:
    venda["Valor Total"]=venda["Quantidade"]*venda["Preco"]

Total_registros = len(vendas)
Total_unidades_vendidas = sum(venda["Quantidade"] for venda in vendas)
Valor_total_vendas = sum(venda["Valor Total"] for venda in vendas)
Valor_médio_venda = (Valor_total_vendas/Total_registros) if Valor_total_vendas>0 else 0

print(f"Total de vendas cadastradas: {Total_registros}")
print(f"Total de unidades vendidas: {Total_unidades_vendidas}")
print(f"Valor total de vendas: R${Valor_total_vendas:.2f}")
print(f"Valor médio por venda: R${Valor_médio_venda:.2f}")

por_produto={}
for venda in vendas:
    produto=venda["Produto"]
    if produto not in por_produto:
        por_produto[produto]={"quantidade_total":0, "Valor_total":0.0}
    por_produto[produto]["quantidade_total"]+=venda["Quantidade"]
    por_produto[produto]["Valor_total"]+=venda["Valor Total"]
print(f"Total de produtos cadastrados: {len(por_produto)}")

produto_maior_qtd={}
maior_qtd=0
for produto, dados in por_produto.items():
    if dados["quantidade_total"]>maior_qtd:
        maior_qtd=dados["quantidade_total"]
        produto_maior_qtd=[produto,dados]

produto_maior_valor=[]
maior_valor=0.0
for produto, dados in por_produto.items():
    if dados["Valor_total"]>maior_valor:
        maior_valor=dados["Valor_total"]
        produto_maior_valor=[produto,dados]

p_qtd, d_qtd = produto_maior_qtd
p_valor, d_valor = produto_maior_valor
print(f"Produto de maior quantidade: {p_qtd} ({d_qtd['quantidade_total']} unidades)")
print(f"Produto de maior valor: {p_valor} (R${d_valor['Valor_total']:.2f})")


linhas=[]
linhas.append("="*60)
linhas.append("RELATÓTIO DE VENDAS")
linhas.append("="*60)
linhas.append("")
linhas.append("ESTÁTISTICAS GERAIS")
linhas.append("="*60)
linhas.append(f"Total de vendas cadastradas: {Total_registros}")
linhas.append(f"Total de unidades vendidas: {Total_unidades_vendidas}")
linhas.append(f"Valor total de vendas: R${Valor_total_vendas:.2f}")
linhas.append(f"Valor médio por venda: R${Valor_médio_venda:.2f}")
linhas.append("="*60)
linhas.append("")
linhas.append("DESTAQUES")
linhas.append("="*60)
linhas.append(f"Produto de maior quantidade: {p_qtd} ({d_qtd['quantidade_total']} unidades)")
linhas.append(f"Produto de maior valor: {p_valor} (R${d_valor['Valor_total']:.2f})")
linhas.append("="*60)
linhas.append("")
for linha in linhas:
    print(linha)

linhas.append("DETALHAMENTO POR PRODUTO")
linhas.append("="*60)
produtos_ordenados=sorted([(dados["Valor_total"], produto, dados) for produto, dados in por_produto.items()], reverse=True)
for Valor_total, produto, dados in produtos_ordenados:
    linhas.append(f"{produto}: {dados['quantidade_total']} unidades - R${dados['Valor_total']:.2f}")
linhas.append("="*60)
linhas.append("Fim do Relatório")
linhas.append("="*60)
for linha in linhas:
    print(linha)
texto_relatorio = "\n".join(linhas)

with open("relatorio_vendas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_relatorio)
print("Relatório salvo em: relatorio_vendas.txt")