import snscrape.modules.twitter as sntwitter
import nltk
import re
import keras
import pickle
import numpy as np
# Set search variables
search_words = "canada"
since_date = "2022-01-01"
until_date = "2022-01-07"

# Create a query string for snscrape
count=10
mlmodel=keras.models.load_model(r'twstapp/models')
file = open(r'twstapp/vocab.pkl','rb')
vocab=pickle.load(file)
vectorizer = keras.layers.TextVectorization(max_tokens=10000, output_mode='int', output_sequence_length=20, vocabulary=vocab)

def preprocess(tweet):
    
    #removes urls
    tweet = re.sub(r'http\S+','',tweet)
    
    tweet=re.sub(r'@\w+\s','',tweet)
    #remove usernames
    
    tweet = re.sub(r'[^\w\s]','',tweet).lower()
    #remove punctuation and makes it lowercase
    
    tweet = ' '.join([w for w in tweet.split() if len(w)>2])
    #remove words with len less than 2
    
    #tokenize the words
    tokenized_tweet = nltk.word_tokenize(tweet)
    lemmatizer = nltk.stem.WordNetLemmatizer()
    tweet = ' '.join([lemmatizer.lemmatize(w) for w in tokenized_tweet])
    return tweet

for tweet in sntwitter.TwitterSearchScraper(search_words,mode=sntwitter.TwitterSearchScraperMode.LIVE).get_items():
    text=preprocess(tweet.__dict__['rawContent'])
    v=vectorizer([text])
    sentiment=mlmodel.predict(np.array(v))
    print(tweet.__dict__['rawContent'],'=')
    if sentiment[0][0] > sentiment[0][1]:
        print('negative\n----------------END----------------\n')
    else:
        print('positive\n----------------END---------------\n')
    if count>0:
        count=count-1
    else:
        break
