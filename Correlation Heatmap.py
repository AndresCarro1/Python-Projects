import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers= ['BTC-USD', 'SPY', 'GLD', 'AAPL', 'DOGE-USD', 'BZ=F', 'X']
start_date = '2022-01-01'

df = yf.download(tickers, start_date)['Adj Close']
df=df.dropna()

returns = df.pct_change()

correlation=returns.corr()
correlation

fig= plt.figure()
ax= fig.add_subplot(1,1,1)

ax.set_xticks(np.arange(correlation.shape[0])+0.5, minor= False)
ax.set_yticks(np.arange(correlation.shape[1])+0.5, minor= False)

heatmap= ax.pcolor(correlation, cmap= plt.cm.RdYlGn)
fig.colorbar(heatmap)

ax.set_xticklabels(correlation.index)
ax.set_yticklabels(correlation.columns)

plt.xticks(rotation=90)
heatmap.set_clim(-1,1)
plt.show()
