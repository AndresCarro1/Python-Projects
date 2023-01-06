# Python-Projects

GUESS THE NUMBER
is a simple guess the number game, where the player can try up to 6 times to get the randomly generated number right.
It is basically and if/else loop of 6 iterations, broken if the number is guessed.
If a character other than an integer is submitted, the rule violation is notified and the game is terminated.

BTC CANDLESTICKS
displays the candlestick chart of Bitcoin prices (expressed in US Dolars) for the past 30 days.
First it uses CoingeckoAPI to retireve the relevant data, then it focus only in Prices and turns it into a Pandas DataFrame.
Then it transforms the Timestamp into a column called Date, mapping unix_to_datetime to convert it into readable date.
After that, Price data can now be grouped by Date, which allows us to pinpoint the data needed for the candlesticks.
Finally, plotly is used to create the chart.

PRICERETRIEVERML
sets a function getMercadoLibrePrice, which uses Beautiful Soup to scan a product's HTML for its defined price in the code.
Then the function price is set, which calls getMercadoLibrePrice and asks for a product's URL as second argument, finally 
printing it's price.

MACD
plots a MACD indicator (see https://www.investopedia.com/terms/m/macd.asp for further reference on the indicator) for a 
requested stock, from a requested date to present time. It asks for a ticker, which is a company ID acronym commonly 
used in Stock Markets (eg for Tesla is TSLA), and a base date and then builds the indicator components (exponential
moving averages, Signal and MACD) based on pricing data collected from Yahoo Finance. Based on the tecnical rules for the
indicator, Buy and Sell dates are sorted out and the former are arranged in a dictionary. After that, as we are dealing with
closing prices (eg. the last market price for each day), the script checks if the last Buy date is yesterday and, if so, 
prints a BUY alert (meaning a buy order should be submitted today at market's opening time). Otherwise, it advises not to
take any action. Finally, MACD's graphic is plotted for visual reference. If either an invalid ticker or date is input, an 
error message is returned.


