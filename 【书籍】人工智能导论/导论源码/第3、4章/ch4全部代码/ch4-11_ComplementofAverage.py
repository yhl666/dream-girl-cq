#ch4-11_ComplementofAverage
from pandas import Series,DataFrame, np
from numpy import nan as NA
data=Series([1.0,NA,3.5,NA,7])
print(data)
print("...........\n")
print(data.fillna(data.mean()))