from apscheduler.schedulers.blocking import BlockingScheduler
from rq import Queue
from worker import conn
from get_statuses import run_get_statuses
from produce_tweets import run_produce_tweets, run_one_off_tweet

import sys

sched = BlockingScheduler()

q = Queue(connection=conn)

def get_statuses():
    q.enqueue(run_get_statuses)

def produce_tweets():
    q.enqueue(run_produce_tweets)

def one_off_tweet():
    q.enqueue(run_one_off_tweet)

# sched.add_job(one_off_tweet) #enqueue right away once
# sched.add_job(one_off_tweet, 'interval', minutes=1, start_date='2018-01-08 23:05:00')
sched.add_job(get_statuses) #enqueue right away once
sched.add_job(get_statuses, 'interval', hours=1, start_date='2018-05-22 21:10:00')
sched.add_job(produce_tweets) #enqueue right away once
sched.add_job(produce_tweets, 'interval', hours=1, start_date='2018-05-22 21:12:00')
sched.start()