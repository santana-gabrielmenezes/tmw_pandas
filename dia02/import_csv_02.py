# %%
import pandas as pd
# %%
# o parâmetro header=None vai indicar ao .read_csv() que o data frame não tem cabeçalho. sendo assim a linha de cabeçalho será preenchida com números segundo a posição da coluna iniciando em 0
# o parâmetro names=[...] é usado para substituir os nomes dos cabeçalhos das colunas por valores personalizados
df = pd.read_csv('../data/products.csv',
                 sep= ';',
                 #header= None,
                 names=['Id', 'Name','Description']
                )
df
# %%
df = df.rename(columns={'Name': 'Nome', 'Description': 'Descricao'})
df
# %%
