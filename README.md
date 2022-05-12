# Sentiment_Analysis_for_Policy

### Overview
Sentiment analysis (also called opinion mining) is the process of computing linguistics and analyzing text in order to determine whether an expressed opinion or text towards a certain topic is positive, negative, or neutral.
In the context of policy analysis, we will be using sentiment analysis to compute polarity scores from certain text or comments/opinions regarding a policy to gauge whether this policy is been deemed as negative or positive by citizens. Accordingly, we will be using two sentiment analyzers (TextBlob and VaderSentiment) in order to analyze text and tweets (from Twitter.com) for polarity score and graph the output in a count plot. 


### Vader Sentiment Analyzer 
VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool tailored to social media sentiments. Vader combines a dictionary mainly using web-based media and social media, accordingly, it is best used to analyze more informal methods of communication including emojis and slang language. Therefore, we will be using Vader to conduct sentiment analysis on tweets on a certain policy topic to compute polarity score of tweets (assuming each tweet is an opinion) from Twitter.com. The scores will be in three categories (-1 Negative, 0 Neutral and 1 Positive). Accordingly, this tool can be easily and quickly  used to know what people on social media think about a policy topic. An important point to note here is that we are going to you a scraper model to extract tweets from twitter. 

#### Major Vader Script Areas

__Step 1: Downloading Vader and Twitter Scraper for use in Conda__

We will need to download snscrape model to scrape tweets and also vaderSentiment model to conduct the sentiment analysis. 
To download models use the two following commands separately in the Anaconda command prompt terminal, it should take around 5 minutes to download both models from pip:
_pip intall snscrape_
_pip install vaderSentiment_

To use these models in the script import them as follows: 
_from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer_
_import snscrape.modules.twitter as sntwitter_

__Step 2: Scraping Tweets from Twitter__

To scrape tweets we are writing a for loop that extracts items, these items are tweets which are extracted using an enumerate that iterates the values of a given search via the scraper. In the below code, the for loop extracts tweets according to the search topic or twitter handle (for e.g. @xyz) and also enables choosing the period for search by editing the since and until dates in a YYYY-MM-DD format (for e.g. 2022-01-01).
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('**The Search Topic or Twitter Handle** _since:2022-01-01 until:2022-05-01_').get_items()):
Further, the for loop will contain an if statement that aims to break the loop after taking a certain number of tweets as a sample (most recent tweets will be taken) and then appends it to an empty list according to the scraper details derived, which are the tweet date, ID and content (text). The number of tweets required can be adjusted as needed in the following code, it is 3000 tweets here: 
if i > _3000_:
    break
Tweets content will then be saved in a list to be used, and the date and ID will be disregarded as they are not needed for our analysis. 

__Step 3: Testing the Analyzer__

If a quick overview of tweets is required and in order to test the sentiment analysis model, we will be creating a for loop to go through the sentences in the list created (i.e. each tweet) and computing a score for it and printing the results. Further, we will store all tweets in a Pandas DataFrame to be used later.

__Step 4: Define a score pulling function__

In this stage, we will define a function that computes the polarity score of each sentence in a dataframe and saves the sentence along with its corresponding score in a Pandas Series columns in a dataframe. The reason for defining this function is to be able to move it to different scripts that analyze tweets or other methods. 

__Step 5: Apply function on Sentences and Plot Results__

Finally, we will apply the function to the sentences in the DataFrame we created in Step 3 of tweets that we scrapped. This will be saved in a dataframe that can also be printed later in ascending order to view most positive. An adjustment rounding is then made on scores to ensure we only have three categories (-1 Negative, 0 Neutral, +1 Positive). This will then be plotted using seaborn and saved as a figure. 


### TextBlob Sentiment Analyzer 
TextBlob is a Python library that processes textual data for sentiment analysis. It uses an averaging technique that takes each words and defines its polarity score (-1 is negative and +1 is positive, while scores around 0 are neutral). This score for each word then is used by TextBlob to derive the sentiment accordingly for longer texts and sentences. TextBlob uses a language library and movie reviews corpus to train its library on words, therefore, it is more useful when computing sentiment from documents, text files and customer feedback files. 
Accordingly, we will be implementing this analysis technique on a focus group transcript from the  Maternal and Child Health Bureau (*file can be found in the repository*). This will serve an example for analyzing text from focus groups, interviews, survey feedback and similar research methods which are widely used in evaluation of public policy. 

#### Major TextBlob Script Areas

__Step 1: Downloading TextBlob for use in Conda__

To download model use the following command in the Anaconda command prompt terminal:
_conda install -c conda-forge textblob_
In around 3 minutes of processing the prompt will ask whether to proceed, click enter and it will take around 2 minutes more to download the full package. 

To use the model, import it in the script as follows: 
_from textblob import TextBlob_

__Step 2: Opening and Filtering the Text__

The _open('textfile_name', 'r')_ command is used to open the file as TextIO which is a generic form that does not recognize the text but calls it, therefore, to use the text we are using .read() function on it. Further, we will be using Regular Expression (also called regex or re) which will help us identify characters and patterns in text to filter the text accordingly. From re, we will use the .sub() command which searches for a given pattern and subsitutes it with matched strings. First filter will be (_re.sub(r'\[[0-9]*\]',"", 'filename'_), this will enable removing references with numbers inside which are usually present in articles, for example [1]. Second filter will be (_re.sub(r'\s+'," ", 'filename'_), to remove the extra spaces in text. 

__Step 3: Tokenizing Sentences__

To be able to read each sentence alone, the process of tokenization is required to separate a block of text (our text file) into sentences. Accordingly, we will be using the natural language toolkit ("NLTK") package to import a sentence tokenizer (sent_tokenize). This sentence tokenizer will be applied on the textfile and that will lead to the file being separated into sentences. In the script, we print the length of tokenized text to know the number of sentences in our text file. The sentences will further be stored in a Pandas DataFrame for ease of use later.

__Step 4: Define a score pulling function__

In this stage, we will define a function that computes the polarity score of each sentence in a dataframe and saves the sentence along with its corresponding score in a Pandas Series columns in a dataframe. The reason for defining this function is to be able to move it to different scripts that analyze tweets or other methods. 

__Step 5: Apply function on Sentences and Plot Results__

Finally, we will apply the function to the sentences in the DataFrame we created in Step 3 of tokenized sentences from our text file. This will be saved in a dataframe that can also be printed later in ascending order to view most positive. An adjustment rounding is then made on scores to ensure we only have three categories (-1 Negative, 0 Neutral, +1 Positive). This will then be plotted using seaborn and saved as a figure. 


### Results and Deliverables
Both scripts will finally give us a count plot figure, this count plot figure will count the number of tweets which are positive, neutral and negative to determine how the overall sentiment is. In our implementation example of Vader on tweets regarding CDC and COVID, we found that the overall sentiment was mostly negative as shown in the plot in the repository (Vader_Score.png). While in our implementation example of the focus group transcript, we found that the sentiment was mostly neutral to positive. 


### Policy Usage of Sentiment Analysis
The sentiment analysis described can be used in the following areas: 
- Post questions on social media and analyze post comments
- Analyze survey results for opinions and sentiment
- Identify policy issues by gathering the most recurring negative opinions 
- Analyze the most positive opinions for policy solutions
- Measure citizen’s satisfaction and receive feedback on actual policy outcomes 
- Track policy reaction and support over-time
- Scrape the social media platforms or articles to collect the most discusses policy areas 


### Sentiment Analysis Issues to Consider
Some issues or biases to take into consideration when conducting sentiment analysis are: 
(1) **Subjectivity:** There are many opinion based reviews. A way to overcome this is to look at subjectivity scores that can also be derived via the sentiment analysis tools. 
(2) **Sarcasm:** People sometime mean the opposite of they write, therefore, when analyzing content from social media, a suitable analysis tool should be used that can interpret slang language better (like Vader). 
(3) **Context:** The context is very important as the same word or sentences can have two different meanings. For instance, an answer of "All of it", can be both answered towards a question asking "What do you dislike about a policy?" and also a question that asks "What do you like about a policy?". Therefore, taking a sample of sentences and analyzing the context helps overcoming this issue. 
