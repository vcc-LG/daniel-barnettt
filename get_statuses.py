import requests
import twitter
import _pickle as cPickle
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret

def get_api():
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)
    return api

def get_statuses(api):
    return api.GetUserTimeline(screen_name='DanFromAbove')

def save_data(status_list):
    with open('status_list.p', 'wb') as fp:
        cPickle.dump(status_list, fp)
    print('Data saved successfully')

def run_get_statuses():
    api = get_api()
    print(api.VerifyCredentials())
    status_list = get_statuses(api)
    save_data(status_list)

if __name__ == "__main__":
    api = get_api()
    print(api.VerifyCredentials())
    status_list = get_statuses(api)
    save_data(status_list)
    # post_status(api, statuses[0].text)

