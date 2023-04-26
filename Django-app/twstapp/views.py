import keras
import pickle
import re
import nltk
import numpy as np
import snscrape.modules.twitter as sntwitter
from datetime import datetime
from django.shortcuts import render
from .models import Tweet

def search(request):
    return render(request, 'search.html')
 
def fetch_tweets(request):
    tag = request.POST.get('tag')
    max_results = 20
    # Analyze sentiment using my ML model
    mlmodel=keras.models.load_model(r'twstapp/models')
    file = open(r'twstapp/vocab.pkl','rb')
    vocab=pickle.load(file)
    vectorizer = keras.layers.TextVectorization(max_tokens=10000, output_mode='int', output_sequence_length=20, vocabulary=vocab)
    Tweet.objects.all().delete()
    for rtweet in sntwitter.TwitterSearchScraper(tag,mode=sntwitter.TwitterSearchScraperMode.LIVE).get_items():
        if max_results > 0:
            max_results =max_results- 1
        else:
            break
        text = preprocess(rtweet.__dict__['rawContent'])
        v=vectorizer([text])
        sentiment=mlmodel.predict(np.array(v))
        if sentiment[0][0] > sentiment[0][1]:
            t = Tweet(text=text, sentiment='negative', rawtweet=rtweet.__dict__['rawContent'])
        else:
            t = Tweet(text=text, sentiment='positive', rawtweet=rtweet.__dict__['rawContent'])
        # Save results to the database
        t.save()
    tweets = Tweet.objects.all()
    context = {'tweets': tweets}
    return render(request, 'results.html', context)

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