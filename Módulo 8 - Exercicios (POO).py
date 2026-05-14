#exercicio1
import math #trazer o número do pi

class Circulo:
    def __init__(self, raio):
        self.raio=raio

    def calcular_area(self):
        area = math.pi * self.raio**2
        return area

    def calcular_perimetro(self):
        perimetro = 2*math.pi*self.raio
        return perimetro

    def exibir_info(self):
        text=f"""
Este círculo possui raio: {self.raio}
Sua área é igual a: {self.calcular_area():.2f}
E seu perímetro é: {self.calcular_perimetro():.2f}
"""
        return text

Raio=int(input("Digite o raio do circulo: "))
circulo1=Circulo(Raio)
info=circulo1.exibir_info()
print(info)

#exercicio2
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_atual = 0

    def acelerar(self, quantidade):
        self.velocidade_atual+=quantidade

    def frear(self, quantidade):
        self.velocidade_atual= max(0, self.velocidade_atual - quantidade) #max age como um limitador, pra velocidade nunca ficar negativa

    def exibir_info(self):
        print(f"Carro: {self.marca}, modelo: {self.modelo}, ano: {self.ano}")
        print(f"Velocidade atual: {self.velocidade_atual:.2f}km/h")

Marca=input("Digite a marca do carro: ")
Modelo=input("Digite o modelo do carro: ")
Ano=int(input("Digite o ano do carro: "))
Aceleração=float(input("Qual a acelaração do carro?: "))
Frenagem=float(input("Qual a freanagem do carro?: "))
carro1=Carro(Marca, Modelo, Ano)
carro1.acelerar(Aceleração)
carro1.frear(Frenagem)
informações=carro1.exibir_info()

#exercicio3
class Retangulo:
    def __init__(self, altura, largura):
        self._altura=altura
        self._largura=largura

    def get_altura(self):
        return self._altura
    def set_altura(self, altura):
        if isinstance(altura, (float, int)) and altura > 0:
            self._altura=altura
        else:
            raise ValueError ("Altura deve ser um número maior que 0")

    def get_largura(self):
        return self._largura
    def set_largura(self, largura):
        if isinstance(largura, (float, int)) and largura > 0:
            self._largura = largura
        else:
            raise ValueError ("Largura deve ser um número maior que 0")

    def calcular_area(self):
        return self._altura*self._largura

altura=float(input("Qual a altura do Retangulo?: "))
largura=float(input("Qual a largura do Retangulo?: "))
retangulo1=Retangulo(altura,largura)
print(f"Altura: {retangulo1.get_altura()}. Largura: {retangulo1.get_largura()}")
print(f"Área: {retangulo1.calcular_area()}")

retangulo1.set_largura(10)
print(f"Nova Área: {retangulo1.calcular_area()}")

#exercicio4
class Conta_bancária:
    def __init__(self, titular, saldo_inicial=0):
        self.titular=titular
        self.saldo=saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Valor depositado: R${valor}. Saldo: R${self.saldo}")
        else:
            print("O valor depositado deve ser maior que 0!")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Valor Sacado: {valor}. Saldo: {self.saldo}")
        else:
            print("O valor inválido ou saldo insuficiente!")

    def exibir (self):
        print(f"Titular: {self.titular}. Saldo: R${self.saldo}")

nome=input("Qual o nome do titular da conta?: ")
conta=Conta_bancária(nome)

while True:
    print("[ 1 ] Sacar")
    print("[ 2 ] Depositar")
    print("[ 3 ] Ver saldo")
    print("[ 4 ] Sair")
    opcao=input("Escolha uma das opções: ")

    if opcao=="1":
        valor=float(input("Digite o valor que deseja sacar: R$"))
        conta.sacar(valor)
    elif opcao=="2":
        valor = float(input("Digite o valor que deseja depositar: R$"))
        conta.depositar(valor)
    elif opcao=="3":
        conta.exibir()
    elif opcao=="4":
        print("Serviço finalizado!")
        break
    else:
        print("Opção inválida!")

#exercicio5
class Aluno:
    def __init__(self, nome, rm):
        self.nome = nome
        self.set_rm (rm)
        self.notas = []

    def get_rm(self):
        return self.rm

    def set_rm(self, rm):
        if isinstance(rm, int) and 100000 <= rm <= 999999:
            self.rm=rm
        else:
            raise ValueError("O RM deve conter exatamente 6 dígitos!")

    def adicionar_nota(self, nota):
        if nota >=0 and nota<=10:
            self.notas.append(nota)
        else:
            print("A nota deve ser entre 0 e 10")

    def calcular_media(self):
        if self.notas:
            return sum(self.notas)/len(self.notas)
        else:
            return 0

    def verificacao(self):
        if self.calcular_media()>=7:
            return "Aprovado"
        else:
            return "Reprovado"

    def exibir_info(self):
        print(f"Aluno: {self.nome}")
        print(f"RM: {self.rm}")
        print(f"Notas: {self.notas}")
        print(f"Média: {self.calcular_media():.2f}")
        print(f"Resultado: {self.verificacao()}")

nome=input("Digite o nome do aluno: ")
rm=int(input("Digite o RM do aluno: "))
aluno=Aluno(nome, rm)

n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
n4=float(input("Digite a quarta nota: "))

aluno.adicionar_nota(n1)
aluno.adicionar_nota(n2)
aluno.adicionar_nota(n3)
aluno.adicionar_nota(n4)
aluno.exibir_info()

#exercício6
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} faz um som")

class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz Miau Miau!")

class Vaca(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz Muuu!")

class Galinha(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz Pó Pó Pó!")

class Bezerro(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz Bé Bé Bé!")

while True:
    print("[ 1 ] Cachorro")
    print("[ 2 ] Gato")
    print("[ 3 ] Vaca")
    print("[ 4 ] Galinha")
    print("[ 5 ] Bezerro")
    print("[ 6 ] Sair")
    opcao=input("Escolha um dos animais para ver o som: ")

    if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":
        nome_animal=input("Digite o nome do animal: ")

        if opcao == "1":
            animal=Cachorro(nome_animal)
            animal.fazer_som()

        elif opcao == "2":
            animal = Gato(nome_animal)
            animal.fazer_som()

        elif opcao == "3":
            animal = Vaca(nome_animal)
            animal.fazer_som()

        elif opcao == "4":
            animal = Galinha(nome_animal)
            animal.fazer_som()

        elif opcao == "5":
            animal = Bezerro(nome_animal)
            animal.fazer_som()

    else:
        opcao == "6"
        print("Serviço finalizado!")
        break

#exercicio7
class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade

    def informações(self):
        print("Cliente Cadastrado!")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Cliente(Pessoa):
    def __init__(self, nome, idade, senha):
        super().__init__(nome,idade)
        self.set_senha(senha)

    def get_senha(self):
        return self.senha
    def set_senha(self, senha):
        if isinstance(senha, int) and 100000 <= senha <= 999999:
            self.senha=senha
        else:
            raise ValueError("A senha deve conter exatamente 6 dígitos!")

    def informações(self):
        super().informações()
        print(f"Senha: {self.senha}")

nome=input("Qual o seu nome?: ")
idade=int(input("Qual a sua idade?: "))
if idade < 18:
    print("Cadastro não permitido para menores de 18 anos.")
else:
    pessoa=Pessoa(nome,idade)
    senha=int(input("Qual a sua senha?: "))
    cliente=Cliente(nome,idade,senha)
    cliente.informações()

#exercicio8
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_quantidade(quantidade)

    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) > 0:
            self._nome=nome.strip() #strip remove espaços aleatórios
        else:
            raise ValueError("Nome inválido!")

    def get_preco(self):
        return self._preco
    def set_preco(self, preco):
        if isinstance(preco, (int, float)) and preco >= 0:
            self._preco=preco
        else:
            raise ValueError("Preço Inválido: o valor deve positivo!")

    def get_quantidade(self):
        return self._quantidade
    def set_quantidade(self, quantidade):
        if isinstance(quantidade, int) and quantidade > 0:
            self._quantidade=quantidade
        else:
            raise ValueError("A quantidade deve ser maior que 0!")

    def total(self):
        return self._preco * self._quantidade

produto=input("Informe o nome do produto: ")
preco=float(input("Informe o preço do produto R$: "))
quantidade=int(input("Informe a quantidade de produtos: "))
compra=Produto(produto, preco, quantidade)
print(f"Produto: {compra.get_nome()}")
print(f"Preço: R${compra.total():.2f}")

#exercicio9
class Funcionário:
    def __init__(self, nome, salario):
        self.nome = nome
        self.set_salario(salario)

    def get_salaraio(self):
        return self.salario
    def set_salario(self, salario):
        if isinstance(salario, float) and salario > 0:
            self.salario=salario
        else:
            raise ValueError("Salário deve ser maior que zero!")

    def info(self):
        print("Funcionário Cadastrado!")
        print(f"Funcionário: {self.nome}")
        print(f"Salário: R${self.salario:.2f}")

class Gerente(Funcionário):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def info(self):
        super().info()
        print(f"Setor: {self.setor}")

nome=input("Digite o nome do funcionário: ")
salario=float(input("Digite o salário do funcionário R$: "))
setor=input("Digite o setor: ")
funcionario=Gerente(nome, salario, setor)
funcionario.info()

#exercício10
class Aluno:
    def __init__(self, nome, idade, serie, turma, rm):
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_serie(serie)
        self.set_turma(turma)
        self.set_rm(rm)
        self.notas=[]

    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) > 0:
            self.nome=nome.strip()
        else:
            raise ValueError("Nome inválido!")

    def get_idade(self):
        return self.idade
    def set_idade(self, idade):
        if isinstance(idade, int) and 0<idade<100:
            self.idade=idade
        else:
            raise ValueError("Idade deve ser maior que 0!")

    def get_serie(self):
        return self.serie
    def set_serie(self, serie):
        if isinstance(serie, int) and 1<=serie<=3:
            self.serie=serie
        else:
            raise ValueError("Serie inválida!")

    def get_turma(self):
        return self.turma
    def set_turma(self, turma):
        turmas_validas=["edi","nutri","adm"]
        if isinstance(turma, str) and turma.lower() in turmas_validas:
            self.turma=turma
        else:
            raise ValueError("Turma inválida! Use Edi, Nutri ou Adm!")

    def get_rm(self):
        return self.rm
    def set_rm(self, rm):
        if isinstance(rm, int) and 100000 <= rm <= 999999:
            self.rm=rm
        else:
            raise ValueError("O RM deve conter exatamente 6 dígitos!")

    def adicionar_notas(self,nota):
        if isinstance(nota, (int, float)) and 0<=nota<=10:
            print(f"Nota: {nota} adicionada!")
            self.notas.append(nota)
        else:
            print("As notas devem ser entre 0 e 10!")

    def calcular_media(self):
        return sum(self.notas)/len(self.notas)

    def status_final(self):
        return "Aprovado" if self.calcular_media()>=7 else "Reprovado"

    def info(self):
        print("Cadastro Finalizado!")
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Serie: {self.serie}")
        print(f"Turma: {self.turma}")
        print(f"RM: {self.rm}")
        print(f"Média: {self.calcular_media()}")
        print(f"Status final: {self.status_final()}")

nome=input("Digite o nome do aluno: ")
idade=int(input("Digite a idade: "))
serie=int(input("Digite o serie do aluno: "))
turma=input("Digite o turma do aluno: ")
rm=int(input("Digite o rm do aluno: "))
n1=float(input("Digite a 1° nota do aluno: "))
n2=float(input("Digite a 2° nota do aluno: "))
n3=float(input("Digite a 3° nota do aluno: "))
n4=float(input("Digite a 4° nota do aluno: "))
aluno=Aluno(nome,idade,serie,turma,rm)
aluno.adicionar_notas(n1)
aluno.adicionar_notas(n2)
aluno.adicionar_notas(n3)
aluno.adicionar_notas(n4)
aluno.info()
