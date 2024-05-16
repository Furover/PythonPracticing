import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

feminicidio_df = pd.read_csv('resources/Feminicidio.csv')

#Ocorrências em cada município
municipio_df = feminicidio_df[['MUNICIPIO_CIRCUNSCRICAO', 'VITIMAS']].groupby('MUNICIPIO_CIRCUNSCRICAO').sum()

#Ocorrências por cor de pele
cor_pele_df = feminicidio_df.groupby('COR_PELE').size().reset_index('QTDE')

#Local das ocorrências
local_df = feminicidio_df[['DESC_TIPOLOCAL', 'VITIMAS']].groupby('DESC_TIPOLOCAL').sum()

#Ocorrências por profissão
profissao_df = feminicidio_df[['PROFISSAO', 'VITIMAS']].groupby('PROFISSAO').sum()

#Ocorrências por mês
mes_df = feminicidio_df[['MES_ESTATISTICA', 'VITIMAS']].groupby('MES_ESTATISTICA').sum()

print(municipio_df)
