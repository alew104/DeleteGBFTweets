#New and improved! Event based deletion!

import tweepy
import settings

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def find_hashtags(self, tweet):
        text = tweet.text
        split = text.split(" ")
        hashtag_list = []
        for word in split:
            if (word.startswith("#")):
                hashtag_list.append(word)
        return hashtag_list

    def parse_hashtags(self, hashtag_list):
        for hashtag in hashtag_list:
            if (hashtag == settings.delete_hashtag):
                return True
        return False

    def on_status(self, status):
        print (status.text)
        if (status.text.startswith("RT") != True) and (status.text.startswith("@") != True):
            hashtag_list = self.find_hashtags(status)
            if (self.parse_hashtags(hashtag_list)):
                print "Deleting GBF related tweet..."
                self.api.destroy_status(status.id)


def main():
    #authentication
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)
    api = tweepy.API(auth)

    cur_user = api.me()
    user_list = [str(cur_user.id)]

    myStreamListener = MyStreamListener(api = api)
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(user_list)

if __name__ == "__main__":
    main()
