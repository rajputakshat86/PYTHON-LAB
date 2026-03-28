import pandas as pd
import numpy as np

data1 = {'X':[2, 3, 4, 5, 6],
         'Y':[1, 2, 3, 4, 5],
         'Z':[2, 3, 4, 2, 3]}

data2 = {'X':[3, 2, 1, 2, 3],
         'Y':[2, 3, 2, 1, 2],
         'Z':[1, 2, 3, 2, 1]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

result = df1 ** df2

print(result)