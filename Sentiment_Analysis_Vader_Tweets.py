# -*- coding: utf-8 -*-
"""

@author: Ali Yusuf
"""
# Download snscrape model to scrape tweets and also vaderSentiment model to conduct the sentiment analysis
# To download models use the two following commands in the Anaconda command prompt terminal
# pip install snscrape
# pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import snscrape.modules.twitter as sntwitter
import pandas as pd
import seaborn as sns

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('CDC COVID since:2022-01-01 until:2022-05-01').get_items()):
    if i > 3000:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=[
                          'Datetime', 'Tweet Id', 'Text'])

article_text = tweets_df2["Text"].tolist()

# from vaderSentiment import SentimentIntensityAnalyzer (as we downloaded it using pip install)


# the seintmentintensityanalyzer that we just imported is saved as analyzer to ease its use
analyzer = SentimentIntensityAnalyzer()
for sentence in article_text:  # here we are taking all the 80 quotes in the list
    # then for each of these quotes we will use the analyzer to find the polarity score for each sentence and saved it as vs "VaderSentiment"
    vs = analyzer.polarity_scores(sentence)
    # we are formatting the output and printing each sentence with the vs scores next to it
    print("{:>0} {}".format(sentence, (vs)))

# we are setting our display options
pd.set_option("display.max_colwidth", 100)

# creating a dataframe showing the quotes in the list
df = pd.DataFrame(article_text, columns=["tweets"])


def get_scores(tweets):  # create a function of analyzer model to analyze the quotes we added to the dataframe
    # analyze the quotes via the vader analyzer
    vader_scores = analyzer.polarity_scores(tweets)

    return pd.Series({
        'Quotes': tweets,
        'Vader': vader_scores['compound'],
    })  # assign the analyzer to variables of the dataframe to display it


# we are creating a dataframe and recalling the function we created and applying it on the quotes
scores = df.tweets.apply(get_scores)
# Take the numeric data of scores and round them to -1 Negative if they are below 0 and 1 Positive if greater than 0 (0 will remain 0 Neutral)
num = scores._get_numeric_data()
num[num < 0] = -1
num[num > 0] = 1

# display the dataframe with color map (Red, Yellow, Green) depending on negative red and positive green with below 0.4 getting low and above 0.4 getting high to enable balancing with yellow
scores.style.background_gradient(cmap='RdYlGn', axis=None, low=0.4, high=0.4)
fig = sns.countplot(x='Vader', data=scores)
fg = fig.get_figure()
fg.savefig('Vader_Score.png') #save figure

# resources https://www.analyticsvidhya.com/blog/2021/06/twitter-sentiment-analysis-a-nlp-use-case-for-beginners/
# resource2 https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721
