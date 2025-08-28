# %%
import pandas as pd
# %%
# criando um dicionário
data = {
    'nome' : ['teo','nah','lara','maria'],
    'sobrenome' : ['calvo','ataide','calvo','calvo'],
    'idade': [31,32,31,2]
}
# %%
# acessando um valor no dicionário
data['idade'][0]
# %%
# criando um DataFrame
df = pd.DataFrame(data)
df
# %%
# acessando um valor do data frame
df['idade'].iloc[0]
# %%
# um data frame funciona como um conjunto de series (cada coluna é uma serie)
type(df['idade'])
# %%
# acessando um valor do data frame através do nome da coluna e da posição (linha)
df['sobrenome'].iloc[0]
# %%
# também é possível acessar as séries do data frame pelas linhas (cada linha é uma serie)
df.iloc[0]
# %%
# acessando atributo: retornando os ídices do data frame
df.index
# %%
# acessando atributo: retornando o nome das colunas do data frame
df.columns
# %%
# retornando informações sobre o data frame
df.info()
# %%
# retornando informações sobre o data frame (com verdadeiro espaço de armazenamento utilizado)
df.info(memory_usage='deep')
# %%
# retornando apenas os tipos de cada coluna
df.dtypes
# %%

df['peso'] = [80,53,65,14]
df.describe()
# %%
# calculando pricipais estatísticas descritivas das colunas
sumario = df.describe()
sumario['peso']['mean']
# %%
# retornando as primeiras linhas do data frame
df.head(3)
# %%
# retornando as últimas linhas do data frame
df.tail(3)
# %%
