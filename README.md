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
