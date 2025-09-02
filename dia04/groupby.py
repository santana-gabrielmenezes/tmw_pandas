# %%
import pandas as pd
# %%
# agreagações são formas de resumir um conjunto de dados por meio de alguma estatística
#   como média, mediana, desvio padrão e etc.
df = pd.read_excel('../data/transactions.xlsx')
df
# %%
# somando todos os pontos de um usuário
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condicao]
df_user['Points'].sum()
# %%
# somando os pontos acumulados de cada usuário usando for
pontos = {}

for i in df['IdCustomer'].unique() :
    condicao = df['IdCustomer'] == i
    pontos[i] = df[condicao]['Points'].sum()

pontos
# %%
# somando os pontos acumulados de cada usuário usando groupby
# o .reset_index() insere uma coluna com o índice das linhas iniciando em 0
df_summary = df.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()
# %%
# o .agg(...) permite realizar o agrupamento como no exemplo acima, porem em mais de
#   uma coluna e com diferentes cálculos de agregação
(df.groupby(['IdCustomer'])
   .agg({
       'Points' : 'sum',
       'UUID' : 'count',
       'DtTransaction' : 'max'
       })
   .reset_index()
   .rename(columns={
                    'Points' : 'Valor',
                    'UUID' : 'Frequência',
                    'DtTransaction' : 'UltimaData'
           })
)
# %%
import datetime

data1 = df['DtTransaction'][0]
now = datetime.datetime.now()

(now - data1).days
# %%
# acrescentando uma coluna com a recencia da última operação

def recencia(x) :
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(['IdCustomer'])
   .agg({
       'Points' : 'sum',
       'UUID' : 'count',
       'DtTransaction' : ['max', recencia]
       })
   .reset_index()
   .rename(columns={
                    'Points' : 'Valor',
                    'UUID' : 'Frequência',
                    'DtTransaction' : 'UltimaData'
           })
)
# %%
