import mysql.connector
import json
import hashlib

with open('sqldatafile.json') as f:
    config = json.load(f)

conn = mysql.connector.connect(
    host=config['DB_HOST'],
    user=config['DB_USER'],
    password=config['DB_PASSWORD'],
    database=config['DB_DATABASE']
)
cursor = conn.cursor()
cursor.execute('SELECT username, en_passcode FROM users_basicdata;')
