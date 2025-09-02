# %%
import pandas as pd
# %%
df = pd.read_csv('../data/customers.csv',sep=';')
df
# %%
# ao realizar uma operação matemática de uma lista com um escalar
#   a operação será iterada sobre todas as linhas da lista, uma-a-uma
df['Point_double'] = df['Points'] * 2
df
# %%
# ao realizar uma operação matemática entre duas listas de mesmo tamanho
#   a operação será realizada linha a linha
df['Points_ratio'] = df['Point_double'] / df['Points']
df
# %%
# ao criar uma coluna com uma constante, todas as linhas da coluna receberá
#   o mesmo valor, sendo este o valor da constante
df['Constante'] = 1
df
# %%
import numpy as np
# %%
# criando uma coluna com valores de log usando a biblioteca numpy
df['Points_log'] = np.log(df['Points','Point_double','Points_ratio'])
df
# %%
# criando uma coluna com os nomes da coluna nome em maiúsculo usando for apensar
#   de ser possível, não é recomendado usar recursão por questões de performace
nomes_alta = []
for i in df['Name'] :
    nomes_alta.append(i.upper())

df['Nome_Alta'] = nomes_alta
df
# %%
# o método mais adequado para esta operação é através de uma operação vetorial
# o metodo .str vai forçar os valores a serem reconhecidos como strings ao invés de objetos
df['Name'].str.upper()
# %%
# o .apply() vai aplicar uma função a todas as linhas da minha série
def get_first(nome:str) :
    return nome.split('_')[0]

df['Name'].apply(get_first)
# %%
# as funções lambda são funções anônimas obrigatoriamente simples que são usadas
#   uma única vez, em uma única linha
get_f = lambda nome: nome.split('_')[0]
get_f('Teo_Calvo')
# %%
# as funções lambda ajudão o código a ficar mais limpo, sem funções criadas para
#   serem usadas uma única vez
df['Name'].apply(lambda x : x.upper().split('_')[0])
# %%

def intervalo_pontos(pontos) :
    if pontos < 2500 :
        return 'baixo'
    elif pontos < 3500 :
        return 'médio'
    else :
        return 'alto'
    
df['Faixa_Pontos'] = df['Points'].apply(intervalo_pontos)
df['Faixa_Pontos']
# %%

df['UUID'].apply(lambda x : x[-3:])
# %%

data = {
    'nome' : ['Teo','Nah','Maria','Lara'],
    'recencia' : [1,30,10,45],
    'frequencia' : [2,5,1,15],
    'valor' : [100,2000,15,500]
}

df_crm = pd.DataFrame(data)
df_crm

def rfv(row) :


    nota=0

    if row['recencia'] <=10 :
        nota += 10
    elif 10 < row['recencia'] <= 30 :
        nota += 5
    elif row['recencia'] > 30 :
        nota += 0

    if row['frequencia'] > 10 :
        nota += 10
    elif 5 <= row['frequencia'] < 10 :
        nota += 5
    elif row['frequencia'] < 5 :
        nota += 0
    
    if row['valor'] > 1000 :
        nota += 10
    elif 100 <= row['valor'] < 1000 :
        nota += 5
    elif row['valor'] < 100 :
        nota +=0
    
    return nota

# %%

df_crm['rfv'] = df_crm.apply(rfv, axis=1)
df_crm
# %%
