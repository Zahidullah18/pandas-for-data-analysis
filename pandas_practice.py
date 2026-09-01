import pandas as pd
dict ={
    "name" :["zahid", "basit", "Shahid", "kamran", "farman", "haroon", "khan", "rayyan","abbas"],
    "marks" :[78,89,56,43,54,67,87,34,56],
    "city" :["peshawar", "islamabad", "lahore", "karachi", "quetta", "multan", "sialkot", "faisalabad", "rawalpindi"]
}
df= pd.DataFrame(dict)
print(df)
print("<==============================================>")
print(df.head(3))
print("<==============================================>")
print(df.tail(2))
print("<==============================================>")
print(df.describe())
print("<==============================================>")
print(df.size)
print(df.shape)

print("<==============================================>")
info = pd.read_csv("d:\\dmc.csv")
print(info)
print(info["Student"])

#print dataframe without index
print(info.to_string(index=False))
print(info.to_string(index=False))
print(info.to_string(index=False))

#sum of the columns
print(sum(info["Math"]))
print(sum(info["Computer"]))

print("===========================================")
print(info["Computer"][0])