import pandas as pd

df1 = pd.read_csv('C:/Users/Willian/Desktop/Radartona/Radartona_ML/bases_tratadas/clima_tratado.csv', sep=";").drop_duplicates()
df2 = pd.read_csv("C:/Users/Willian/Desktop/Radartona/Radartona_ML/bases_tratadas/velocidades.csv", sep=";").drop_duplicates()
# df2_key = df2.Colname2

# creating a empty bucket to save result
df_result = pd.DataFrame(columns=(df1.columns.append(df2.columns)).unique())
df_result.to_csv("C:/Users/Willian/Desktop/Radartona/Radartona_ML/bases_tratadas/df_ultimo.csv",index_label=False,sep=";")

# save data which only appear in df1 # sorry I was doing left join here. no need to run below two line.
# df_result = df1[df1.Colname1.isin(df2.Colname2)!=True]
# df_result.to_csv("df3.csv",index_label=False, mode="a")

# deleting df2 to save memory
del(df2)

def preprocess(x):
    x = x.merge(df1, left_on = ['ano','mes','dia'], right_on = ['ano','mes','dia'], how="left")
    x.to_csv("C:/Users/Willian/Desktop/Radartona/Radartona_ML/bases_tratadas/df_ultimo.csv",mode="a",header=False,index=False,sep=";")

reader = pd.read_csv('C:/Users/Willian/Desktop/Radartona/Radartona_ML/bases_tratadas/velocidades.csv', sep=";", chunksize=100000) # chunksize depends with you colsize

[preprocess(r) for r in reader]