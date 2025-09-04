# %%
# o codigo abaixo concatena todas as tabelas .csv da pasta ../data/ipea/
import pandas as pd
import os
# %%
def import_etl(path_arquivo:str) :

    name = (path_arquivo.split('/')[-1]
                .split('.')[0])

    df = (pd.read_csv('../data/ipea/homicidios.csv', sep=';')
            .rename(columns={'valor': name})
            .set_index(['cod','nome','período']))
    return df
# %%
path_pasta = '../data/ipea'
files = os.listdir(path_pasta)
# %%
dfs = []
for i in files :
    dfs.append(import_etl(path_pasta+i))
# %%
df_completo = (pd.concat(dfs, axis=1)
                .reset_index())
df_completo
# %%
df_completo.to_csv('../data/df_consolidado.csv', sep=';', index=False)