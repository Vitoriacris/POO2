
class Usuario:
    def __init__(self, nome, cpf):
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
    def nome(self, numcpf):
        self._cpf = self._cpf

    def cad(self):
        nome = input(print('Insira o nome:'))


class Produto:

    def __init__(self, codigo_produto, descricao, quant):
        self._codigo_produto = codigo_produto
        self._descricao = descricao
        self._quant = quant
        print('=-' * 20)
        print('Produto Cadastrado!')


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

    def add_produto(self, num):
        self._quant += num
        print('=-' * 20)
        print(f'{num} novas unidades foram adicionadas\nAo Produto do tipo: {self._descricao}')
        print(f'Agora o estoque desse produto tem: {self._quant} unidades')

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


class CadFuncionario(Usuario):

    def __init__(self, nome, cpf, cod):
        super().__init__(nome, cpf)
        self._cod = cod
        print('=-' * 20)
        print(f'Funcinario(a) {self._nome} Cadastrado(a)')

    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, cod2):
        self._cod = self._cod



#teste
pao = Produto(1234,"Pão",2)

funcionario1 = CadFuncionario('Maria',694000,123)


funcionario2 = CadFuncionario('Joao',694001,321)


pao.add_produto(4)


cliente1 = Usuario('Luana',6750111)
print(cliente1._nome)

pao.venda(cliente1,funcionario1,pao,4,pao._quant)
