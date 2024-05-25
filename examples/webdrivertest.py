from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
# import openai

# api = 'pOZ3SxAl6Y03BvtYYMgUGtVYAbGsy9kF'


#######API DO EDITACODIGO##########################################
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

api = requests.get("https://editacodigo.com.br/index/api-whatsapp/pOZ3SxAl6Y03BvtYYMgUGtVYAbGsy9kF" ,  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
position = 0
pizza = None

##########################################


dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap")
driver = webdriver.Chrome(options=chrome_options2)

driver.get('https://web.whatsapp.com/')


def bot():
    global pizza
    global position
    try:
        ######PEGAR A MENSAGEM E CLICAR NELA
        bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha =  webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()


        ##### LER A NOVA MSG _21Ahp
        todas_as_msg = driver.find_elements(By.CLASS_NAME,msg_cliente)
        todas_as_msg_texto = [e.text for e  in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print(msg)
        vector = ['Olá, bem vindo a PizzaTime!\nO que gostaria de fazer?\n1 - Comprar Pizza\n2 - Sair',
                  'Pizzas disponíveis:\n1 - Mussarela\n2 - Calabresa\n3 - Frango com Catupiry\n4 - Voltar',
                  'Qual o seu endereço?',
                  'Até mais, sempre peça pizza do pizzaTime, nós temos seu endereço!!! :smile:'
                  ]

        if msg[:1]=='O' and position == 0:
            resposta= vector[0]
            position = 1
        elif position == 1 and msg[:1]=='1':
            resposta = vector[position]
            position = 2
        elif position == 2 and msg[:1]=='1' or msg[:1]=='2' or msg[:1]=='3':
            resposta = vector[position]
            if msg[:1] == '1':
                pizza = 'Mussarela'
            if msg[:1] == '2':
                pizza = 'Calabresa'
            if msg[:1] == '3':
                pizza = 'Frango com Catupiry'
            position = 3
        elif position == 2:
            position = 0
            resposta = vector[position]
        elif position == 3:
            end = len(msg) - 7
            man = msg[0:end]
            resposta = f"Iremos enviar uma pizza de {pizza} para {man}"
            position = 0
        elif position == 1 and msg[:1]=='2':
            resposta = vector[3]
            position = 0
        
        else:
            resposta = 'vc digitou algo'

      
        
        #RESPONDE A MSG
        campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
        campo_de_texto.click()
        campo_de_texto.send_keys(resposta,Keys.ENTER)

        #FECHA O CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        

    except:
        pass

while True:

    bot() 
