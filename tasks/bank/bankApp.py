from accounts import *

P1 = Poupanca(14,12123,231231,10,False)
C1 = Corrente(10,123123,123123,False,3)
E1 = Especial(1000,0,0,0,False)
EM1 = Empresa(123123,123123,123,False,10000)
ES1 = Estudantil(123132,123123,123132,False,5000)

def Poupation():
    try:
        P1.Ativar()
        for i in range(10):
            print("Saldo atual :", P1.Saldo)
            print("Movimento : D - Debito, C - Credito")
            op = input("Opção ")
            if op == "D" or op == "d":
                if P1.Saldo == 0:
                    print("Saldo insuficiente faça um Credito")
                else:
                    P1.Debito(float(input("Valor para debitar: ")))
            elif op == "C" or op == "c":
                P1.Credito(float(input("Valor para Credito: ")))
    except:
        print("Vai se ferra meu, acha que eu sou quem???")

    print("Saldo atual :", P1.Saldo)
    try:
        P1.Correcao(int(input("Qual o dia de hj?: ")))
        print("Saldo atual :", P1.Saldo)
    except:
        print("AH meu vai se ferra meu")

def Correnting():
    correte = False
    try:
        C1.Ativar()
        for i in range(10):
            print("Saldo atual :", C1.Saldo)
            print("Movimento : D - Debito, C - Credito, S - Sair")
            op = input("Opção ")
            if op == "D" or op == "d":
                if C1.Saldo == 0:
                    print("Saldo insuficiente faça um Credito")
                else:
                    C1.Debito(float(input("Valor para debitar: ")))
            elif op == "C" or op == "c":
                C1.Credito(float(input("Valor para Credito: ")))
            elif op == "S" or op == "s":
                opp = input("Vc quer uns cheques, meu mano?")
                if opp == "S" or opp == "s":
                    C1.Talao(int(input("Quantos cheques você quer? (Até 3): ")))
                    print("Obrigado!\nSaldo atual :", C1.Saldo)
                    correte = True
                    break
                if opp == "N" or opp == "n":
                    print("Obrigado!\nSaldo atual :", C1.Saldo)
                    correte = True
                    break

        if correte == False:
            opp = input("Vc quer uns cheques, meu mano?")
            if opp == "S" or opp == "s":
                C1.Talao(int(input("Quantos cheques você quer? (Até 3): ")))
                print("Obrigado!\nSaldo atual :", C1.Saldo)
                correte = True
            if opp == "N" or opp == "n":
                print("Obrigado!\nSaldo atual :", C1.Saldo)


    except:
        print("Vai se ferra meu, acha que eu sou quem???")

def Speacialing():
    try:
        E1.Ativar()
        for i in range(10):
            print("Saldo atual: ", E1.Saldo,"\nLimite: ", E1.Limite)
            print("Movimento : D - Debito, C - Credito")
            op = input("Opção ")
            if op == "D" or op == "d":
                E1.Debito(float(input("Valor para debitar: ")))
            elif op == "C" or op == "c":
                E1.Credito(float(input("Valor para Credito: ")))    
    except:
        print("Vai se ferra meu, acha que eu sou quem???")

def Empresing():
    try:
        EM1.Ativar()
        for i in range(10):
            print("Saldo atual :", EM1.Saldo,"\nLimite: ", EM1.LimEmpresitmo)
            print("Movimento : D - Debito, C - Credito, E - Emprestimo")
            op = input("Opção ")
            if op == "D" or op == "d":
                if EM1.Saldo == 0:
                    print("Saldo insuficiente faça um Credito")
                else:
                    EM1.Debito(float(input("Valor para debitar: ")))
            elif op == "C" or op == "c":
                EM1.Credito(float(input("Valor para Credito: ")))
            elif op == "E" or op == "e":
                EM1.Emprestimo(float(input("Valor do Emprestimo: ")))
    except:
        print("Vai se ferra meu, acha que eu sou quem???")

def Estudaling():
    try:
        ES1.Ativar()
        for i in range(10):
            print("Saldo atual :", ES1.Saldo,"\nLimite: ", ES1.LimEmpresitmo)
            print("Movimento : D - Debito, C - Credito, E - Emprestimo")
            op = input("Opção ")
            if op == "D" or op == "d":
                if ES1.Saldo == 0:
                    print("Saldo insuficiente faça um Credito")
                else:
                    ES1.Debito(float(input("Valor para debitar: ")))
            elif op == "C" or op == "c":
                ES1.Credito(float(input("Valor para Credito: ")))
            elif op == "E" or op == "e":
                ES1.Emprestimo(float(input("Valor do Emprestimo: ")))
    except:
        print("Vai se ferra meu, acha que eu sou quem???")


try:
    while True:
        print("Escolha uma opção:\n1 - Conta Poupança \n2 - Conta Corrente \n3 - Conta Especial \n4 - Conta Empresa\n5 - Conta Estundatil \n6 - Sair ")
        op = input("Opção ")
        if op == "1":
            Poupation()
            break
        elif op == "2":
            Correnting()
            break
        elif op == "3":
            Speacialing()
            break
        elif op == "4":
            Empresing()
            break
        elif op == "5":
            Estudaling()
            break
        elif op == "6":
            break
        else:
            print("Tente novamente")

except:
    print("error")