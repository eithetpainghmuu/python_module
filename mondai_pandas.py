import pandas as pd

df = pd.read_csv("./titanic.csv")

#①
# print(df[["Age","Gender","Pclass","Fare","Survived"]])
# print(df)
#②
# print(df.dropna(how="any"))
# ③
print(df["Fare"].max())
print(df["Fare"].min())
# #④
# age_counts = df[df['Age']<=30].count()
# print(age_counts)
# print(len(df[df["Age"]] <= 30))
# #⑤
# result = df.sort_values("Pclass",ascending=True)
# print(result)
#⑥
# result1 = df[df["Survived"]==1].groupby("Gender").size()
# result2 = df[df["Survived"]==1].groupby("Gender")["Survived"].count()
# print(result1)
# print(result2)
#⑦
#print(df.groupby("Gender")['Age'].mean())


