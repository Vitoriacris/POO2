listaProduto = []
var = 1
q = 1

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

    def __init__(self, nome=0, cod=0):
        self._nome = nome
        self._cod = cod

    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self, cod2):
        self._cod = self._cod


class Produto():
    def __init__(self, descricao=0, quant=0, valor=0):
        self._descricao = descricao
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


fun = list()
listCli = list()


class Menu(CadFuncionario):
    def __init__(self, quant=0):
        super().__init__(quant)
        menu = 1

        while menu != '0':
            print('----------------------')
            print('===Sistema de estoque===')
            print('----------------------')
            print('[1] Produto')
            print('[2] Funcionario')
            print('[3] Cadastrar Cliente')
            print('[4] Realizar Venda')
            print('[0] SAIR')
            print('Escolha uma opção: ')
            menu = input()

            if menu == '1':
                print('[1] CADASTRAR Produto: ')
                print('[2] EXCLUIR Produto')
                print('[3] REPOR ESTOQUE')
                print('[4] LISTA DE PRODUTOS DISPONIVEIS')
                funcio = input(' ')
                if funcio == '1':
                    self._descricao = input('Nome do produto:')
                    self._quant = input("Quantas unidades: ")
                    self._valor = input("Valor da unidade: ")

                    listaProduto.append(self._descricao)
                    listaProduto.append(self._quant)
                    listaProduto.append(self._valor)

                    print('=-' * 20)
                    print('Produto Cadastrado!', listaProduto)

                elif funcio == '2':
                    self._descricao = input('Nome do Produto: ')
                    self._quant = input('Unidades disponiveis:')
                    self._valor = input('Valor: ')

                    if self._descricao in listaProduto and self._quant in listaProduto and self._valor in listaProduto:
                        listaProduto.remove(self._descricao)
                        listaProduto.remove(self._quant)
                        listaProduto.remove(self._valor)
                        print('PRODUTO EXCLUIDO', listaProduto)

                elif funcio == '3':
                    self._descricao = input('Nome do Produto: ')
                    self._quant = quant = (input('Unidades disponiveis:'))
                    self._valor = input('Valor: ')

                    if self._descricao in listaProduto and self._quant in listaProduto and self._valor in listaProduto:
                        listaProduto.remove(quant)
                        num = (input('Quantas Unidades deseja repor: '))
                        tot = int(quant + num)
                        listaProduto.append(tot)

                elif funcio == '4':
                    print(listaProduto)

            elif menu == '2':
                print('[1] CADASTRAR FUNCIONARIO: ')
                print('[2] EXCLUIR FUNCIONARIO')
                funcio = input(' ')

                if funcio == '1':
                    self._nome = input('Nome: ')
                    self._cod = input('Codigo:')
                    fun.append(self._nome)
                    fun.append(self._cod)
                    print('=-' * 20)
                    print(f'Funcinario(a) Cadastrado(a)')
                    print(fun)

                elif funcio == '2':
                    self._nome = input('Nome: ')
                    self._cod = input('Codigo:')

                    if self._nome in fun and self._cod in fun:
                        fun.remove(self._nome)
                        fun.remove(self._cod)
                    print('Funcionario Removido', fun)

            elif menu == '3':

                Usuario._nome = input('Nome: ')
                Usuario._cpf = input('CPF: ')
                listCli.append(Usuario._nome)
                listCli.append(Usuario._cpf)
                print('=-' * 20)
                print(f'Cliente Cadastrado')

            elif menu == '4':
                self._cod = input('Insira o codigo do vendedor:')
                if self._cod in fun:
                    self._nome = input('Nome do cliente:')

                    if self._nome in listCli:
                        self._descricao = input('Nome do produto que será vendido:')
                        q = input('Quantas unidades deseja vender:')

                        if self._descricao in listaProduto:

                            if self._quant <= q:
                                var = self._quant - q
                                listaProduto.append(var)
                                listaProduto.remove(self._quant)
                            else:
                                print('Quantidade indisponivel no estoque')
                        else:
                            print('Produto nao disponivel no estoque')
                    else:
                        print('Cliente não cadastrado!')
                else:
                    print('Funcionario não consta no sistema!')

        print('Até Logo...')


Menu()
