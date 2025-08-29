# %%
# um arquivo .parquet é um arquivo binário otimizado para leitura e armazenamento permitindo uma leitura mais rápida do banco de dados e um menor espaço de armazenamento comparado a um aquivo de texto comum
import pandas as pd
# %%
df = pd.read_parquet('../data/transactions_cart.parquet')
df
# %%
