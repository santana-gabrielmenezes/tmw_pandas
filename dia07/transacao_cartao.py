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

def add_months(row) :
    new_date =  row['dtTransaction'] + np.timedelta64(row['Months_add']*30, 'D')
    dt_str = '-'.join(str(new_date).split('-')[:-1]) +'-01'
    return dt_str

df_fatura['DtFatura'] = df_fatura.apply(add_months, axis=1)
df_fatura
# %%
df_fatura = df_fatura.groupby(['idCliente','DtFatura'])['ValorParcela'].sum()
df_fatura = df_fatura.reset_index()
# %%
fatura_mes = df_fatura.pivot_table(columns='DtFatura', index='idCliente',values='ValorParcela')
fatura_mes = fatura_mes.fillna(0)
fatura_mes
# %%
