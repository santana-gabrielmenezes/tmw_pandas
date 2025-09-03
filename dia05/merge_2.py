# %%
import pandas as pd
# %%
df_customer = pd.read_csv('../data/customers.csv', sep=';')
df_customer
# %%
df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions
# %%
df_transactions_product = pd.read_parquet('../data/transactions_cart.parquet')
df_transactions_product
# %%
# o sufixes=[] insere sufixos nas colunas de data frames diferente que tenham o mesmo nome
#   afim de facilitar a identificação da origem da coluna no data frame resultante
df_join = df_transactions.merge(df_customer,
                                how='left',
                                left_on='IdCustomer',
                                right_on='UUID',
                                suffixes=['_transacao','_cliente']
                                )
df_join
# %%
df_join.merge(df_transactions_product,
              how='inner',
              left_on='UUID_transacao',
              right_on='IdTransaction'
              )
# %%
# também é possível encadear merges
df_join = (df_transactions.merge(df_customer,
                                how='left',
                                left_on='IdCustomer',
                                right_on='UUID',
                                suffixes=['_transacao','_cliente']
                                )
                          .merge(df_transactions_product,
                                 how='inner',
                                 left_on='UUID_transacao',
                                 right_on='IdTransaction'
                                 ))

df_join
# %%
