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
# %%
# para remover as duplicatas basta usar o método drop_duplicates()
# por padrão o .drop_duplicates() removerá apenas as linhas que forem completamente iguais em todas as colunas
# para que considere apenas colúnas específicas, é necessário usar o parâmetro subset=[...]
df.drop_duplicates(subset=['Nome','Idade'])
# %%
