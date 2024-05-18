class Produto:
    def __init__(self,id,codigo,nome,valor,estoque):
        self.id = id
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

    def incluir(self,valor):
        if valor >= 0:
            self.estoque += valor
        else:
            print("Não")

    def retirar(self,valor):
        if valor >= 0 and self.estoque >= valor:
            self.estoque -= valor
        else:
            print("Não")

    def __str__(self):
        return "Dados do produto: id: ",self.id," codigo: ",self.codigo," nome: ",self.nome," valor: ",self.valor," estoque: ",self.estoque