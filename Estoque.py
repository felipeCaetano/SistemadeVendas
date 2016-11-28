from produtos import *


class Estoque(object):
    def __init__(self):
        self.categorias = []
        self.subcategorias = []
        self.produtos = []
        self.menu_estoque()

    def save_categoria(self, categoria):
        pass

    def save_subcategorias(self, subcategoria):
        pass

    def save_produtos(self, produto):
        pass

    def create_categoria(self):
        """"
        Cria uma categoria através dos dados recolhidos pelo formulário.
        Os dados são: Codigo, nome e descrição
        """
        print("- Criar CATEGORIA -")
        codigo = input("CÓDIGO: ").strip()
        nome = input("NOME: ").strip()
        descrição = input("DESCRIÇÃO: ").strip()
        categoria = Categoria(codigo, nome, descrição)
        if categoria not in self.categorias:
            self.categorias.append(categoria)

    def create_subcategoria(self):
        """"
        Cria uma categoria através dos dados recolhidos pelo formulário.
        Os dados são: Codigo, nome e descrição e a passagem de um objeto categoria
        """
        if len(self.categorias) == 0:
            print("Você deve criar pelo menos uma CATEGORIA!\n")
            self.create_categoria()
        print("- Criar SUBCATEGORIA -")
        codigo = input("CÓDIGO: ").strip()
        nome = input("NOME: ").strip()
        descrição = input("DESCRIÇÃO: ").strip()
        escolhe = input("CATEGORIA (Nome ou Código): ")
        categoria = 0

        for cat in self.categorias:
            if cat.nome == escolhe or cat.codigo == escolhe:
                categoria = cat
                break
            else:
                print("Categoria não Encontrada!\nVocê deve criar uma CATEGORIA!")
                self.create_categoria()

        subcategoria = Subcategoria(categoria, codigo, nome, descrição)

        if subcategoria not in self.subcategorias:
            self.subcategorias.append(subcategoria)

    def create_produto(self):
        pass

    # funcionalidade pedida na especificação

    def low_stock_alarm(self):  # aviso de estoque baixo
        pass

    def consulta_estoque(self):    # exibe itens disponiveis no estoque
        print("Exibindo estoque")
        for categoria in self.categorias:
            print(categoria, end=" ")
        print()
        for subcategoria in self.subcategorias:
            print(subcategoria, end=" ")
        print()
        print(self.produtos)

        self.menu_estoque()

    def altera_item(self):      # altera um item disponivel no estoque
        print("alterando item do estoque")
        self.menu_estoque()

    def remove_item(self):    # remove um item disponivel no estoque - n remover se o item ainda tem produtos no estoque
        print("Removendo item do estoque")
        self.menu_estoque()

    def adiciona_item(self):     # adiciona novo item ao estoque
        print("Adicionando item ao estoque")
        while 1:
            print("************* Menu Adicionar: ******************")
            print("Digite Ação!\n1 - Adicionar Categoria\n2 - Adicionar Subcategoria\n3 - Adicionar Produtos\n4 - Sair")
            opcao = input()
            while not self.valida_opcao(opcao):
                print("Opção Inválida!")
                opcao = input()
            if opcao == '1':
                self.create_categoria()
            elif opcao == '2':
                self.create_subcategoria()
            elif opcao == '3':
                pass
            elif opcao == '4':
                break
        self.menu_estoque()

    def menu_estoque(self):
        print("Sistema de Vendas ao Consumidor")
        print("****** MENU DE ESTOQUE *****")
        print("Digite Ação!\n1 - Consultar Estoque\n2 - Adicionar\n3 - Remover\n4 - Alterar")
        opcao = input()

        while not self.valida_opcao(opcao):
            print("Opção Inválida!")
            opcao = input()

        if opcao == '1':
            self.consulta_estoque()
        elif opcao == '2':
            self.adiciona_item()
        elif opcao == '3':
            self.remove_item()
        elif opcao == '4':
            self.altera_item()

    def valida_opcao(self, opcao):
        if opcao.isdigit():
            return True
        else:
            return False

estoque = Estoque()
