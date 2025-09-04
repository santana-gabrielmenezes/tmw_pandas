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
pd.read_sql_table('customers',engine)
# %%
