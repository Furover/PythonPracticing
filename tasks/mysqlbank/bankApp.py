from accounts import *
import pymysql
import random

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank"
)

cursor = connection.cursor()

P1 = Poupanca(None,None,None,None,None)
C1 = Corrente(None,None,None,None,None)
E1 = Especial(None,None,None,None,None)
EM1 = Empresa(None,None,None,None,None)
ES1 = Estudantil(None,None,None,None,None)

def Poupation():
    global P1
    try:
        while True:
            if P1.Numero != None:
                for i in range(10):
                    print("Saldo atual :", P1.Saldo)
                    print("Movimento : D - Debito, C - Credito")
                    op = input("Opção ")
                    if op == "D" or op == "d":
                        if P1.Saldo == 0:
                            print("Saldo insuficiente faça um Credito")
                        else:
                            P1.Debito(float(input("Valor para debitar: ")))
                            bonitin = (P1.Saldo,P1.Numero)
                            cursor.execute("update Poupanca set saldo = %s where numero = %s",bonitin)
                            connection.commit()
                    elif op == "C" or op == "c":
                        P1.Credito(float(input("Valor para Credito: ")))
                        bonitin = (P1.Saldo,P1.Numero)
                        cursor.execute("update Poupanca set saldo = %s where numero = %s",bonitin)
                        connection.commit()
                print("Saldo atual :", P1.Saldo)
                P1.Correcao(int(input("Qual o dia de hj?: ")))
                bonitin = (P1.Saldo,P1.Numero)
                cursor.execute("update Poupanca set saldo = %s where numero = %s",bonitin)
                connection.commit()
                print("Saldo atual :", P1.Saldo)
                break
            else:
                opof = input("Parece que você não tem uma conta! Quer criar uma ou logar?(C/L)")
                if opof == "C" or opof == "c":
                    num = random.randint(0,999999)
                    cred = input("Qual seu cpf?: ")
                    niver = int(input("Qual a data de seu nascimento?: "))
                    if niver > 0 and niver <= 31 and len(cred) == 11:
                        data = (num,cred,niver)
                        cursor.execute("insert into Poupanca (numero, cpf, dia_aniversario) values(%s,%s,%s)", data)
                        connection.commit()
                        P1 = Poupanca(niver,num,cred,0,True)
                        print("Conta criada!")
                        print(f"Numero da sua conta: {num}")
                    else:
                        print("Tentou ser engraçadinho?")
                if opof == "L" or opof == "l":
                    opnum = input("Qual o numero da sua conta?: ")
                    cursor.execute("select * from Poupanca where numero = %s limit 1",opnum)
                    data = cursor.fetchall()
                    if len(data) > 0:
                        print("Achei sua conta!")
                        P1 = Poupanca(data[0][4],data[0][1],data[0][2],data[0][3],True)
                    else:
                        print("Não achei")
    except Exception as e:
        print(e)

def Correnting():
    global C1
    correte = False
    dont = True
    try:
        while dont:
            if C1.Numero != None:
                print(f"Olá conta: {C1.Numero}!")
                for i in range(10):
                    print("Saldo atual :", C1.Saldo)
                    print("Movimento : D - Debito, C - Credito, S - Sair")
                    op = input("Opção ")
                    if op == "D" or op == "d":
                        if C1.Saldo == 0:
                            print("Saldo insuficiente faça um Credito")
                        else:
                            C1.Debito(float(input("Valor para debitar: ")))
                            bonitin = (C1.Saldo,C1.Numero)
                            cursor.execute("update Corrente set saldo = %s where numero = %s",bonitin)
                            connection.commit()
                    elif op == "C" or op == "c":
                        C1.Credito(float(input("Valor para Credito: ")))
                        bonitin = (C1.Saldo,C1.Numero)
                        cursor.execute("update Corrente set saldo = %s where numero = %s",bonitin)
                        connection.commit()
                    elif op == "S" or op == "s":
                        opp = input("Vc quer uns cheques, meu mano?")
                        if opp == "S" or opp == "s":
                            C1.Talao(int(input(f"Quantos cheques você quer? (Você tem {C1.NTalao}): ")))
                            print("Obrigado!\nSaldo atual :", C1.Saldo)
                            bonitin = (C1.NTalao,C1.Numero)
                            cursor.execute("update Corrente set taloes = %s where numero = %s",bonitin)
                            connection.commit()
                            correte = True
                            dont = False
                        if opp == "N" or opp == "n":
                            print("Obrigado!\nSaldo atual :", C1.Saldo)
                            correte = True
                            dont = False

                if correte == False:
                    opp = input("Vc quer uns cheques, meu mano?")
                    if opp == "S" or opp == "s":
                        C1.Talao(int(input("Quantos cheques você quer? (Até 3): ")))
                        print("Obrigado!\nSaldo atual :", C1.Saldo)
                        bonitin = (C1.NTalao,C1.Numero)
                        cursor.execute("update Corrente set taloes = %s where numero = %s",bonitin)
                        connection.commit()
                        correte = True
                        dont = False
                    if opp == "N" or opp == "n":
                        print("Obrigado!\nSaldo atual :", C1.Saldo)
                        dont = False
            else:
                opof = input("Parece que você não tem uma conta! Quer criar uma ou logar?(C/L)")
                if opof == "C" or opof == "c":
                    num = random.randint(0,999999)
                    cred = input("Qual seu cpf?: ")
                    if len(cred) == 11:
                        data = (num,cred)
                        cursor.execute("insert into Corrente (numero, cpf) values(%s,%s)", data)
                        connection.commit()
                        C1 = Corrente(num,cred,0,True,3)
                        print("Conta criada!")
                        print(f"Numero da sua conta: {num}")
                    else:
                        print("Tentou ser engraçadinho?")
                if opof == "L" or opof == "l":
                    opnum = input("Qual o numero da sua conta?: ")
                    cursor.execute("select * from Corrente where numero = %s limit 1",opnum)
                    data = cursor.fetchall()
                    if len(data) > 0:
                        print("Achei sua conta!")
                        C1 = Corrente(data[0][1],data[0][2],data[0][3],True,data[0][4])
                    else:
                        print("Não achei")

    except:
        print("Vai se ferra meu, acha que eu sou quem???")

def Speacialing():
    global E1
    try:
        while True:
            if E1.Numero != None:
                for i in range(10):
                    print("Saldo atual: ", E1.Saldo,"\nLimite: ", E1.Limite)
                    print("Movimento : D - Debito, C - Credito")
                    op = input("Opção ")
                    if op == "D" or op == "d":
                        E1.Debito(float(input("Valor para debitar: "))) 
                        bonitin = (E1.Saldo,E1.Limite,E1.Numero)
                        cursor.execute("update Especial set saldo = %s, bonus = %s where numero = %s",bonitin)
                        connection.commit()
                    elif op == "C" or op == "c":
                        E1.Credito(float(input("Valor para Credito: "))) 
                        bonitin = (E1.Saldo,E1.Numero)
                        cursor.execute("update Especial set saldo = %s where numero = %s",bonitin)
                        connection.commit()
            else:
                opof = input("Parece que você não tem uma conta! Quer criar uma ou logar?(C/L)")
                if opof == "C" or opof == "c":
                    num = random.randint(0,999999)
                    cred = input("Qual seu cpf?: ")
                    if len(cred) == 11:
                        data = (num,cred)
                        cursor.execute("insert into Especial (numero, cpf) values(%s,%s)", data)
                        connection.commit()
                        E1 = Especial(1000,num,cred,0,True)
                        print("Conta criada!")
                        print(f"Numero da sua conta: {num}")
                    else:
                        print("Tentou ser engraçadinho?")
                if opof == "L" or opof == "l":
                    opnum = input("Qual o numero da sua conta?: ")
                    cursor.execute("select * from Especial where numero = %s limit 1",opnum)
                    data = cursor.fetchall()
                    if len(data) > 0:
                        print("Achei sua conta!")
                        E1 = Especial(data[0][4],data[0][1],data[0][2],data[0][3],True)
                    else:
                        print("Não achei")
    except:
        print("Vai se ferra meu, acha que eu sou quem???")

def Empresing():
    global EM1
    try:
        while True:
            if EM1.Numero != None:
                for i in range(10):
                    print("Saldo atual :", EM1.Saldo,"\nLimite: ", EM1.LimEmpresitmo)
                    print("Movimento : D - Debito, C - Credito, E - Emprestimo")
                    op = input("Opção ")
                    if op == "D" or op == "d":
                        if EM1.Saldo == 0:
                            print("Saldo insuficiente faça um Credito")
                        else:
                            EM1.Debito(float(input("Valor para debitar: ")))
                            bonitin = (EM1.Saldo,EM1.Numero)
                            cursor.execute("update Empresarial set saldo = %s where numero = %s",bonitin)
                            connection.commit()
                    elif op == "C" or op == "c":
                        EM1.Credito(float(input("Valor para Credito: ")))
                        bonitin = (EM1.Saldo,EM1.Numero)
                        cursor.execute("update Empresarial set saldo = %s where numero = %s",bonitin)
                        connection.commit()
                    elif op == "E" or op == "e":
                        EM1.Emprestimo(float(input("Valor do Emprestimo: ")))
                        bonitin = (EM1.Saldo,EM1.LimEmpresitmo,EM1.Numero)
                        cursor.execute("update Empresarial set saldo = %s, bonus = %s where numero = %s",bonitin)
                        connection.commit()

            else:
                opof = input("Parece que você não tem uma conta! Quer criar uma ou logar?(C/L)")
                if opof == "C" or opof == "c":
                    num = random.randint(0,999999)
                    cred = input("Qual seu cpf?: ")
                    if len(cred) == 11:
                        data = (num,cred)
                        cursor.execute("insert into Empresarial (numero, cpf) values(%s,%s)", data)
                        connection.commit()
                        EM1 = Empresa(num,cred,0,True,10000)    
                        print("Conta criada!")
                        print(f"Numero da sua conta: {num}")
                    else:
                        print("Tentou ser engraçadinho?")
                if opof == "L" or opof == "l":
                    opnum = input("Qual o numero da sua conta?: ")
                    cursor.execute("select * from Empresarial where numero = %s limit 1",opnum)
                    data = cursor.fetchall()
                    if len(data) > 0:
                        print("Achei sua conta!")
                        EM1 = Empresa(data[0][1],data[0][2],data[0][3],True,data[0][4])
                    else:
                        print("Não achei")
    except:
        print("Vai se ferra meu, acha que eu sou quem???")

def Estudaling():
    global ES1
    try:
        while True:
            if ES1.Numero != None:
                for i in range(10):
                    print("Saldo atual :", ES1.Saldo,"\nLimite: ", ES1.LimEmpresitmo)
                    print("Movimento : D - Debito, C - Credito, E - Emprestimo")
                    op = input("Opção ")
                    if op == "D" or op == "d":
                        if ES1.Saldo == 0:
                            print("Saldo insuficiente faça um Credito")
                        else:
                            ES1.Debito(float(input("Valor para debitar: ")))
                            bonitin = (ES1.Saldo,ES1.Numero)
                            cursor.execute("update Estudantil set saldo = %s where numero = %s",bonitin)
                            connection.commit()
                    elif op == "C" or op == "c":
                        ES1.Credito(float(input("Valor para Credito: ")))
                        bonitin = (ES1.Saldo,ES1.Numero)
                        cursor.execute("update Estudantil set saldo = %s where numero = %s",bonitin)
                        connection.commit()
                    elif op == "E" or op == "e":
                        ES1.Emprestimo(float(input("Valor do Emprestimo: ")))
                        bonitin = (ES1.Saldo,ES1.Limiteimite,ES1.Numero)
                        cursor.execute("update Estudantil set saldo = %s, bonus = %s where numero = %s",bonitin)
                        connection.commit()
            else:
                opof = input("Parece que você não tem uma conta! Quer criar uma ou logar?(C/L)")
                if opof == "C" or opof == "c":
                    num = random.randint(0,999999)
                    cred = input("Qual seu cpf?: ")
                    if len(cred) == 11:
                        data = (num,cred)
                        cursor.execute("insert into Estudantil (numero, cpf) values(%s,%s)", data)
                        connection.commit()
                        ES1 = Estudantil(num,cred,0,True,5000)    
                        print("Conta criada!")
                        print(f"Numero da sua conta: {num}")
                    else:
                        print("Tentou ser engraçadinho?")
                if opof == "L" or opof == "l":
                    opnum = input("Qual o numero da sua conta?: ")
                    cursor.execute("select * from Estudantil where numero = %s limit 1",opnum)
                    data = cursor.fetchall()
                    if len(data) > 0:
                        print("Achei sua conta!")
                        ES1 = Estudantil(data[0][1],data[0][2],data[0][3],True,data[0][4])
                    else:
                        print("Não achei")
    except:
        print("Vai se ferra meu, acha que eu sou quem???")


try:
    while True:
        print("Escolha uma opção:\n1 - Conta Poupança \n2 - Conta Corrente \n3 - Conta Especial \n4 - Conta Empresa\n5 - Conta Estundatil \n6 - Sair ")
        op = input("Opção ")
        if op == "1":
            Poupation()
        elif op == "2":
            Correnting()
        elif op == "3":
            Speacialing()
        elif op == "4":
            Empresing()
        elif op == "5":
            Estudaling()
        elif op == "6":
            connection.close()
            break
        else:
            print("Tente novamente")

except:
    print("error")