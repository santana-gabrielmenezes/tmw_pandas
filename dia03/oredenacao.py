# %%
import pandas as pd
# %%
df = pd.read_csv('../data/customers.csv',sep=';')
df
# %%
# ordenando do menor para o maior
df.sort_values(by='Points')
# %%
# ordenando do maior para o menor
df.sort_values(by='Points', ascending=False)
# %%
# o .sort_values() não sobrescreve, mas cria um novo
df
# %%
# para sobrescrever o data frame original é nessessário reatribuir o novo data frame à variável
df = df.sort_values(by='Points', ascending=False)
df
# %%
# ou usar o parâmetro inplace=True
df.sort_values(by='Points', ascending=False, inplace=True)
df
# %%
# é possível encadear métodos desde que os parâmetros usados retornem data frames novos,
# o que não funciona om o inplace=True pois este altera o data frame original
df = (df.sort_values(by='Points',
                     ascending=False)
        .rename(columns={'Name':'Nome',
                         'Points':'Pontos'}))
df
# %%
# para que seja criada uma hierarquia de ordenação basta passar uma lista no parâmetro by= do .sort_values()
# ao invés de um valor espessífico
df.sort_values(by=['Pontos','Nome'], ascending=[False, True])
# %%
