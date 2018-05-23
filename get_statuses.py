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
    all_tweets = []
    screen_name = 'DanFromAbove'
    new_tweets = api.GetUserTimeline(screen_name=screen_name,count=200)
    all_tweets.extend(new_tweets)
    oldest = all_tweets[-1].id - 1
    while len(new_tweets) > 0:		
	    new_tweets = api.GetUserTimeline(screen_name = screen_name,count=200,max_id=oldest)
	    all_tweets.extend(new_tweets)
	    oldest = all_tweets[-1].id - 1
	    print("...%s tweets downloaded so far" % (len(all_tweets)))
    return all_tweets

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

