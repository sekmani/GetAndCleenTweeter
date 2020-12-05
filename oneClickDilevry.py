from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

apikey = '0Gz01a6oCZ9YrGea7vF3uCIc3'
apisecret = 'yqAyQ4E5mzdgbBVCSpZ0B7JQmXglp2MVvnUzdbliUYe3iHixAu'
token = '1331646107714285569-Ow1g5ybOKFO8PT0Kih3VNNeLB3TpSe'
tokensecret = 'IMMtwt9jCGkqo4hJx8fYi1hWigEuiS6f0egWQgIQ9LTpu'


i=0
class listener(StreamListener):

    def on_data(self, data):
        try:
            global i
            i=i+1
            TheTime=data.split('{"created_at":"')[1].split('","id')[0]
            tweet=data.split(',"text":"')[1].split('","source')[0]

            saveThis=open("music_Tweet.csv","a")
##            saveFile =open("trump.csv","a")
##            saveFile.write(data)
            dataSplitted=str("Time:")+TheTime+str(" tweet:")+tweet
            saveThis.write(dataSplitted)
##            saveFile.write("\n")
##            saveFile.close()
            saveThis.write("\n")
            saveThis.write(str(i))
            saveThis.write("\n")
            saveThis.close()
            return True
        except Exception as e:
            print('failed ',str(e))
            time.sleep(5)
            
    def on_error(self, status):
        print (status)
        

auth = OAuthHandler(apikey, apisecret)
auth.set_access_token(token, tokensecret)


twitterStream= Stream(auth, listener())

twitterStream.filter(track=["music"])
        




  
