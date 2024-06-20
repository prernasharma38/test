import pandas as pd

# mydataset = {
#     'std' : ["rohan", "sohan", "mohan"],
#     'marks' : [34, 56,79]
# }

# myvar = pd.DataFrame(mydataset)
# print(myvar)

# a = [2,5,7]
# myarrya = pd.Series(a)
# print(myarrya[1]) 

# a = [3,4,6]
# myans = pd.Series(a, index=["x","y", "z"])
# print(myans)

# colories = {"name" : "neha", "marks": 432, "sub" : "maths"}

# myvar = pd.Series(colories, index=["name", "marks"])
# print(myvar)

# data = {
#     "names" : ['nisha', 'rohan', 'vidyut'],
#     "marks" : [89, 50, 70]
# }

# df = pd.DataFrame(data)
# print(df.loc[1])


# data = {
#     "names" : ['nisha', 'rohan', 'vidyut'],
#     "marks" : [89, 50, 70]
# }

# df = pd.DataFrame(data, index=["a","b","c"])
# print(df)

# df = pd.read_csv('data.csv')
# print(df.to_string())

# df = pd.read_csv('data.csv')
# print(df)

# df= pd.read_json("data.json")
# print(df.to_string())

# df = pd.read_csv('data.csv')
# new_df = df.dropna()
# print(new_df.to_string())
# print(new_df.info())

# df = pd.read_csv('data.csv')
# df.dropna(inplace= True)
# # print(df.to_string())
# print(df.info())

# df = pd.read_csv("data.csv")
# df.fillna(22222, inplace= True)
# print(df.to_string())

# df = pd.read_csv('data.csv')
# df["Calories"].fillna(555, inplace= True)
# print(df.to_string())

# df = pd.read_csv('data.csv')
# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace= True)
# print(df.to_string())
# print(x)

# df = pd.read_csv('data.csv')
# x = df["Calories"].median()
# df["Calories"].fillna(x, inplace= True)
# print(df.to_string())
# print(x)

# df = pd.read_csv("data.csv")
# x = df["Calories"].mode()
# df["Calories"].fillna(x, inplace= True)
# print(df.to_string())

# df = pd.read_csv("data.csv")
# df["Date"] = pd.to_datetime(df["Date"])
# print(df.to_string())

# df = pd.read_csv("data.csv")
# df.dropna(subset=["Calories"], inplace = True)
# print(df.to_string())

# df = pd.read_csv("data.csv")
# df.loc[7,'Duration'] = 45
# print(df.to_string())


df = pd.read_csv("data.csv")
# for x in df.index:
#     if df.loc[x, "Duration"] > 60 :
#         df.loc[x, "Duration"] = 60

# print(df.to_string())


# for x in  df.index:
#     if  df.loc[x, "Duration" ] < 60:
#         df.drop(x, inplace = True)
# print(df.to_string())
my= df.head(20)
# print(my.duplicated())
my. drop_duplicates(inplace= True)



print("hello")