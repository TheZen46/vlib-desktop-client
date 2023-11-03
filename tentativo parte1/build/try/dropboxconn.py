import dropbox
import os
import dropbox.files

'''with open('token.txt', 'r') as f:
    TOKEN = f.read()

dbx = dropbox.Dropbox(TOKEN)


def upload():
    with open('res_image.png', 'rb') as f:
        data= f.read()
        dbx.files_upload(data, f'/res_image.png')

upload()'''

#I HAVE TO OBTAIN THE TOKEN --->  IT IS ONLY FOR TESTING
class DropConn():
    def __init__(self, image_transfer=None, user=None):    
        self.image_transfer= image_transfer
        self.user= user

        with open('token.txt', 'r') as f:
            TOKEN= f.read()

        self.dbx= dropbox.Dropbox(TOKEN)

    def upload_image(self):
        with open(self.image_transfer, 'rb') as f:
            data= f.read()
            self.dbx.files_upload(data, f'/{self.user}_image.png')
            self.dbx.close()

    def download_image(self):
        for entry in self.dbx.files_list_folder('').entries:
            self.dbx.files_download_to_file(os.path.join('local_temp_files', entry.name), f'/{entry.name}')
            self.dbx.close()
    
    def downlaod_onlyimage(self, name_file=None):
        local_file_path= 'local_downloaded_image.png'
        dropbox_file_path= f'/{name_file}.png'

        with open(local_file_path, 'wb') as local_file:
            metadata, res = self.dbx.files_download(dropbox_file_path)
            local_file.write(res.content)
        
        self.dbx.close()