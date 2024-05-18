import pymysql as psql
import random as rdm
from products import Produto
import time

P = Produto(None,None,None,None,None)

connection = psql.connect(
    host="localhost",
    user="root",
    password="root",
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS DBLOJA")

connection.commit()

connection = psql.connect(
    host="localhost",
    user="root",
    password="root",
    database="DBLOJA"
)

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS PRODUTOS (ID int unsigned not null auto_increment primary key,CODIGO varchar(255) not null,NOME varchar(255) not null,VALOR FLOAT not null,ESTOQUE INT not null DEFAULT 0)")

connection.commit()

while True:
    print("Escolha sua opção:\n1 - Cadastrar\n2 - Alterar\n3 - Listar\n4 - Excluir\n5 - Movimentar\n6 - Sair")
    op = input("Opção ")
    if op == '6':
        print("Até breve")
        break

    if op == '1':
        codigo = rdm.randint(0,999999)
        nome = input("Qual o nome do produto?: ")
        valor = float(input("Qual o valor do produto?: "))
        dados = [codigo,nome,valor]
        cursor.execute("INSERT INTO PRODUTOS(CODIGO,NOME,VALOR) VALUES(%s,%s,%s)",dados)
        #id = cursor.execute("SELECT LAST_INSERT_ID()")
        connection.commit()

    if op == '2':
        while True:
            try:
                codigo = input("Qual o código do produto?: ")
                cursor.execute("select * from PRODUTOS where CODIGO = %s limit 1",codigo)
                dado = cursor.fetchall()
                if len(dado) > 0:
                    print("Achei!")
                    print("ID, CODIGO, NOME, VALOR, ESTOQUE")
                    for el in dado:
                        print(el)
                    nome = input("Qual o novo nome do produto?: ")
                    valor = float(input("Qual o novo valor do produto?: "))
                    estoque = int(input("Qual o novo estoque do produto?: "))
                    dados = [nome,valor,estoque,codigo]
                    cursor.execute("UPDATE PRODUTOS SET NOME = %s, VALOR = %s, ESTOQUE = %s WHERE CODIGO = %s",dados)
                    connection.commit()
                    print("Item atualizado com sucesso!")
                    time.sleep(5)
                    break
                else:
                    print("Não achei!")
            except:
                print("Ocorreu um erro durante a atualização! Tente novamente.")

    if op == '3':
        cursor.execute("SELECT * FROM PRODUTOS LIMIT 10")
        lista = cursor.fetchall()
        print("ID, CODIGO, NOME, VALOR, ESTOQUE")
        for el in lista:
            print(el)
        time.sleep(5)

    if op == '4':
        while True:
            try:
                codigo = input("Qual o código do produto?: ")
                cursor.execute("select * from PRODUTOS where CODIGO = %s limit 1",codigo)
                dado = cursor.fetchall()
                #item = Produto(*dado) #Quebra a lista e coloca dentro da classe
                if len(dado) > 0:
                    print("Achei!")
                    print("ID, CODIGO, NOME, VALOR, ESTOQUE")
                    for el in dado:
                        print(el)
                    while True:
                        certeza = input("Quer deletar esse item mesmo?(S/N): ").upper()
                        if certeza == "S":
                            cursor.execute("DELETE FROM PRODUTOS WHERE CODIGO = %s",codigo)
                            connection.commit()
                            print("Item deletado com sucesso!")
                            time.sleep(5)
                            break
                        elif certeza == "N":
                            break
                        else:
                            print("Não tenta ser engraçado.")
                    break
                else:
                    print("Não achei!")
            except:
                print("Ocorreu um erro durante a atualização! Tente novamente.")

    if op == '5':
        while True:
            try:
                codigo = input("Qual o código do produto?: ")
                cursor.execute("select * from PRODUTOS where CODIGO = %s limit 1",codigo)
                dado = cursor.fetchall()
                if len(dado) > 0:
                    print("oii")
                else:
                    print("Não achei!")
            except:
                print("Ocorreu um erro durante a atualização! Tente novamente.")

