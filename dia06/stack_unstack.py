# %%
import pandas as pd
# %%
df = pd.read_csv('../data/df_consolidado.csv',sep=';')
df
# %%
# o .stack() realiza o empilhamento de várias colunas em uma única, criando uma colunas
#   nova para indicar uma flag que determine a que categoria aquele dado se refere
#   é usado quado a tabela tem vários valores de mesma natureza categorizados em colunas diferentes
# o .set_index() vai definir quais colunas permanecerão fixas
# o .stack vai criar uma série com os índices indicados no .set_index()
# e o reset_index() vai resetar as colunas indicadas no set_index() novamente como colunas
#   estruturando tudo como um data frame novamente
df = df.set_index(['cod','nome','período'])
df_stack = (df.stack()
             .reset_index()
             .rename(columns={'level_3': 'tipo',
                              0:'qtnd'})
            )
df_stack
# %%
# o .ustack() realiza a "colunização" mantendo todas as colunas do data frame fixas exeto pela
#   coluna informada como parâmetro. esta coluna pode ser informada pelo nome no formato strig
#   ou pelo índice começando em 0 até n-1
df_unstack = (df_stack.set_index(['cod','nome','período','tipo'])
                      .unstack('tipo')
                      .reset_index()
              )
df_unstack
# %%
# 
homicidios = df_unstack['qtnd'].columns.tolist()
identificadores = df_unstack.columns.droplevel(1).tolist()[:3]

df_unstack.columns = identificadores + homicidios
df_unstack
# %%
