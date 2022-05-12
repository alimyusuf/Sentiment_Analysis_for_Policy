# Sentiment_Analysis_for_Policy

### Overview
Sentiment analysis (also called opinion mining) is the process of computing linguistics and analyzing text in order to determine whether an expressed opinion or text towards a certain topic is positive, negative, or neutral.
In the context of policy analysis, we will be using sentiment analysis to compute polarity scores from certain text or comments/opinions regarding a policy to gauge whether this policy is been deemed as negative or positive by citizens. Accordingly, we will be using two sentiment analyzers (TextBlob and VaderSentiment) in order to analyze text and tweets (from Twitter.com) for polarity score and graph the output in a count plot. 

### TextBlob Sentiment Analyzer 
TextBlob is a Python library that processes textual data for sentiment analysis. It uses an averaging technique that takes each words and defines its polarity score (-1 is negative and +1 is positive, while scores around 0 are neutral). This score for each word then is used by TextBlob to derive the sentiment accordingly for longer texts and sentences. TextBlob uses a language library and movie reviews corpus to train its library on words, therefore, it is more useful when computing sentiment from documents, text files and customer feedback files. 
Accordingly, we will be implementing this analysis technique on a focus group transcript from the  Maternal and Child Health Bureau (*file can be found in the repository*). This will serve an example for analyzing text from focus groups, interviews, survey feedback and similar research methods which are widely used in evaluation of public policy. 

#### Major TextBlob Script Areas
__Step 1: Downloading TextBlob for use in Conda__
To download model use the following command in the Anaconda command prompt terminal:
_conda install -c conda-forge textblob_
In around 3 minutes of processing the prompt will ask whether to proceed, click enter and it will take around 2 minutes more to download the full package. 

__Step 2: Opening and Filtering the Text__
The _open('textfile_name', 'r')_ command is used to open the file as TextIO which is a generic form that does not recognize the text but calls it, therefore, to use the text we are using .read() function on it. Further, we will be using Regular Expression (also called regex or re) which will help us identify characters and patterns in text to filter the text accordingly. From re, we will use the .sub() command which searches for a given pattern and subsitutes it with matched strings. First filter will be (_re.sub(r'\[[0-9]*\]',"", 'filename'_), this will enable removing references with numbers inside which are usually present in articles, for example [1]. Second filter will be (_re.sub(r'\s+'," ", 'filename'_), to remove the extra spaces in text. 

__Step 3: Tokenizing Sentences__
To be able to read each sentence alone, the process of tokenization is required to separate a block of text (our text file) into sentences. Accordingly, we will be using the natural language toolkit ("NLTK") package to import a sentence tokenizer (sent_tokenize). This sentence tokenizer will be applied on the textfile and that will lead to the file being separated into sentences. In the script, we print the length of tokenized text to know the number of sentences in our text file. The sentences will further be stored in a Pandas DataFrame for ease of use later.

__Step 4: Define a score pulling function__
In this stage, we will define a function that computes the polarity score of each sentence in a dataframe and saves the sentence along with its corresponding score in a Pandas Series columns in a dataframe. The reason for defining this function is to be able to move it to different scripts that analyze tweets or other methods. 

__Step 5: Apply function on Sentences and Plot Results__
Finally, we will apply the function to the sentences in the DataFrame we created in Step 3 of tokenized sentences from our text file. This will be saved in a dataframe that can also be printed later in ascending order to view most positive. An adjustment rounding is then made on scores to ensure we only have three categories (-1 Negative, 0 Neutral, +1 Positive). This will then be plotted using seaborn and saved as a figure. 


### Results and Deliverables
