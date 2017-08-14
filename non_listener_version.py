#This one doesn't use a listener, will check your tweets every two minutes
#This one also doesn't do battle raid Ids.
import tweepy
import settings
import time

#OAUTH
auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)
api = tweepy.API(auth)

def find_hashtags(tweet):
    text = tweet.text
    split = text.split(" ")
    hashtag_list = []
    for word in split:
        if (word.startswith("#")):
            hashtag_list.append(word)
    return hashtag_list

def parse_hashtags(hashtag_list):
    for hashtag in hashtag_list:
        if (hashtag == settings.delete_hashtag):
            return True
    return False

def delete_tweet(tweet):
    api.destroy_status(tweet.id)
    return True


while(True):
    print "Checking Tweets..."
    user_tweets = api.user_timeline()
    delete_list = []
    for tweet in user_tweets:
        success = False
        if (tweet.text.startswith("RT") != True) and (tweet.text.startswith("@") != True):
            hashtag_list = find_hashtags(tweet)
            if (parse_hashtags(hashtag_list)):
                print tweet.text
                print ""
                delete_list.append(tweet)
    for tweet in delete_list:
        delete_tweet(tweet)
    print "All tweets related to GBF have been deleted!"
    print "Sleeping..."
    time.sleep(120)
