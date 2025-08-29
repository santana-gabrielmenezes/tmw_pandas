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
# para combinação de condições lógicas, é necessário inserir cada uma entre parênteses
condicao = (df_costumers['Points'] >= 1000) & (df_costumers['Points'] <= 2000)
df_costumers[condicao]
# %%
# um mesmo objeto, neste caso uma lista, pode ter vários nomes atribuidos de modo que a alteração realizada usando um nome, reflete igualmente em todos
a = [1,2,3,4]
b = a
print(a)
print(b)

b.append(5)
print(a)
print(b)
# %%
# para criar um novo objeto com os mesmos valores, uma das opções é usar o .copy()
b = a.copy()
# %%
# caso seja necessário manipular uma base de dados filtrada, é importante realizar uma cópia, a fim de evitar auterar indevidamente a base de dados original
condicao = (df_costumers['Points'] >= 1000) & (df_costumers['Points'] <= 2000)
df_1000_2000 = df_costumers[condicao].copy()

df_1000_2000['Points'] = df_1000_2000['Points'] + 1000
df_1000_2000
# %%
# o quando inserido diretamente o nome da coluna entre colchetes o retorno do data frame é uma lista
df_costumers['UUID']
# %%
# porem, quando inserido uma lista com o nome das colunas o retorno é um data frame com apenas as colunas indicadas
df_costumers[['UUID']]
# %%
# para retornar mais de uma caluna, é necessário usar inserir uma lista com o nome das colunas
df_costumers[['UUID','Name']]
# %%
# ordenando o nome das colunas em ordem alfabética
colunas = df_costumers.columns.tolist()
colunas.sort()

df_costumers = df_costumers[colunas]
df_costumers
# %%
# para renomear o nome das colunas (obs.: o .rename() cria um novo data frame com os novos nomes por isso, para alterar o data frame original, é neccessário reatribuir a ele mesmo como no exemplo acima)
df_costumers = df_costumers.rename(columns= {'Name':'Nome', 'Points': 'Pontos'})
df_costumers
# %%
# também é possível renomear usando o parâmetro inplace = true que renomea o data frame original (não necessitando reatribuir)
df_costumers.rename(columns= {'UUID': 'ID'}, inplace=True)
df_costumers
# %%
