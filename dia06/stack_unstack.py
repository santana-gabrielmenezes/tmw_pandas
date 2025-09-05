# %%
import pandas as pd
# %%
df = pd.read_csv('../data/df_consolidado.csv',sep=';')
df
# %%
# o .stack() realiza o empilhamento de várias colunas em uma única, criando uma colunas
#   nova para indicar uma flag que determine a que categoria aquele dado se refere
#   é usado quado a tabela tem vários valores de mesma natureza categorizados em colunas diferentes
# o .set_index() vai definir quais colunas permanecerão
# o .stack vai criar uma série com os índices indicados no .set_index()
# e o reset_index() vai resetar as colunas indicadas no set_index() novamente como colunas
#   estruturando tudo como um data frame novamente
df = df.set_index(['cod','nome','período'])
df.stack().reset_index()
# %%
