class Account:
    def __init__(self,id,email,carrinho):
        self.id = id
        self.email = email
        self.carrinho = carrinho

    def incluir(self,item):
        self.carrinho.append(item)

    def retirar(self):
        self.carrinho = []