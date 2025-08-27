# %%
import pandas as pd
# %%

data = {
    'nome' : ['teo','nah','lara','maria'],
    'sobrenome' : ['calvo','ataide','calvo','calvo'],
    'idade': [31,32,31,2]
}
# %%

data['idade'][0]
# %%
# criando um DataFrame
df = pd.DataFrame(data)
df
# %%
# acessando um elemento do DataFrame
df['idade'].iloc[0]
# %%
# um DataFrame funciona como um conjunto de series (cada coluna é uma serie)
type(df['idade'])
# %%

df['sobrenome'].iloc[0]
# %%
# também é possível acessar as séries do data frame pelas linhas (cada linha é uma serie)
df.iloc[0]
# %%

df.index
# %%

df.columns
# %%

df.info()
# %%

df.info(memory_usage='deep')
# %%

df.dtypes
# %%
df['peso'] = [80,53,65,14]
df.describe()
# %%

sumario = df.describe()
sumario['peso']['mean']
# %%

df.head(3)
# %%

df.tail(3)
# %%
