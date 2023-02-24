'''
import json

def write_db_credentials_to_json(host, user, password, database):
    # Create a dictionary with the database credentials
    credentials = {
        "DB_HOST": host,
        "DB_USER": user,
        "DB_PASSWORD": password,
        "DB_DATABASE": database,
    }

    # Write the credentials to a JSON file
    with open('sqldatafile.json', "w") as json_file:
        json.dump(credentials, json_file, indent=4)

# Example usage:
db_host = "sql7.freesqldatabase.com"
db_user = "sql7637488"
db_password = "yqTzuvhUBa"
db_database = "sql7637488"

write_db_credentials_to_json(db_host, db_user, db_password, db_database)


import hashlib

def sha256_hash(input_string):
    # Encode the input string as bytes
    input_bytes = input_string.encode('utf-8')
    
    # Compute the SHA-256 hash of the input bytes
    sha256_hash = hashlib.sha256(input_bytes).hexdigest()
    
    return sha256_hash

if __name__ == "__main__":
    # Get the input from the user
    input_data = input("Enter the data to hash: ")

    # Calculate the SHA-256 hash
    hashed_data = sha256_hash(input_data)

    print("SHA-256 Hash: ", hashed_data)
'''

import mysql.connector
import json
import hashlib

# Read sensitive information from a configuration file
with open("sqldatafile.json") as config_file:
    config = json.load(config_file)

host = config["DB_HOST"]
user = config["DB_USER"]
password = config["DB_PASSWORD"]
database = config["DB_DATABASE"]


# Step 1: Connect to the database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


input_user = input('Insert username:    ')
input_passcode = input('Insert passcode:    ')
input_passbytes = input_passcode.encode('utf-8')
hash_inputpass = hashlib.sha256(input_passbytes).hexdigest()
input_birthday = input('Insert birthday:    ')
input_description = input('Insert description:    ')
input_language = input('Insert language:     ')

cursor = conn.cursor()

# Sample data for the new row
filedat = 'fake/url'

# Execute the INSERT query
insert_query = "INSERT INTO users_basicdata (username, en_passcode, filedata, birthday, description, language) VALUES (%s, %s, %s, %s, %s, %s);"
data = (input_user, hash_inputpass, filedat, input_birthday, input_description, input_language)
cursor.execute(insert_query, data)

conn.commit()

# Step 6: Close the cursor and connection
cursor.close()
conn.close()
