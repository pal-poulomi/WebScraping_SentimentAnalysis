from cgitb import text
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt


finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['NFLX', 'GOOG', 'AMD']

news_tables = {}

for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url=url, headers={'user-agent':'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, 'html')

    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table
    
#print(news_tables)


# Parse data

# amzn_data = news_tables['AMZN']
# amzn_rows = amzn_data.findAll('tr')
# #print(amzn_rows)

# for index, row in enumerate(amzn_rows):
#     if row.a is not None:
#         title = row.a.text
#         timestamp = row.td.text
#         print(timestamp + " " + title)

parsed_data = []

for ticker, news_table in news_tables.items():

    for row in news_table.findAll('tr'):
        if row.a is not None:
            title = row.a.text
            date_data = row.td.text.split(' ')

            if len(date_data) == 1:
                time = date_data[0]
            else:
                date = date_data[0]
                time = date_data[1]

            parsed_data.append([ticker, date, time, title])
#print(parsed_data)


# Applying sentiment analysis

df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])
print(df.head())
print(df.shape)

vader = SentimentIntensityAnalyzer()

#applying the vader polarity score on the title column
score = lambda title: vader.polarity_scores(title)['compound']
df['compound'] = df['title'].apply(score)

#print(df.head())

# visualization

df['date'] = pd.to_datetime(df.date).dt.date


mean_df = df.groupby(['ticker', 'date']).mean()
mean_df = mean_df.unstack()
mean_df = mean_df.xs('compound', axis="columns").transpose()
mean_df.plot(kind='bar')
plt.title("Sentiment Analysis of stocks news articles on FinViz")
plt.ylabel("Compound score")
plt.savefig("Sentiment Analysis.png")
plt.show()
#print(mean_df)