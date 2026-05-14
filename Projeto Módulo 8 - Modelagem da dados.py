class Produto:
    def __init__(self, codigo, nome, preco, quantidade_estoque):
        self.set_codigo(codigo)
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_quantidade_estoque(quantidade_estoque)

    def get_codigo(self):
        return self._codigo
    def set_codigo(self, codigo):
        if isinstance(codigo, str) and len(codigo) == 4:
            self._codigo = codigo
        else:
            raise ValueError("Código Inválido!")

    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome) > 0:
            self._nome = nome
        else:
            raise ValueError("Nome Inválido!")

    def get_preco(self):
        return self._preco
    def set_preco(self, preco):
        if isinstance(preco, (int,float)) and preco > 0:
            self._preco = preco
        else:
            raise ValueError("Preço Inválido!")

    def get_quantidade_estoque(self):
        return self._quantidade_estoque
    def set_quantidade_estoque(self, quantidade_estoque):
        if isinstance(quantidade_estoque, int) and quantidade_estoque > 0:
            self._quantidade_estoque = quantidade_estoque
        else:
            raise ValueError("Quantidade em estoque inválida!")

    def adicionar_estoque(self, adicionar_estoque):
        self._quantidade_estoque += adicionar_estoque
        print(f"Adicionado: {adicionar_estoque}. Agora o estoque é de: {self._quantidade_estoque}")

    def remover_estoque(self, quantidade):
        if isinstance(quantidade, int) and quantidade > 0:
            if quantidade <= self._quantidade_estoque:
                self._quantidade_estoque-=quantidade
                print(f"Quantidade em estoque: {self._quantidade_estoque}")
                return True
            else:
                print(f"Quantidade Insuficiente!")
                return False
        else:
            raise ValueError ("A quantidade deve ser maior que 0!")

    def calcular_total_estoque(self):
        return self._preco * self._quantidade_estoque

    def aplicar_desconto(self, percentual):
        if isinstance(percentual, (int, float)) and 0 < percentual <= 100:
            self._preco=self._preco-self._preco * (percentual / 100)
            print(f"Desconto Aplicado. Novo valor: R${self._preco:.2f}")
        else:
            print(f"O percentual de desconto deve ser maior entre 0 e 100!")

    def mostrar_informacoes(self):
        print("="*40)
        print(f"Código: {self._codigo}")
        print(f"Nome: {self._nome}")
        print(f"Preço: R${self._preco:.2f}")
        print(f"Estoque: {self._quantidade_estoque}")
        print(f"Total: {self.calcular_total_estoque()}")

class GestaoProdutos:
    def __init__(self):
        self._produtos = {}

    def Adicionar_produto(self, produto): #função so aceita produtos, armazena no dicionário
        if isinstance(produto, Produto):
            codigo = produto.get_codigo()
            if codigo not in self._produtos:
                self._produtos[codigo] = produto
                print(f"Produto: {codigo} adicionado!")
            else:
                print(f"Produto {codigo} ja existe!")

    def buscar_produtos (self, codigo):
        return self._produtos.get(codigo)

    def listar_produtos(self):
        if self._produtos:
            print("\n===LISTA DE PRODUTOS===")
            for produto in self._produtos.values(): #values pega todos os valores que estiver dentro do dicionário
                produto.mostrar_informacoes()
        else:
            print("Nenhum produto cadastrado!")

    def calcular_total_estoque(self):
        return sum(p.calcular_total_estoque() for p in self._produtos.values())

    def exibir_relatorio(self):
        print("="*40)
        print("RELATÓRIO DE ESTOQUE")
        print("="*40    )
        print(f"Total de Produtos: {len(self._produtos)}")
        print(f"Valor total: R${self.calcular_total_estoque():.2f}")

gestao=GestaoProdutos()

while True:
    print("[ 1 ] Adicionar produto")
    print("[ 2 ] Listar produtos")
    print("[ 3 ] Buscar produto")
    print("[ 4 ] Remover produto")
    print("[ 5 ] Relatório")
    print("[ 0 ] Sair")
    opcao = input("Escolha uma das opções: ")

    if opcao=="1":
        try:
            nome=input("Digite o nome do produto: ")
            codigo = input("Digite o código do produto: ")
            preco = float(input("Digite o preço R$: "))
            quantidade = int(input("Digite a quantidade: "))

            produto=Produto(codigo,nome,preco,quantidade)
            gestao.Adicionar_produto(produto)

        except ValueError as e:
            print(f"Erro {e}")

    elif opcao=="2":
        gestao.listar_produtos()

    elif opcao=="3":
        codigo=input("Digite o codigo do produto: ")
        produto=gestao.buscar_produtos(codigo)
        if produto:
            produto.mostrar_informacoes()
        else:
            print("Produto não encontrado!")

    elif opcao=="4":
        codigo = input("Digite o codigo do produto: ")
        produto=gestao.buscar_produtos(codigo)
        if produto:
            del gestao._produtos[codigo]
            print("Produto removido!")
        else:
            print("Produto não encontrado!")

    elif opcao=="5":
        gestao.exibir_relatorio()

    elif opcao=="0":
        print("Pesquisa finalizada!")
        break

    else:
        print("Opção invalida!")




