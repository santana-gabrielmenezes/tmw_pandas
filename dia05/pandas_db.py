# %%
# a biblioteca sqlalchemy permite conectar o python com um banco de dados sql
import pandas as pd
import sqlalchemy
# %%
# o sqlalchemy.create_engine(...) conecta o banco de dados e permite o pandas acessar
#   as tabelas dentro deste
# as 3 barras em 'sqlite:///' indica ao sqlalchemy que será usado o protocolo para bancos de dados locais
engine = sqlalchemy.create_engine('sqlite:///../data/database.db')
# %%
# o pd.read_sql_table() busca a tabela, pelo nome fornecido no primeiro parâmetro,
#   no banco de informado no segundo parâmetro
# desta forma abaixo, o pandas solicitará a tabela inteira do banco de dados independente do tamanho
df_transactions_cart = pd.read_sql_table('customers',engine)
df_transactions_cart
# %%
# utilizando o pd.read_sql_query() é possível enviar querys ao banco de dados de maneira que a estrutura
#   da tabela será montada pelo banco de dado, não mais pelo pandas, retornando apenas a tabela final desejada
# aspas triplas ''' são usadas para escrever textos de múltiplas linhas
query = '''
SELECT *
FROM customers AS t1
LEFT JOIN transactions AS t2
ON t1.UUID = t2.IdCustomer
LIMIT 10 '''
df_customers = pd.read_sql_query(query, engine)
df_customers
# %%
# o .to_sql() cria tabelas e popula com as onformações do dataframe
data_01 = {
    'id' : [1,2,3,4],
    'nome' : ['Teo','Mat','Nah','Mah'],
    'idade' : [31,31,32,32]
}
df_01 = pd.DataFrame(data_01)

data_02 = {
    'id' : [5,6,7,8],
    'nome' : ['Jose','Nathan','Arnaldo','Mario'],
    'idade' : [23,33,19,21]
}
df_02 = pd.DataFrame(data_02)

df_01.to_sql("tb_df",engine,index=False)
# %%
df_02.to_sql("tb_df",engine,index=False, if_exists='append')
# %%
pd.read_sql('tb_df',engine)
# %%
df_01.to_sql("tb_df",engine,index=False, if_exists='replace')
# %%
