import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


ckey = "RHI316f9DQO22MYdsCSQk3098"
csecret = "CGBGlVXcNnTWX4DjMaxhdusI8TjgBqn7IRrKK0vns1GgFyb3bN"
atoken = "1046186563737178113-5VYSQUNFEB7MYkHxDbWyHP3zLJ8VVp"
asecret = "GJ1GKY2nJx6wYGNjjw5zC3nMeUL2hgghcrqQMlJct7HN6"

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Armand:1998@127.0.0.1:5984')  
try:
    db = server.create('juegosolimpicosquito')
    #db = server.create('juegosolimpicos')
except:
    db = server['juegosolimpicosquito']    
    #db = server['juegosolimpicos']
'''===============LOCATIONS=============='''  


#twitterStream.filter(track=['Carapaz'])

twitterStream.filter(locations=[-4.2995,40.1175,-3.1529,40.9053]) #Madrid