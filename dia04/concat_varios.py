# %%
import pandas as pd
# %%
df_01 = (pd.read_csv('../data/ipea/homicidios.csv', sep=';')
           .rename(columns={'valor':'homicidios'})
           .set_index(['cod','nome','período']))
df_01
# %%
df_02 = (pd.read_csv('../data/ipea/homicidios-por-armas-de-fogo.csv', sep=';')
           .rename(columns={'valor':'homicidios-por-armas-de-fogo'})
           .set_index(['cod','nome','período']))
df_02
# %%
pd.concat([df_01,df_02],axis=1).reset_index()
# %%
