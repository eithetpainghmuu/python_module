import pandas as pd
df = pd.read_csv("./titanic.csv")

#series_data = [10,15,20,25]
#ser = pd.Series(series_data)
#print(ser)


"""dataframe_data = ([
    [100, "a", True],
    [200, "b", False],
    [150, "d", False],
    [550, "c", True]
])
df = pd.DataFrame(dataframe_data)
df.index=["a1","b1","c1","d1"]
df.columns=["金額","クラス","boolean"]

print(df)
print(df["金額"])
print(df[["金額","クラス"]])"""




"""print(df)
print(df[["Age"]])
print(df["Age"])
print(df[["Age","Name","PassengerId"]])

print(df[0:10])
print(df[:1])
print(df.head(3))
print(df.tail(3))
print(df.loc[[2,5]])
print(df.loc[2:5])
print(df.loc[:1,["Age","Name"]])
print(df.loc[[2,5],["Age","Name"]])

print(df.iloc[2:5,0:5])

print(df.loc[2,["Name"]])
print("###############################################")
print(df.at[2,"Name"])
print("###############################################")
print(df.iloc[1:3,1:3])
print(df.at[0,"Age"])
print(df["Age"]>=30)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(df["Age"]>=30)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
result = df[df["Age"].isin([20,30,40])]
print(result)"""

#print(df.sort_values("Age"))

#sorted_df = df.sort_values("PassengerId",ascending=False)
#print(sorted_df)

#print(df.dropna(how="any"))
#print(df.fillna(value = 0))

#print(df.isna())

##print(df.groupby(["Gender","Age"])[["Gender","Age"]].count())

#print(df["Gender"].value_counts())

#print(df.groupby(["Gender","Survived"])["Survived"].count())

#print(df.groupby(["Gender","Survived"])[["Gender","Age"]].mean())

#print(df[["Gender","Age"]].max())

"""for column in df:
    print(column)

for row in df:
    print(df)"""

#for index,row in df.iterrows():
    #print(index,row)
     
"""for index,row in df.iterrows():
    print(row["Age"])"""

#for index,row in df.iterrows():
    #print(row["Age"])

#for age,pclass in zip(df["Age"],df["Pclass"]):
    #print(age,pclass)