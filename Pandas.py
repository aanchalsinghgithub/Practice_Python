import numpy as np
import pandas as pd

labels=['a','b','c']
my_list =[10,20,30]
arr= np.array([10,20,30])
d={1:10,2:20,3:30}

# print(pd.Series(my_list))

pd.Series(my_list,index=labels)

pd.Series(arr)

pd.Series(d)

#Dataframes

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}

df=pd.DataFrame(data)
print(df)

data_list = [
    ['John', 28, 'New York', 65000],
    ['Anna', 34, 'Paris', 70000],
    ['Peter', 29, 'Berlin', 62000],
    ['Linda', 42, 'London', 85000]
]

df2=pd.DataFrame(data_list)
columns=[]