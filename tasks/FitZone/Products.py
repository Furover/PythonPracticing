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
            print("Item atualizado com sucesso!")
        elif self.estoque + valor > 26:
            print("Não conseguimos ter tanto estoque")
        else:
            print("Coloque um valor positivo")

    def retirar(self,valor):
        if self.estoque >= valor and self.estoque != 0:
            self.estoque -= valor
            print("Item atualizado com sucesso!")
        elif self.estoque == 0:
            print("Não temos mais desse produto")
        elif self.estoque - valor < 0:
            print("Não é possível remover tanto do estoque")
        else:
            print("Coloque um valor positivo")