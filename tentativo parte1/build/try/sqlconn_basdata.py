import mysql.connector
import json
import hashlib

class Mycon_basdata():
    def __init__(self, username= None, password=None, birthday=None, filedat= None,description= None, email= None, language= None):
        with open("sqldatafile.json") as config_file:
            config = json.load(config_file)
        
        self.host = config['DB_HOST']
        self.user = config["DB_USER"]
        self.passcode = config["DB_PASSWORD"]
        self.database = config["DB_DATABASE"]
        self.username= username
        self.password= password
        self.birthday = birthday
        self.language= language
        self.description= description
        self.filedat= filedat
        self.email= email

        self.conn = mysql.connector.connect(
            host= self.host,
            user= self.user,
            password= self.passcode,
            database= self.database
        )

        self.cursor= self.conn.cursor()


    def find_and_verify(self):
        self.cursor.execute('SELECT username, en_passcode FROM Vlib;')
        self.result = self.cursor.fetchall()
        
        for row in self.result:
            username= row[0]
            if username == self.username:
                en_pass= row[1]
                if en_pass == hashlib.sha256(self.password.encode('utf-8')).hexdigest():
                    return True
                else:
                    return False
            else:
                return False

    def find_and_verify_noenc(self):
        self.cursor.execute('SELECT username, en_passcode FROM Vlib;')
        self.result = self.cursor.fetchall()
        print('give am 1')
        for row in self.result:
            username= row[0]
            print('no competion')
            print(f'verifing if {username} == to self.{self.username}')
            if username == self.username:
                en_pass= row[1]
                print('search')
                if en_pass == self.password:
                    print('stole drug')
                    return True


    def get_imagepath(self):
        self.cursor.execute('SELECT username, filedata FROM Vlib;')
        self.result = self.cursor.fetchall()
        
        for row in self.result:
            username= row[0]
            if username== self.username:
                image_path= row[1]
                return image_path
        return None

    def find_and_verify_name(self):
        self.cursor.execute('SELECT username FROM Vlib;')
        self.result = self.cursor.fetchall()
        
        votes = True

        for row in self.result:
            username= row[0]
            if username == self.username:
                votes = False

        return votes



    def write_and_modify(self):
        insert_query= 'INSERT INTO Vlib (username, en_passcode, filedata, birthday, description, email, language) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        encoded_pass= self.password.encode('utf-8')
        self.password_EN = hashlib.sha256(encoded_pass).hexdigest()
        data= (self.username, self.password_EN, self.filedat, self.birthday, self.description, self.email, self.language)
        self.cursor.execute(insert_query, data)
        self.conn.commit()
        

    def close_all(self):
        self.cursor.close()
        self.conn.close()