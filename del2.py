from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json



#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = localhost.connect("localhost","beginneraccount","cookies","beginneraccount$tutorial")

c = conn.cursor()


#consumer key, consumer secret, access token, access secret.
ckey=	"5P2X3xByvD9WDHEZj9gEWbeJn"
csecret="hh2AawXhACIwNmVBKqL9M7v4CSp0fh8qWOF0Fz3DsoTxeiqQoz"
atoken="231152429-5aVjqYQYX7kAzCqGcAC6uRNE12Gz9xP0KnQdJUyE"
asecret="hpLNUflrRSatx4CpsALtSI4XA38ypiOjny9JpYB1Q1SeH"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        username = all_data["user"]["screen_name"]

        c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))

        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
