import pandas as pd
 
#series_data = [10,15,20,25]
#ser = pd.Series(series_data)
#print(ser)


dataframe_data = ([
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
print(df[["金額","クラス"]])
