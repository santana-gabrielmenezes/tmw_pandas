# %%
import pandas as pd

df = pd.read_csv('../data/customers.csv',sep=';')
df
# %%
df.dtypes
# %%
# o método .astype(...) tentará converter os valores no tipo definido
df['Points'].astype(str)
# %%
