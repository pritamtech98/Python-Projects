import tweepy
import os
import time

CONSUMER_API_KEY = 'SBJHVTcUMdwTQGRzmftCluBOz'
CONSUMER_API_SECRET_KEY = 'jgFnTeIMGypWivAIXgtGuQ97WkEzO1OWIf0MSUrrCQTLadJlOJ'
ACCESS_TOKEN_KEY = '804584806562533376-dEBEwuk0ONlOGhsKP442339ujpTp5Ay'
ACCESS_TOKEN_SECRET_KEY = 'ydseAw8kQOdYT5oBO4gTf3b2SWBYcD3gx5cTzFtuW5Og9'

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET_KEY)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

# USed for getting 20 recent tweets on our timeline
# c = 1
# for tweet in public_tweets:
#     print(c, tweet.text, sep=' :-')
#     c+=1


# this is used o\to get the user info

user = api.get_user('twitter')
user_name = user.screen_name
# followers_count = user.followers_count
# print(user_name, followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

def get_last_tweet(file_name):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name+'.txt')
    var = os.path.exists(path)
    if var:
        f = open(file_name+'.txt', 'r')
        id = f.read()
        f.close()
        return id



def store_last_id(id, file_name):

    f = open(file_name+'.txt', 'w')
    f.write(str(id))
    f.close()

while True:
    mentions = api.mentions_timeline(since_id = get_last_tweet('id_list'), count = 4)
    for mention in reversed(mentions):
        text = mention.text.lower()
        last_id = mention.id
        store_last_id(last_id, 'id_list')
        if '#hellopritam' in mention.text.lower():
            try:
                api.update_status('@'+mention.user.screen_name+'   good morning', mention.id)
                print('messaged : ' + mention.user.screen_name)
            except Exception as err:
                print(err, 'message sending failed', sep='\n')

    print("Waiting for tweets : 20 secs...")
    time.sleep(20)







