#New and improved! Event based deletion!

import tweepy #tweepy api wrapper
import settings #settings module
import re

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    """
        @param tweet: The tweet to parse

        Extracts hashtags from a tweet.

        @return list: The list of hashtags in the tweet
    """
    def find_hashtags(self, tweet):
        text = tweet.text
        split = text.split(" ")
        hashtag_list = []
        for word in split:
            if (word.startswith("#")):
                hashtag_list.append(word)
        return hashtag_list

    """
        @param hashtag_list: The list of hashtags in a tweet

        Linear search implementation to find the target hashtag in
        the list of hashtags found within a tweet

        @return boolean: returns whether the target hashtag was found
    """
    def parse_hashtags(self, hashtag_list):
        for hashtag in hashtag_list:
            if (hashtag == settings.delete_hashtag):
                return True
        return False


    def find_battle_id(self, tweet):
        text = tweet.text
        if (bool(re.search(settings.regex, text))):
            return True
        return False


    """
        @param status: The tweet that the listener found

        Listener function. Will check hashtags and delete
        if target hashtag is found
    """
    def on_status(self, status):
        delete = False
        tweet = status
        if (self.find_battle_id(tweet)):
            delete = True
        if (tweet.text.startswith("RT") != True) and (tweet.text.startswith("@") != True):
            hashtag_list = self.find_hashtags(tweet)
            if (self.parse_hashtags(hashtag_list)):
                delete = True
        if (delete):
            print "Deleting GBF related tweet..."
            self.api.destroy_status(tweet.id)

    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        pass

    def on_limit(self, track):
        """Called when a limitation notice arrives"""
        pass

    def on_error(self, status_code):
        """Called when a non-200 status code is returned"""
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        """Called when stream connection times out"""
        print 'Snoozing Zzzzzz'

    def on_disconnect(self, notice):
        """Called when twitter sends a disconnect notice
        Disconnect codes are listed here:
        https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
        """
        print (notice)

    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        print (notice)

def main():
    """
        Tweepy oAuth handling.
        Uses settings taken from settings.py
    """
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)
    api = tweepy.API(auth)

    """
        Grabs the current user's id to track stream
    """
    cur_user = api.me()
    user_list = [str(cur_user.id)]

    """
        Instantiate listener and filter incoming tweets to
        only select from a particular user
    """
    myStreamListener = MyStreamListener(api = api)
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(user_list)

"""
    Some weird python thing to make main work(?).
    Look into this.
"""
if __name__ == "__main__":
    main()
