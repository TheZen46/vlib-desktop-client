'''import mysql.connector
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

# Step 2: Create a cursor
cursor = conn.cursor()

name_list = []

input_user = input('Insert username:    ')
input_passcode = input('Insert passcode:    ')
input_passbytes = input_passcode.encode('utf-8')
hash_inputpass = hashlib.sha256(input_passbytes).hexdigest()

# Step 3: Execute the query
cursor.execute("SELECT username, en_passcode, description FROM users_basicdata;")

# Step 4: Fetch data
result = cursor.fetchall()

# Step 5: Process the data
for row in result:
    username = row[0]
    passcode = row[1]
    description = row[2]

    if username == input_user:
        print('username found')

        if passcode == hash_inputpass:
            print('YOU SHALL PASS')

# Step 6: Close the cursor and connection
cursor.close()
conn.close()'''
'''from PIL import Image
import PIL
import aggdraw


def round_corner_jpg(image, radius):
    """generate round corner for image"""
    mask = Image.new('L', image.size) # filled with black by default
    draw = aggdraw.Draw(mask)
    brush = aggdraw.Brush('white')
    width, height = mask.size
    #upper-left corner
    draw.pieslice((0,0,radius*2, radius*2), 90, 180, None, brush)
    #upper-right corner
    draw.pieslice((width - radius*2, 0, width, radius*2), 0, 90, None, brush)
    #bottom-left corner
    draw.pieslice((0, height - radius * 2, radius*2, height),180, 270, None, brush)
    #bottom-right corner
    draw.pieslice((width - radius * 2, height - radius * 2, width, height), 270, 360, None, brush)
    #center rectangle
    draw.rectangle((radius, radius, width - radius, height - radius), brush)
    #four edge rectangle
    draw.rectangle((radius, 0, width - radius, radius), brush)
    draw.rectangle((0, radius, radius, height-radius), brush)
    draw.rectangle((radius, height-radius, width-radius, height), brush)
    draw.rectangle((width-radius, radius, width, height-radius), brush)
    draw.flush()
    image = image.convert('RGBA')
    image.putalpha(mask)
    return image

im = Image.open('2Q.png')
print('hi')
im= round_corner_jpg(im, 18)
print('helo')
im.save('2Q.png')
print('bye')'''

import json

# Function to read data from the file and load it into a dictionary
def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}  # If the file doesn't exist, start with an empty dictionary
    return data

# Function to write data from a dictionary to the file
def write_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Main function to interact with the data
def main():
    filename = "Onl_verification.json"
    data = read_data(filename)

    while True:
        print("1. Add an activity, user, and password")
        print("2. View all data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            activity = input("Enter the activity (Active, Name, Ghost): ")
            user = input("Enter the username: ")
            password = input("Enter the password: ")
            data = {"user": user, "pass": password, 'activity': activity}
            write_data(filename, data)
            print("Data saved successfully!")

        elif choice == '2':
            print(json.dumps(data, indent=4))

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
