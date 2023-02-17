import mysql.connector
import json

with open('sqldatafile.json') as f:
    config = json.load(f)
