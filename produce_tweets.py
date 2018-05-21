import requests
import twitter
import _pickle as cPickle
import sys
import random

def get_api():
    api = twitter.Api(consumer_key='cpMdXihHf33UTfgYRb8ljpswA',
                      consumer_secret='ZdmdLSq9tYVnG0eHBG0DH56g2GB4xaiaDa4wYqfh2TRw8whQaM',
                      access_token_key='998650292857131014-awsoWfRhWAsKjQ7mZauJob2XnV0Uz8q',
                      access_token_secret='X9nVHXQaQJLH2qa0Vv1FBaRpNbHXWeVIKnXe8MbPcr8ri')
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
    api.PostUpdate(status_string.text)

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

