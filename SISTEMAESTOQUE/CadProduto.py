
class Usuario:
    def __init__(self,nome, cpf):
        self._nome=nome
        self._cpf=cpf
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nom):
        self._nome= nome
        
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def nome(self, numcpf):
        self._cpf=cpf
        
class CadFuncionario(Usuario):
    
    def __init__(self,nome, cpf, cod):
        super().__init__(nome, cpf)
        self._cod=cod
        
    @property
    def cod(self):
        return self._cod

    @cod.setter
    def cod(self,cod2):
        self._cod= cod



class Produto:
    
    def __init__(self,codigo_produto, descricao, quant):
        self._codigo_produto= codigo_produto
        self._descricao= descricao
        self._quant=quant

    @property
    def codigo_produto(self):
            return self._codigo_produto

    @codigo_produto.setter
    def codigo_produto(self,cod):
            self._codigo_produto= codigo_produto

    @property
    def descricao(self):
            return self._descricao

    @descricao.setter
    def descricao(self,descri):
            self._descricao = descricao

    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self,quant2):
         self._quant = quant
            
    def add_produto(self, num):
        self._quant+=num
        
            
    

   