import numpy as np
import pandas as pd

data = pd.read_excel('C:\Users\hp\Desktop/test.xlsx')
df = pd.DataFrame(columns = data.columns)
t = 1
for i in range(len(data)):
 buss = data.iloc[i]['股票名称']
 series = data.iloc[i]
 if '高新' in buss or '半导体' in buss or '集成电路' in buss:
  t += 1
  print(series)
  df.append(series)
print(df)
