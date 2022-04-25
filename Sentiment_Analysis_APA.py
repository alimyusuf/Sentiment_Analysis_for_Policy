# -*- coding: utf-8 -*-
"""

@author: Ali Yusuf
"""
#Download snscrape model to scrape tweets and also vaderSentiment model to conduct the sentiment analysis
#To download models use the two following commands in the Anaconda command prompt terminal
#pip intall snscrape
#pip install vaderSentiment

import snscrape.modules.twitter as sntwitter
import pandas as pd
import seaborn as sns

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('cdc covid since:2022-03-01 until:2022-03-31').get_items()):
    if i>500:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text'])
tweets_df2.to_csv("Sentiment1.csv")

article_text = tweets_df2["Text"].tolist()

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #from vaderSentiment import SentimentIntensityAnalyzer (as we downloaded it using pip install)


analyzer = SentimentIntensityAnalyzer() #the seintmentintensityanalyzer that we just imported is saved as analyzer to ease its use
for sentence in article_text: #here we are taking all the 80 quotes in the list 
    vs = analyzer.polarity_scores(sentence) #then for each of these quotes we will use the analyzer to find the polarity score for each sentence and saved it as vs "VaderSentiment"
    print("{:>0} {}".format(sentence, (vs))) #we are formatting the output and printing each sentence with the vs scores next to it
    
pd.set_option("display.max_colwidth", 100) #we are setting our display options 

df = pd.DataFrame(article_text, columns = ["tweets"]) #creating a dataframe showing the quotes in the list

def get_scores(tweets): #create a function of both analyzer models to analyze the quotes we added to the dataframe
    vader_scores = analyzer.polarity_scores(tweets) #analyze the quotes via the vader analyzer
    
    return pd.Series({
        'Quotes': tweets,  
        'Vader': vader_scores['compound'],
    }) #assign the analyzers to variables of the dataframe to display it 

scores = df.tweets.apply(get_scores).round(0) #we are creating a dataframe and recalling the function we created and applying it on the quotes 

scores.style.background_gradient(cmap='RdYlGn', axis=None, low=0.4, high=0.4) #display the dataframe with color map (Red, Yellow, Green) depending on negative red and positive green with below 0.4 getting low and above 0.4 getting high to enable balancing with yellow

sns.countplot(x='Vader', data=scores)

