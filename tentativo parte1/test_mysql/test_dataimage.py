import dropbox

# Your app key and secret obtained from the Dropbox Developer website
app_key = 'z7rzx6tolakj23b'
app_secret = 'hv9zz9zgkavjpv3'

# Create a Dropbox object and authenticate
flow = dropbox.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start()
print("1. Go to: " + authorize_url)
print("2. Click 'Allow' (you might have to log in first)")
print("3. Copy the authorization code.")

auth_code = input("Enter the authorization code here: ")

access_token, user_id = flow.finish(auth_code)

# Create a Dropbox client
dbx = dropbox.Dropbox(access_token)

# Upload a file to Dropbox
with open("las_purgas.png", "rb") as f:
    dbx.files_upload(f.read(), "/try1.png")

print("File uploaded to Dropbox.")
