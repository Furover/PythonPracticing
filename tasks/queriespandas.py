import pandas as pd

feminicidio_df = pd.read_csv('PythonPracticing/resources/Feminicidio.csv')

#Ocorrências em cada município
municipio_df = feminicidio_df[['MUNICIPIO_CIRCUNSCRICAO', 'VITIMAS']].groupby('MUNICIPIO_CIRCUNSCRICAO').sum()

#Ocorrências por cor de pele
cor_pele_df = feminicidio_df[['COR_PELE', 'VITIMAS']].groupby('COR_PELE').sum()

#Local das ocorrências
local_df = feminicidio_df[['DESC_TIPOLOCAL', 'VITIMAS']].groupby('DESC_TIPOLOCAL').sum()

#Ocorrências por profissão
proffisao_df = feminicidio_df[['PROFISSAO', 'VITIMAS']].groupby('PROFISSAO').sum()

#Ocorrências por mês
mes_df = feminicidio_df[['MES_ESTATISTICA', 'VITIMAS']].groupby('MES_ESTATISTICA').sum()

print(municipio_df)
