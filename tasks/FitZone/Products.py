class Product:
    def __init__(self,id,descricao,marca,valor,estoque):
        self.id = id
        self.descricao = descricao
        self.marca = marca
        self.valor = valor
        self.estoque = estoque

    def incluir(self,valor):
        if valor >= 0 and valor + self.estoque <= 26:
            self.estoque += valor
        else:
            print("Coloque um valor positivo")

    def retirar(self,valor):
        if self.estoque >= valor and self.estoque != 0:
            self.estoque -= valor
        elif self.estoque == 0:
            print("Não temos mais desse produto")
        else:
            print("Coloque um valor positivo")