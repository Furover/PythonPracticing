import pymysql as psql
import random as rdm
import time
from Accounts import *
from Products import *

conta = Account(None,None,None)

connection = psql.connect(
    host="localhost",
    user="root",
    password="root",
)

cursor = connection.cursor()

cursor.execute("create database if not exists fitzone")

connection.commit()

connection = psql.connect(
    host="localhost",
    user="root",
    password="root",
    database="fitzone"
)

cursor = connection.cursor()

cursor.execute("create table if not exists usuarios (id int unsigned not null auto_increment primary key,email varchar(255) not null,senha varchar(255) not null,created_at timestamp not null default CURRENT_TIMESTAMP)")
connection.commit()
cursor.execute("create table if not exists produtoacademia (id_produtoacademia int unsigned not null auto_increment primary key,descricao varchar(255) not null,marca varchar(255) not null,valor FLOAT not null,estoque INT not null default 0,created_at timestamp not null default CURRENT_TIMESTAMP)")
connection.commit()

def Cadastro():
    try:
        print("Cadastrar Item")
        desc = input("Qual a descrição do item?: ")
        marca = input("Qual a marca do item?: ")
        valor = float(input("Qual o valor do item?: "))
        item = Product(None,desc,marca,valor,0)
        cursor.execute("insert into produtoacademia(descricao,marca,valor) values(%s,%s,%s)",(item.descricao,item.marca,item.valor))
        connection.commit()
        print("Item cadastrado com sucesso!")
        time.sleep(5)
    except:
        print("Ocorreu um erro no cadastro, tente novamente.")
        time.sleep(3)

def Atualizar():
    try:
        print("Atualizar Item")
        cursor.execute("select * from produtoacademia")
        itens = cursor.fetchall()
        if len(itens) > 0:
            while True:
                for i in itens:
                    print(i)
                change = input("Qual o id do item que deseja alterar?: ")
                cursor.execute("select * from produtoacademia where id_produtoacademia = %s",change)
                response = cursor.fetchall()
                if len(response) > 0:
                    item = Product(response[0][0],response[0][1],response[0][2],response[0][3],response[0][4])
                    op = input("Deseja adicionar ou remover do estoque desse item?(A/R): ").upper()
                    if op == 'A':
                        amount = int(input("Quanto você deseja adicionar?: "))
                        item.incluir(amount)
                        cursor.execute("update produtoacademia set estoque = %s where id_produtoacademia = %s",(item.estoque,item.id))
                        connection.commit()
                        time.sleep(3)
                        break
                    elif op == 'R':
                        amount = int(input("Quanto você deseja remover?: "))
                        item.retirar(amount)
                        cursor.execute("update produtoacademia set estoque = %s where id_produtoacademia = %s",(item.estoque,item.id))
                        connection.commit()
                        time.sleep(3)
                        break
                else:
                    print("Não achei")
                    time.sleep(1)
        else:
            print("Não temos itens para atualizar no momento.")
            time.sleep(3)
    except:
        print("Ocorreu um erro na atualização, tente novamente.")
        time.sleep(3)

def Comprar():
    global conta
    try:
        print("Comprar Item")
        cursor.execute("select id_produtoacademia, descricao, marca, valor, estoque from produtoacademia")
        itens = cursor.fetchall()
        if len(itens) > 0:
            while True:
                for i in itens:
                    print(i)
                change = input("Qual o id do item que deseja comprar?: ")
                cursor.execute("select id_produtoacademia, descricao, marca, valor, estoque from produtoacademia where id_produtoacademia = %s",change)
                response = cursor.fetchall()
                if len(response) > 0:
                    item = Product(response[0][0],response[0][1],response[0][2],response[0][3],response[0][4])
                    qtde = int(input("Quantos você quer desse produto?: "))
                    if item.estoque > 0 and qtde <= item.estoque and qtde > 0:
                        if len(conta.carrinho) > 0:
                            yatiene = False
                            for i in conta.carrinho:
                                if response[0][0] == i[0]:
                                    yatiene = True
                            if yatiene:
                                print("Você já tem esse item no seu carrinho")
                            else:
                                conta.incluir([response[0][0],response[0][1],response[0][2],response[0][3],response[0][4],qtde])
                                print("Item adicionado no carrinho com sucesso!")
                            time.sleep(3)
                            break
                        else:
                            conta.incluir([response[0][0],response[0][1],response[0][2],response[0][3],response[0][4],qtde])
                            print("Item adicionado com sucesso!")
                            time.sleep(3)
                            break
                    else:
                        print("Não temos estoque suficiente desse produto no momento.")
                        time.sleep(3)
                        break
                    
                else:
                    print("Não achei")
                    time.sleep(1)
        else:
            print("Não temos itens no momento.")
            time.sleep(3)
    except:
        print("Ocorreu um erro durante a compra, tente novamente. ")
        time.sleep(3)


def Carrinho():
    global conta
    finalPrice = 0
    try:
        print("Carrinho")
        if len(conta.carrinho) > 0:
            for i in conta.carrinho:
                print("Nome: ",i[1], " Valor: ",i[3], " Quantidade: ",i[5])
            op = input("Deseja finalizar a compra?(S/N): ").upper()
            if op == 'S':
                for i in conta.carrinho:
                    id = i[0]
                    value = i[3]
                    amount = i[5]
                    stock = i[4] - amount
                    finalPrice += value * amount
                    cursor.execute("update produtoacademia set estoque = %s where id_produtoacademia = %s",[stock,id])
                    connection.commit()
                print("Itens Comprados: ")
                for i in conta.carrinho:
                    print("Nome: ",i[1], " Valor: ",i[3], " Quantidade: ",i[5])
                print("Preço final: ",finalPrice)
                conta.retirar()
                time.sleep(4)
            else:
                pass
        else:
            print("Seu carrinho está vazio!")
            time.sleep(3)
    except:
        print("Ocorreu um erro durante a compra, tente novamente. ")
        time.sleep(3)
try:
    while True:
        if conta.email != None:
            print(f"Seja bem vindo a FitZone!!!\nEmail logado: {conta.email}\nO que deseja fazer?\n1 - Cadastrar Item\n2 - Atualizar Item\n3 - Colocar Itens no Carrinho\n4 - Ver Carrinho\n5 - Sair")
            op = input("Opção ")
            if op == '1':
                Cadastro()
            elif op == '2':
                Atualizar()
            elif op == '3':
                Comprar()
            elif op == '4':
                Carrinho()
        else:
            op = input("Parece que você não está cadastrado! Deseja fazer login ou criar uma conta?(L/C)").upper()
            if op == "L":
                email = input("Qual o email da conta?: ")
                senha = input("Qual a senha?: ")
                cursor.execute("select * from usuarios where email = %s and senha = %s",[email,senha])
                response = cursor.fetchall()
                if len(response) > 0:
                    print("Seja bem vindo!")
                    conta = Account(response[0][0],response[0][1],[])
                else:
                    print("Não Achei!")
            elif op == "C":
                email = input("Qual o email que deseja cadastrar?: ")
                senha = input("Digite uma senha para sua nova conta: ")
                conta = Account(None,email,[])
                cursor.execute("insert into usuarios(email,senha) values(%s,%s)",(conta.email,senha))
                connection.commit()
except:
    print("Ocorreu um erro: ")