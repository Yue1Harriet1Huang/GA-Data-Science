#Shirin Hashim
#10 minutes to pandas
#September 15, 2014

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Create Series
s = pd.Series([1,3,5,np.nan,6,8])
print s

#Create DataFrame with datetime and labels
dates = pd.date_range('20130101',periods=6)
print dates

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print df

#Create DataFrame with dictionary
df2 = pd.DataFrame({ 'A' : 1.,
					 'B' : pd.Timestamp('20130102'),
					 'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
					 'D' : np.array([3] * 4, dtype='int32'),
					 'E' : 'foo' })
print df2
print df2.dtypes






