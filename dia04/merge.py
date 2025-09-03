# %%
import pandas as pd
# %%
data_users = {
    'id' : [1,2,3,4],
    'nome' : ['Teo','Mat','Nah','Mah'],
    'idade' : [31,31,32,32]
}

df_user = pd.DataFrame(data_users)
df_user
# %%
data_transacoes = {
    'id_user' : [1,1,1,2,3,3],
    'vl' : [432,532,123,6,4,87],
    'qtProdutos' : [2,1,3,6,10,2]
}
df_transacao = pd.DataFrame(data_transacoes)
df_transacao
# %%
# o .merge() une data frames análogo ao LEFT JOIN do SQL.
# o how='left' mantem o data frame à esquerda buscando as informações
#   do data frame inserido nos parâmetros
# o left_on= e o rght_on= identificam as colunas chave valor
# caso as colunas chave sejam identificadas pelo mesmo nome nos dois
#   data frames, é possível usar on='nome da coluna'

# equivalente no SQL:

# SELECT *
# FROM df_transacao
# LEFT JOIN df_user
# ON df_transacao.id_user = df_user.ID

df_transacao.merge(df_user,
                   how='left',
                   left_on='id_user',
                   right_on='id'
                   )
# %%
