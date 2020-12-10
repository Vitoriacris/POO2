class Usuario:
    def __init__(self):
        self._nome = input('Nome:')
        self._cpf = input('CPF:')

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

    def __init__(self):
        self._nome = input('Nome:')
        self._cpf = input('CPF:')
        self._cod = input('Codigo: ')

    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, cod2):
        self._cod = self._cod


class Estoque:
    def __init__(self):
        self.listaProduto = []
        print(self.listaProduto)
class Produto():
    def __init__(self,descricao=0, codigo_produto=0, quant=0, valor=0):
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


# Menu
estoque = Estoque()
menu = 1111

while menu != 0:
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
        Produto._descricao= input('Nome do produto:')
        Produto._codigo_produto= input("Codigo de ID: ")
        Produto._quant = input("Quantas unidades: ")
        Produto._valor = input("Valor da unidade: ")
        estoque.listaProduto.append(Produto._descricao)
        print('=-' * 20)
        print('Produto Cadastrado!')
        print(estoque.listaProduto)
    elif menu == '2':
        CadFuncionario()
        print('=-' * 20)
        print(f'Funcinario(a) Cadastrado(a)')

    elif menu == '3':
        Usuario()
        print('=-' * 20)
        print(f'Cliente Cadastrado')
    elif menu == '4':
        print('Opção Invalida')
    elif menu == '5':
        print('Opção Invalida')
    elif menu == '0':
        menu = False
        print('Até logo!')
    else:
        print('Opção Invalida')

# funcionario2 = CadFuncionario(321)

# pao.add_produto(4)

# print(cliente1._nome)
