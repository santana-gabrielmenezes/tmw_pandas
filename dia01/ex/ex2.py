# %%
import pandas as pd
# %%
dados = {'nome': ['Teo','Nah','Napoleão'], 'idade': [31,32,14]}
dados
# %%
df_dados = pd.DataFrame(dados)
df_dados
# %%
df_dados_nome = df_dados['nome']
df_dados_nome
# %%
df_dados_idade = df_dados['idade']
df_dados_idade
# %%
df_dados_idade.mean()
# %%
df_dados_nome.iloc[-1]
# %%