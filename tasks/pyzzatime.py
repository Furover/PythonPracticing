import os
import time
op = ""
comprou = False

def Checkout(pizza,price):
    global comprou
    end = input("Qual o seu endereço?: ")
    print(f"Iremos enviar uma pizza de {pizza} para {end}")
    print(f"Valor total: {price}")
    while True:
        op = input("Confirmar ou voltar?(C/V): ").upper()
        if op == "C":
            print("Estamos preparando sua pizza!")
            comprou = True
            time.sleep(4)
            break
        elif op == "V":
            break


def Comprar():
    while True:
        os.system("clear")
        print("Pizzas disponíveis:\n1 - Mussarela\n2 - Calabresa\n3 - Frango com Catupiry\n4 - Voltar")
        op = input("Opção ")
        if op == "1":
            Checkout("Mussarela",60)
            break
        if op == "2":
            Checkout("Calabresa",80)
            break
        if op == "3":
            Checkout("Frango com catupiry",100)
            break
        if op =="4":
            break
        else:
            print("Digita correto bobo")
            time.sleep(2)

while True:
    os.system("clear")
    print("Olá, bem vindo a PizzaTime!\nO que gostaria de fazer?\n1 - Comprar Pizza\n2 - Sair")
    op = input("Opção ")

    if op == "1":
        Comprar()
    elif op == "2":
        if comprou:
            print("Até mais! Aproveite sua pizza quentinha!")
        else:
            print("Até mais! Divirta-se sem ter uma pizza quentinha gostosa e boa com queijo caindo derretido! Já que você não quer uma pizza e ME ODEIA, divirta-se vai, nem ligo.")
            time.sleep(2)
            os.system("clear")
            print("Seu ip: 192.168.15.30")
            print("Enderoço: Rua Vila dos bobões, Curitiba, Brasil")
            print("Nome real: Edevaldo")
            print("Quantidade de pizzas GOSTOSAS: 0")
            print("CPF: 684.175.124.33")
        time.sleep(2)
        break
    else:
        "Digita correto bobo"
        time.sleep(2)
