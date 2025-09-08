# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_excel('../data/transacao_cartao.xlsx')
df
# %%
df['dtTransaction'] = pd.to_datetime(df['dtTransaction'], format='%d/%m/%y')
# %%
df['ValorParcela'] = df['Valor'] / df['Parcelas']
df
# %%
df['ValorParcela'] = df.apply(lambda row : [row['Valor']/row['Parcelas'] for i in range(row['Parcelas'])],axis=1)
df
# %%
df.explode('ValorParcela')
# %%
df_fatura = df.explode('ValorParcela')
df_fatura = df_fatura.drop(['Valor','Parcelas'], axis=1)
df_fatura['Months_add'] = df_fatura.groupby('idTransaction')['dtTransaction'].rank('first').astype(int)
df_fatura.apply(add_months, axis=1)
df_fatura
# %%
def add_months(row) :
    new_date =  row['dtTransaction'] + np.timedelta64(row['Months_add'], 'M')
    return new_date
# %%
