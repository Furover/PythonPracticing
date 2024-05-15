import pandas as pd

import os

os.system("clear")
vendas_df = pd.read_excel("resources/Vendas.xlsx")
 
#feminicidio_df = pd.read_csv("resources/Feminicidio.csv")
pd.set_option('display.max_columns',None)

faturamento = vendas_df[['Valor Final', 'ID Loja']].groupby('ID Loja').sum()
quantidade = vendas_df[['Quantidade', 'ID Loja']].groupby('ID Loja').sum()
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
print(ticket_medio)