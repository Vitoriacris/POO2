class Usuario:
    def __init__(self, nome=0, cpf=0):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nom):
        self._nome = self._nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, numcpf):
        self._cpf = self._cpf


class CadFuncionario(Usuario):

    def __init__(self,nome=0, cod=0):
        self._nome = nome
        self._cod = cod


    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, cod2):
        self._cod = self._cod


class Lista:
    def __init__(self):
        self.listaProduto = []
        self.listFun = []
        self.listCli = []


class Produto():
    def __init__(self, descricao=0, codigo_produto=0, quant=0, valor=0):
        self._descricao = descricao
        self._codigo_produto = codigo_produto
        self._quant = quant
        self._valor = valor

    @property
    def codigo_produto(self):
        return self._codigo_produto

    @codigo_produto.setter
    def codigo_produto(self, cod):
        self._codigo_produto = self._codigo_produto

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descri):
        self._descricao = self._descricao

    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self, quant2):
        self._quant = self._quant

    def venda(self, cliente, funcionario, produto, quantidade, quant):

        self._cliente = cliente
        self._funcionario = funcionario
        self._produto = produto
        self._quantidade = quantidade

        if self._quantidade > self._quant:
            print('=-' * 20)
            print('Quantidade indisponivel no estoque')
        else:
            self._quant = self._quant - self._quantidade
            print('=-' * 20)
            print(f'Venda Efetuada!')
            print(f'Produto: {self._descricao}')
            print(f'Vendedor(a): {funcionario._nome}')
            print(f'Cliente: {cliente._nome}')


class addProduto(Produto):
    def __init__(self):
        num = input('Quantas Unidades deseja repor: ')
        self._quant += num
        estoque.listaProduto.insert(2,self.quant)


# Menu

estoque = Lista()
fun = Lista()
cli= Lista()
lista2 = []
menu = 1
while menu != '0':
    print('Sistema de estoque')
    print('Escolha uma opção: ')
    print('[1] Cadastrar Produto')
    print('[2] Cadastrar Funcionario')
    print('[3] Cadastrar Cliente')
    print('[4] Realizar Venda')
    print('[5] Repor estoque')
    print('[0] SAIR')
    menu = input()

    if menu == '1':
        Produto._descricao = input('Nome do produto:')
        Produto._codigo_produto = input("Codigo de ID: ")
        Produto._quant = input("Quantas unidades: ")
        Produto._valor = input("Valor da unidade: ")
        estoque.listaProduto.append(Produto._descricao)
        estoque.listaProduto.append(Produto._codigo_produto)
        estoque.listaProduto.append(Produto._quant)
        print('=-' * 20)
        print('Produto Cadastrado!')
        print(estoque.listaProduto)

    elif menu == '2':
        CadFuncionario._nome= input('Nome: ')
        CadFuncionario._cod= input('Codigo:')
        fun.listFun.append(CadFuncionario._nome)
        fun.listFun.append(CadFuncionario._cod)
        print('=-' * 20)
        print(f'Funcinario(a) Cadastrado(a)')
        print(fun.listFun)

    elif menu == '3':
        Usuario._nome= input('Nome: ')
        Usuario._cpf= input('CPF: ')
        cli.listCli.append(Usuario._nome)
        cli.listCli.append(Usuario._cpf)
        print('=-' * 20)
        print(f'Cliente Cadastrado')

    elif menu == '4':
        print('Opção Invalida')

    elif menu == '5':
        p = input('Digite o codigo do produto que desejar repor: ')
        if p in estoque.listaProduto:
            addProduto()
            print(estoque.listaProduto)

print('Até Logo...')
# funcionario2 = CadFuncionario(321)

# pao.add_produto(4)

# print(cliente1._nome)
415