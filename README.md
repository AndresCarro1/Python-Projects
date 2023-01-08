# Python-Projects

> Note: for each project you will find in the .py all the libraries needed for the scripts to run.

## GUESS THE NUMBER
It is a simple guess the number game, where the player can try up to 6 times to get the randomly generated number right.
It is basically and if/else loop of 6 iterations, broken if the number is guessed.
If a character other than an integer is submitted, the rule violation is notified and the game is terminated.

![image](https://user-images.githubusercontent.com/111796101/211201603-d9fe5bd2-fc4e-4617-a8cb-a78a63fa3ef7.png)



## BTC CANDLESTICKS
It displays the candlestick chart of Bitcoin prices (expressed in US Dolars) for the past 30 days.
First it uses CoingeckoAPI to retireve the relevant data, then it focus only in Prices and turns it into a Pandas DataFrame.
Then it transforms the Timestamp into a column called Date, mapping unix_to_datetime to convert it into readable date.
After that, Price data can now be grouped by Date, which allows us to pinpoint the data needed for the candlesticks.
Finally, plotly is used to create the chart.![BTC Candlesticks Example](https://user-images.githubusercontent.com/111796101/211084396-aba73f33-69eb-4627-aa0b-f683c96a4f7e.jpg)


## PRICERETRIEVERML
It sets a function getMercadoLibrePrice, which uses Beautiful Soup to scan a product's HTML for its defined price in the code.
Then the function price is set, which calls getMercadoLibrePrice and asks for a product's URL as second argument, finally 
printing it's price.


## MACD
It plots a MACD indicator (see https://www.investopedia.com/terms/m/macd.asp for further reference on the indicator) for a 
requested stock, from a requested date to present time. It asks for a ticker, which is a company ID acronym commonly 
used in Stock Markets (eg for Tesla is TSLA), and a base date and then builds the indicator components (exponential
moving averages, Signal and MACD) based on pricing data collected from Yahoo Finance. Based on the tecnical rules for the
indicator, Buy and Sell dates are sorted out and the former are arranged in a dictionary. After that, as we are dealing with
closing prices (eg. the last market price for each day), the script checks if the last Buy date is yesterday and, if so, 
prints a BUY alert (meaning a buy order should be submitted today at market's opening time). Otherwise, it advises not to
take any action. Finally, MACD's graphic is plotted for visual reference. If either an invalid ticker or date is input, an 
error message is returned.![MACD Apple Example](https://user-images.githubusercontent.com/111796101/211083982-1c66bd45-bd8b-4987-9fbd-be2cd07b82db.png)


## CORRELATION HEATMAP
It takes a set of tickers, from a requested starting date, and connects to Yahoo Finance to retrieve its' daily closing prices
(ignoring empty values, for example on holidays or weekends for stocks). After that, a correlation between all tickers' daily
price changes is performed. Finally, the rest is setting up the heatmap (plotting the relationships, the colors, axis labels. 
This chart is useful to analyze in which way different prices (stocks, cryptos, ETFs, raw materials, etc) a related, which could
for example lead to trading oportunities (eg. one asset's price has increased and it's correlated asset prices still hasn´t, then
it´s time to buy the latter as it should go up).![Correlation Heatmap Example](https://user-images.githubusercontent.com/111796101/211084010-c24413a6-c0f4-4c1d-b6ef-772aab3f14ee.png)



