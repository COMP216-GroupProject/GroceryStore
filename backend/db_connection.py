import mysql.connector
import datetime

db_connection = None

def getSqlConnection():
    global db_connection
    print("Establishing connection to mysql db")

    if db_connection is None:
        db_connection = mysql.connector.connect(user='root', password='root', database='gs');
        print("db connected : ", db_connection)

    return db_connection
