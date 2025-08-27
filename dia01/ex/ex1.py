# %%
import pandas as pd
# %%
dados = [10,20,45,9,12,35,24,10,8,14,21]
# %%
series_dados = pd.Series(dados)
series_dados
# %%
series_dados.describe()
# %%
dados_mean = series_dados.mean()
dados_mean
# %%
dados_std = series_dados.std()
dados_std
# %%
dados_max = series_dados.max()
dados_max
# %%
