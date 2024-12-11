#ch4-12_JudgeRepleateofData
from pandas import Series,DataFrame, np
from numpy import nan as NA
import pandas as pd
import numpy as np
data=pd.DataFrame({'k1':['one']*3+['two']*4, 'k2':[1,1,2,2,3,3,4]})
print(data)
print("........\n")
print(data.duplicated())