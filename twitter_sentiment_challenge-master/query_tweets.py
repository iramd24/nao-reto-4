import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost',
                                    database='tweets',
                                    user='root',
                                    password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tweets.tweets")

        myresult = cursor.fetchall()

        for x in myresult:
            print(x)

except Error as e:
            print("Error while connecting to MySQL", e)

finally:
    if conn.is_connected():
        conn.close()
        print("MySQL connection is closed")
