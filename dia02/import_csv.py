# %%
# importando pandas
import pandas as pd
# %%
# usando pandas para ler um arquivo .csv
df_costumers = pd.read_csv('../data/customers.csv', sep=';')
df_costumers
# %%
# retornando o número de linhas e colunas
df_costumers.shape
# %%
# retornando informações com espaço real de armazenamento
df_costumers.info(memory_usage='deep')
# %%
# retornando as estatísticas descitivas apenas da coluna Points
df_costumers['Points'].describe()
# %%
# retornando o valor máximo da coluna Points
df_costumers['Points'].max()
# %%
# exemplo de como filtrar uma lista com python
notas = [4.5,6,7,3.5]
for i in notas :
    if i > 5 :
        print(i)
# %%
# exemplo de como realizar uma operação iterando sobre todos os valores de uma lista
notas_novas = []
for i in notas :
    notas_novas.append(i+1)
notas_novas
# %%
# com séries é possível realizar operações vetoriais onde a operação é realizada sobre todos os valores da serie, um a um
df_costumers['Points'] + 1000
# %%
# é possível, inclusive, realizar operações booleanas
df_costumers['Points'] > 1000
# %%
# realizando um filto com pandas (neste caso para obter a linha com o valor da coluna 'Points')
maximo = df_costumers['Points'].max()
condicao = df_costumers["Points"] == maximo
df_costumers[condicao]
# %%
# é comum encontrar o mesmo filtro usando a condição lógica inteira como parâmetro
df_costumers[df_costumers["Points"] == df_costumers['Points'].max()]
# %%
# é possível tratar o retorno de uma leitura de um .csv como um data frame
df_costumers[df_costumers["Points"] == df_costumers['Points'].max()]['Name']
# %%
# também é possível tratar uma coluna como uma série
df_costumers[df_costumers["Points"] == df_costumers['Points'].max()]['Name'].iloc[0]
# %%
# de forma mais organizada
condicao = df_costumers["Points"] == df_costumers['Points'].max()
df_maior = df_costumers[condicao]
df_maior['Name'].iloc[0]
# %%
