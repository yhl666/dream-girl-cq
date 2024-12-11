#ch4-10_FillValueofColumns
from pandas import Series,DataFrame, np
from numpy import nan as NA
data=DataFrame(np.random.randn(7,3))
data.ix[:4,1]=NA
data.ix[:2,2]=NA
print(data)
print("...........")
print(data.fillna({1:111,2:222}))