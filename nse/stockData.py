from datetime import date
from nsepy import get_history
import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix

tcs = get_history(symbol='TCS',
                  start=date(2022, 1, 3),
                  end=date(2022, 2, 3))
infy = get_history(symbol='INFY', start=date(2022, 1, 3), end=date(2022, 2, 3))

tcs['MA50'] = tcs['Open'].rolling(50).mean()
tcs['MA200'] = tcs['Open'].rolling(200).mean()
tcs['Open'].plot(figsize=(15, 7))
tcs['MA50'].plot()
tcs['MA200'].plot()
# plt.show()
df = pd.DataFrame(tcs[['Close', 'Open', 'High', 'Low']])
print(tcs)
print(df.iloc[0].name)
arr = []
for i in range(len(tcs)):
    arr.append(tcs.iloc[i].name)
df = pd.DataFrame(arr, columns=['Date'])
print(df)
print(len(tcs))
print(tcs.keys())
