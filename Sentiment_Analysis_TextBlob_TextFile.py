# -*- coding: utf-8 -*-
"""
@author: Ali Yusuf
"""

# Download TextBlob  model to conduct the sentiment analysis
# To download model use the following command in the Anaconda command prompt terminal, it will ask you in 3 minutes to proceed click enter and it will take around 2 minute more to download the full package
# conda install -c conda-forge textblob

from textblob import TextBlob 
import re #import regex
import pandas as pd
import seaborn as sns
import nltk #importing the nltk package
nltk.download('punkt') #download punkt sentence tokenizer to enable dividing text into sentences 

article_open = open('MCH focus group transcript.txt', 'r') #open text file
article = article_open.read() #read textfile
article_open.close() #close textfile 


#Removing references and extra spaces from the text stored in paragraphs using regex  
article_text_filtered= re.sub(r'\[[0-9]*\]',"", article) #to remove references ([] with a number inside)
article_text_filtered= re.sub(r'\s+'," ",article_text_filtered) #to remove extra spaces from the text stored in paragraphs

#Use the NLTK sentence tokenizer to break up the text into sentences
from nltk.tokenize import sent_tokenize #import sent_tokenize to enable breaking up text into sentences
tokenized_sent_text=sent_tokenize(article_text_filtered) #extract sentences out of article paragraph text
len(tokenized_sent_text) #Count the number of sentences  
print(f' the article has {len(tokenized_sent_text)} sentences') # Reporting number of sentences in a comment or text block


# we are setting our display options
pd.set_option("display.max_colwidth", 100)

# creating a dataframe showing the quotes in the list
df = pd.DataFrame(tokenized_sent_text, columns=["Sentences"])    

def get_scores(Sentences):  # create a function of analyzer model to analyze the quotes we added to the dataframe
    # analyze the quotes via the TextBlob analyzer
    textblob_scores = TextBlob(Sentences).sentiment.polarity
    return pd.Series({
        'Quotes': Sentences,
        'TextBlob': textblob_scores,
    })  # assign the analyzer to variables of the dataframe to display it


# we are creating a dataframe and recalling the function we created and applying it on the quotes
scores = df.Sentences.apply(get_scores)
# Take the numeric data of scores and round them to -1 Negative if they are below 0 and 1 Positive if greater than 0 (0 will remain 0 Neutral)
num = scores._get_numeric_data() 
num[num < 0] = -1
num[num > 0] = 1

# display the dataframe with color map (Red, Yellow, Green) depending on negative red and positive green with below 0.4 getting low and above 0.4 getting high to enable balancing with yellow
scores.style.background_gradient(cmap='RdYlGn', axis=None, low=0.4, high=0.4)
fig = sns.countplot(x='TextBlob', data=scores)
fg = fig.get_figure()
fg.savefig('TextBlob_Score.png') #save figure

# resource https://towardsdatascience.com/my-absolute-go-to-for-sentiment-analysis-textblob-3ac3a11d524