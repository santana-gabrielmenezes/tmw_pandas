# %%
import pandas as pd
# %%
df = pd.read_excel('../data/transactions.xlsx')
# %%
# as vezes é necessário instalar uma dependência do pandas que permite acessar arquivos de Excel. para isso utilize o comando !pip install openpyxl
df
# %%
df.shape
# %%
df.head()
# %%
df.tail()
# %%
colunas = ['UUID',
           'Points',
           'IdCustomer',
           'DtTransaction']

df = df[colunas]

df
# %%
df.info(memory_usage='deep')
# %%
