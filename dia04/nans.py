# %%
import pandas as pd
import numpy as np
# %%
data = {
    'Nome':['Teo','Nah','Lah','Mah','Jo'],
    'Idade':[31,32,34,12,np.nan],
    'Renda':[np.nan,3245,357,12432,np.nan]
}

df = pd.DataFrame(data)
df
# %%
# o método .isna() retorna um data frame com booleanos para cada elemento do
#   data frame original que seja nan
# considerando que um booleano pode ser interpretado como um valor 1 e 0, a
#   maneira mais rápida de retornar a quantidade de true é somando todos os
#   valores da coluna.
df['Idade'].isna().sum()
# %%
# indentificando o número de nan em cada coluna
df.isna().sum()
# %%
# identificando a taxa de nan em cada coluna
df.isna().mean()
# %%
# o método .fillna() substitui especificamente os elementos nan
df.fillna({
            'Idade' : df['Idade'].mean(),
            'Renda' : df['Renda'].mean()
           })
# %%
# o método .dropna() remove a linha com nan. se o parâmetro how='all' removerá
#   apenas se todos os elementos forem nan. se how='any' removera a linha se
#   qualquer elemento for nan
# para que o .dropna() considere apenas colunas específicas usa-se o parâmetro
#   .sebset=[] com uma lista do nome de cada coluna a ser considerada
df.dropna(subset=['Idade','Renda'], how='all')
# %%
# o axis=1 força o .dropna() a deixar de avaliar linhas e passar a avaliar
#   culunas inclusive excluindo-as. por padrão axis=0 o .dropna() avalia linhas
# thresh=... requer uma quantidade mínima de valores não-nan para que a coluna
#   seja retornada
df.dropna(axis=1, thresh=4)
# %%
