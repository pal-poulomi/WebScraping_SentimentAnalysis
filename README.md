# WebScraping_SentimentAnalysis
Web scraping of data from FinViz.com and performing a Sentiment Analysis on the articles

## Data collection and preprocessing
- The goal of this project is scrape web data - here, latest FinViz articles (February 2023), analyze them and figure out how the sentiment of those news articles are for the particular companies chosen here
- Data is collected from FinViz website
- We choose the tickers for Netflix, Google and AMD
- Iterate over each ticker to fetch the html data
- Parse the html data to a readable format (list of lists)
- Creating a pandas dataframe from the parsed data and using just the required columns such as ticker, date, time and title (text data)
- Checking the size of data which is 300 x 4

## Model Building
- Using the NLTK library and its Sentiment Analyzer Vader as our model, we calculate the sentiment associated with each title
- Applying the Vader polarity score on the title column - we use the compound score instead of positive, negative or neutral scores because its a better indicator with values between -1 to 1 where -1 indicates extremely negative and 1 indicates extremely positive
- Formatting the date column
- Grouping the data by ticker and date to have one row pertaining to each day (originally there are multiple rows for each ticker for each day with different time stamps) and use the mean of the compound score
- Transforming the data to the format with date as one column and the each ticker as individual columns populates with mean compound scores for each corresponding dates

## Visualization and Insights
- Plotting the results as a bar chart using matplotlib
- The results show that for the 3 tickers chosen, during the first few days of the month stock news associated with Google were mostly negative whereas the stocks news related to Netflix has been negative towards the later half of the month
- For AMD the stock news sentiment has been mostly positive throughout
- This project can be used for any ticker of our choice and can also be used in real life scenarios to keep track of the sentiments asociated with the stock news of the companies that an individual is interested in in real time


