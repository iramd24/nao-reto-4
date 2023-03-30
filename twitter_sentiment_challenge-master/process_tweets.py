import mysql.connector
from mysql.connector import Error
from textblob import TextBlob
from googletrans import Translator, constants

import re

translator = Translator()

try:
    conn = mysql.connector.connect(host='localhost',
                                    database='tweets',
                                    user='root',
                                    password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT id, text FROM tweets.tweets")

        myresult = cursor.fetchall()

        for row in myresult:
            for w in row[1].split("\n"):
                separator = '#'
                cleanTweet = w.split(separator, 1)[0]
                cleanTweet = " ".join(re.findall(r"[\w.!?]+", cleanTweet))
                print(cleanTweet)
                translatedTweet = translator.translate(cleanTweet)
                print(translatedTweet.text)
                analysis = TextBlob(translatedTweet.text)
                print(analysis.sentiment)
                score = analysis.sentiment.polarity
                subjectivityScore = analysis.sentiment.subjectivity
                polarity = ''
                subjectivity = ''
                if score < 0:
                    polarity = 'Negative'
                elif score == 0:
                    polarity = 'Neutral'
                else:
                    polarity = 'Positive'
                print(polarity)

                if subjectivityScore < 0.5:
                    subjectivity = 'Objective'
                elif subjectivityScore == 0.5:
                    subjectivity = 'Neutral'
                else:
                    subjectivity = 'Subjective'
                print(subjectivity)

                sql = "UPDATE tweets.tweets SET sentiment = %s, sentiment_score = %s, subjectivity = %s, subjectivity_score = %s, translated_text = %s WHERE id = %s"
                val = (polarity, score, subjectivity, subjectivityScore, translatedTweet.text, row[0])
                cursor.execute(sql, val)
                conn.commit()
                print("")


except Error as e:
            print("Error while connecting to MySQL", e)

finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")