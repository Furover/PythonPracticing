class Conta():
  def __init__(self,numero,cpf,saldo,ativo):
    self.Numero = numero
    self.Cpf = cpf
    self.Saldo = saldo
    self.Ativo = ativo
  def Ativar(self):
    if self.Ativo == False:
      self.Ativo = True
    else:
      print("Ja ativou")
  def Debito(self,valor):
    if self.Ativo == True and self.Saldo - valor >= 0 and valor >= 0:
      self.Saldo = self.Saldo - valor
      print(self.Saldo)
    else:
      print("uhh, tá pedindo demaisss ou coloco negativo, que feio")
  def Credito(self,valor):
    if self.Ativo == True and valor >= 0 :
      self.Saldo = self.Saldo + valor
      print(self.Saldo)

class Poupanca(Conta):
  def __init__(self,diaAniversario, numero,cpf,saldo,ativo):
    super().__init__(numero,cpf,saldo,ativo)
    self.diaAniversario = diaAniversario
  def Correcao(self,data):
    if(self.diaAniversario == data):
      self.Saldo = (self.Saldo * 0.05) + self.Saldo

class Corrente(Conta):
  def __init__(self, numero,cpf,saldo,ativo, nTalao):
    super().__init__(numero,cpf,saldo,ativo)
    self.NTalao = nTalao
  def Talao(self, numero):
    if numero <= self.NTalao and numero >= 0:
      self.Saldo = self.Saldo - 30
      self.NTalao -= numero
    else:
       print("nananinanao")


class Especial(Conta):
  def __init__(self,limite, numero,cpf,saldo,ativo):
    super().__init__(numero,cpf,saldo,ativo)
    self.Limite = limite
  def Debito(self, limite):
    if self.Saldo - limite >= 0 and limite >= 0:
       self.Saldo -= limite
    elif self.Saldo + self.Limite - limite >= 0 and limite >= 0:
      self.Limite = self.Limite + self.Saldo - limite
      self.Saldo = 0
    else:
       print("Falta de saldo, realize um credito")

class Empresa(Conta):
    def __init__(self, numero,cpf,saldo,ativo,limEmprestimo):
        super().__init__(numero,cpf,saldo,ativo)
        self.LimEmpresitmo = limEmprestimo
    def Emprestimo(self, emprestimo):
        if emprestimo <= self.LimEmpresitmo and emprestimo >= 0:
            self.Saldo = emprestimo + self.Saldo
            self.LimEmpresitmo = self.LimEmpresitmo - emprestimo
        else:
           print("Tá pedindo demaisssss!!!!!")

class Estudantil (Conta):
    def __init__(self, numero,cpf,saldo,ativo,limite):
        super().__init__(numero,cpf,saldo,ativo)
        self.Limiteimite = limite
    def Emprestimo(self, emprestimo):
        if emprestimo <= self.Limiteimite and emprestimo >= 0:
            self.Saldo = emprestimo + self.Saldo
            self.Limiteimite = self.Limiteimite - emprestimo
        else:
           print("Tá pedindo demaisssss!!!!!")








