API_KEY = ""
API_SECRET = ""

import tweepy
import os;
import MySQLdb;

auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#queries = ["\"justin trudeau\"", "trudeau", "canadapm", "canadaprimeminister", "\"canada prime minister\"", "@justintrudeau", "@canadianpm" ];
#queries = ["\"Theresa May\"", "@theresa_may", "UKpm", "UKprimeminister", "\"UK primeminister\"", "@Number10gov" ];
queries = ["#sarcasm"];

tweets = [];

db = MySQLdb.connect("localhost","root","root","sys" );

cursor = db.cursor()

def func(x):
    t = tweepy.Cursor(api.search, q=x+" -RT", lang="en", show_user=True)
    for status in t.items(2000000):
        if ("http" not in status.text):
            statustext = status.text
            statusid = status.id
            statustime = status.created_at
            userid = status.user.id
            userloc = status.user.location
            #tweets.append([statustext,statusid,statustime,userid,userloc])
            sql = "INSERT INTO sarcasmdataset(userid,userlocation, statusid, statustime, tweet) VALUES (\'"+ str(userid) +"\', \'"+ str(userloc) +"\', \'"+ str(statusid) +"\', \'"+ str(statustime) +"\', \'"+ str(statustext) +"\')"
            try:
               cursor.execute(sql)
               db.commit()
            except:
               db.rollback()
    return tweets

query = "";

for x in range(len(queries)):
    if x == 0:
       query = queries[x] + "";
    else:
       query = query + " OR " + queries[x];

print(query);
func(query)

db.close();

