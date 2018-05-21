import requests
import twitter
import _pickle as cPickle
import sys
import random
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret

def get_api():
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)
    return api

def get_statuses_from_file():
    try:
        with open('status_list.p', 'rb') as fp:
            status_list = cPickle.load(fp)
    except:
        print("Could not open tweet data")
        sys.exit(1)
    return status_list

def post_status(api, status_string):
    raw_text = status_string.text
    lol_text = ''.join(random.choice((x,y)) for x,y in zip(raw_text.upper(),raw_text.lower()))
    api.PostUpdate(lol_text)
    print("Posted to twitter")

def run_produce_tweets():
    api = get_api()
    status_list = get_statuses_from_file()
    post_status(api, random.choice(status_list))

def run_one_off_tweet():
    api = get_api()
    post_status(api, "I can post from the pi")

if __name__ == "__main__":
    api = get_api()
    print(api.VerifyCredentials())
    status_list = get_statuses_from_file()
    post_status(api, random.choice(status_list))

