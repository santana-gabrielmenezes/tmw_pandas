# %%
# importando pandas
import pandas as pd
# %%
# declarando uma lista de valores
idades = [30,42,90,34]
idades
# %%
# tranformação para séries pandas
series_idades = pd.Series(idades)
series_idades
# %%
# métodos das séries pandas
# média
series_idades.mean()
# %%
# variância
series_idades.var()
# %%
# mediana
series_idades.median()
# %%
# desvio padrão
series_idades.std()
# %%
# 1º quartil
series_idades.quantile(0.25)
# %%
# sumarização
series_idades.describe()
# %%
# deimensão da série
series_idades.shape
# %%
# navegando na lista
idades[0]
# %%
# navegando na série
series_idades[0]
# %%
# visualizando índices da série
series_idades.index
# %%
# personalizando índices da série
series_idades.index = ['t','e','o','c']
series_idades
# %%
# navegando na série pelo índice personalizado
series_idades['t']
# %%
# navegando na série pela posição (quando ídices não tiverem alterados ou quando a navegação não encontrar o índice personalizado)
# o pandas vai, primeiro, usar a navegação por índice, caso não encontre, usa a navegação por posição
series_idades[3]
# %%
# navegando na série, obrigatoriamente, pela posição
# usando o .iloc[] o pandas vai navegar obrigatoriamente pela posição (independente do índice)
series_idades.index = [40,30,50,10]
series_idades.iloc[0]
# %%
