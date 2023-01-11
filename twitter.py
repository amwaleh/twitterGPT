import tweepy
import os

api_key = os.environ['API_KEY']
username = os.environ['USERNAME']
api_secrets = os.environ['API_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def update_status(list_of_lines):
  try:
    api.verify_credentials()

    tweet = list_of_lines [0]
    resp = api.update_status(tweet)
    print(tweet)
  
    if len(list_of_lines) > 1:
      for i, line in enumerate(list_of_lines[1:]):
        tweet = f"{username} {i+1}/{len(list_of_lines)} {line}"
        api.update_status(tweet, in_reply_to_status_id=resp.id )
        print (tweet)
      
  
  except Exception as e:
    print(e)

