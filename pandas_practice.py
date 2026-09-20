from operator import index
import numpy as np
import pandas as pd
# 1  series and their their ways of creaation
# 1.1creating a series from a list
mark=[45,56,58,37,78]
marks_series=pd.Series(mark)
print(marks_series)

# 1.2 creating a series from  a dictionary
dict={
    "ali": 56,
    "Zahid": 90,
    "Haroon": 67
}
dict_marks=pd.Series(dict)
print(dict_marks)   

# 1.2.1 how to access the values of series using index or label
print("Zahid ullah's mark is", dict_marks["Zahid"])

#1.3 creating a series with customized index
marks=[45,65,67]
marks_with_custom_index=pd.Series(marks, index=["ali","ZZaid ullah","haroon"])
print(marks_with_custom_index)

#1.4 creating a series from numpy array
list=[45,56,87,9,89]
list_array=np.array(list)
print(list_array)
#1.5 creating a series from scalar value
series_single_value= pd.Series(100, index=["haroon", "sahil","Basit"])
print(series_single_value)


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