# %%
import pandas as pd
# %%
data = {
    'Nome':['Teo','Nah','Maria','Nah','Lara','Teo'],
    'Idade':[32,33,2,33,31,32],
    'updated_at':[1,2,3,1,2,3]
}
df = pd.DataFrame(data)
# %%
# para remover as duplicatas basta usar o método drop_duplicates()
# por padrão o .drop_duplicates() removerá apenas as linhas que forem completamente iguais em todas as colunas
#   para que considere apenas colúnas específicas, é necessário usar o parâmetro subset=[...]
# por definição o .drop_duplicates() mantem a primeira linha duplicada e remove as demais,
#   para mudar esta priorização usa-se o parâmetro keep=[...]
# visto que o mais comum é manter o registro mais recente e descartar os mais antigo,
#   é comum usar o .sort_values() antes do drop_duplicates() para ordenar com o registro mais recente acima e
#   só então eliminara as duplicatas com drop_duplicates()
df = (df.sort_values(by='updated_at', ascending=False)
       .drop_duplicates(subset=['Nome','Idade'],keep='first'))
df
# %%
