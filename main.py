import tweepy
import os
import openai

api_key = os.environ['API_KEY']
api_secrets = os.environ['API_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']
username = os.environ['USERNAME']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
 
openai.api_key = os.environ['OPENAI_KEY'] 
response = openai.Completion.create(model="text-davinci-003", 
                                    prompt="hbr todays article, conclude by providing  link", 
                                    temperature=0.5,
                                    max_tokens=2048)

result = response.get("choices")[0].get("text")
print(result)

orig_string = result
list_of_lines = []
max_length = 180

while len(orig_string) > max_length:
    line_length = orig_string[:max_length].rfind(' ')
    list_of_lines.append(orig_string[:line_length])
    orig_string = orig_string[line_length + 1:]
list_of_lines.append(orig_string)
print (list_of_lines)


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
      
    print('Successful Authentication')
  
except Exception as e:
    print(e)


# response = openai.Image.create(
#   prompt="",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']
# print(image_url)