import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import numpy as np
from os import system

print ("Ticker?")
Ticker = input()

print ("Start date?")
StDate = input()

try:
    df = yf.download(Ticker, start = StDate)

    df["EMA12"] = df.Close.ewm(span=12).mean()
    df["EMA26"] = df.Close.ewm(span=26).mean()
    df["MACD"] = df.EMA12-df.EMA26
    df["Signal"] = df.MACD.ewm(span = 9).mean()

    plt.subplot(2,1,2)
    plt.plot(df.Signal, color="red")
    plt.plot(df.MACD)
    Buy, Sell = [], []
    for i in range(2, len(df)):
       if df.MACD.iloc[i] > df.Signal.iloc[i] and df.MACD.iloc[i-1] < df.Signal.iloc[i-1]:
            Buy.append(i)
       elif df.MACD.iloc[i] < df.Signal.iloc[i] and df.MACD.iloc[i-1] > df.Signal.iloc[i-1]:
           Sell.append(i)

    print("Dates sales:")
    print(df.iloc[Sell].index, df.iloc[Sell].Close)
    sellinfo = df.iloc[Sell].index, df.iloc[Sell].Close

    print("Bullish dates:")
    print(df.iloc[Buy].index, df.iloc[Buy].Close)
    buyinfo = df.iloc[Buy].index, df.iloc[Buy].Close

    df1 = pd.DataFrame.from_records(buyinfo)
    print(df1)

    dictionary = df1.to_dict()

    keys = list(dictionary.keys())
    countkeys = keys[-1]
    print("count:",countkeys)


    print("Last info for buy:")
    print(dictionary[countkeys])

    print("Last date for buy:")
    date1 = dictionary[countkeys][0]
    dateforbuy = date1.strftime("%d/%m/%Y")
    print(dateforbuy)

    print("########")

    print("Today date:")
    now = datetime.now()
    datetoday = now.strftime("%d/%m/%Y")
    print(datetoday)

    print("Yesterday date:")
    yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
    print(yesterday)

    print("FINAL DECISION:")
    if str(dateforbuy) == str(yesterday):
        print("MACD = BUY")
    else:
        print("TAKE NO ACTION")

    plt.subplot(2,1,1)
    plt.scatter(df.iloc[Buy].index, df.iloc[Buy].Close, marker="o", color="green")
    plt.scatter(df.iloc[Sell].index, df.iloc[Sell].Close, marker="o", color="red")
    plt.plot(df.Close, color="black")

    plt.show()

except (IndexError, NameError):
    print ("Wrong input, please check ticker and date")




