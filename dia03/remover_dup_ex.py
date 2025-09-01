# %%
import pandas as pd
# %%
df = pd.read_excel('../data/transactions.xlsx')
df
# %%
df_last = (df.sort_values(by='DtTransaction',ascending=False)
        .drop_duplicates(subset='IdCustomer',keep='first'))
df_last
# %%
# o método .nunique() retorna o número de elementos únicos de uma lista e pode ser usado para avaliar
#   se as duplicatas foram removidas. quando o .nunique() retornar um valor igual ao número de linhas
df_last['IdCustomer'].nunique()
# %%
