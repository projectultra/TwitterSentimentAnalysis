from django.db import models
class Tweet(models.Model):
    text = models.CharField(max_length=280)
    sentiment = models.CharField(max_length=10)
    rawtweet = models.CharField(max_length=300,null=True)