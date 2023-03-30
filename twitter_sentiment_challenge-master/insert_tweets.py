import mysql.connector
from mysql.connector import Error

import pandas as pd
tweetdata = pd.read_csv('/Users/iramd24/Workspace/twitter_sentiment_challenge-master/tweets_sample.csv', index_col=False, delimiter = ',')
tweetdata.head()

try:
    conn = mysql.connector.connect(host='localhost',
                                    database='tweets',
                                    user='root',
                                    password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        #loop through the data frame
        for i,row in tweetdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO tweets.tweets (text,user,hashtags,tweet_creation_date,retweets,favs) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)

finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
