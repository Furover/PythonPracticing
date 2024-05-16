import pandas as pd
import matplotlib.pyplot as plt

cities = ['Santo André', 'São Bernardo do Campo', 'São Caetano do Sul', 'Diadema', 'Mauá','Ribeirão Pires', 'Rio Grande da Serra']

pd.set_option('display.max_columns', None)

feminicidio_df = pd.read_csv('resources/Feminicidio.csv')

#Cor_Pele em osasco
cidade_df = feminicidio_df[feminicidio_df['MUNICIPIO_CIRCUNSCRICAO'] == 'Osasco']

osasco_df = cidade_df.groupby('COR_PELE').size().reset_index(name='QUANTIDADE')

osasco_df = osasco_df.sort_values(by='COR_PELE',ascending=False)

#Todos casos cidades de uma lista

cities_df = feminicidio_df[feminicidio_df['MUNICIPIO_CIRCUNSCRICAO'].isin(cities)]

precision_df = cities_df[['MUNICIPIO_CIRCUNSCRICAO','VITIMAS']].groupby('MUNICIPIO_CIRCUNSCRICAO').sum().sort_values(by='VITIMAS',ascending=False).reset_index(names='CIDADES')

#precision_df = cities_df.groupby('MUNICIPIO_CIRCUNSCRICAO').size().reset_index(name='QUANTIDADE').sort_values(by='QUANTIDADE',ascending=False)

#print(precision_df)

plt.figure(figsize=(8,8))
plt.pie(precision_df['VITIMAS'],labels=precision_df['CIDADES'],autopct='%1.1f%%',startangle=140)
plt.title('Vitimas por município')
plt.axis('equal')
plt.show()
