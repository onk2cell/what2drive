import io
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


#class for uploading image in the google drive
class Drive_OCI:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.credentials = "./credentials.json"
        self.pickle = "token.pickle"

    def main(self) -> str:
        floder = "12UAmlWFiLxIsaiWga_Zgj4hIPp5DVbgb"
        creds = None
        if os.path.exists(self.pickle):
            with open(self.pickle, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(self.pickle, 'wb') as token:
                pickle.dump(creds, token)

        drive_service = build('drive', 'v3', credentials=creds)

        mime = 'image/jpeg'
        file_metadata = {'name': self.filename,
                         'mimeType': mime,
                         "parents": [floder], }
        file = drive_service.files().create(
            body=file_metadata,
            media_body=MediaFileUpload(self.filename, mimetype=mime)
        ).execute()
        print('File ID: %s' % file.get('id'))

        return file.get('id')


if __name__ == '__main__':
    filename = "jpg.jpg"
    img = Drive_OCI(filename)
    file_id = img.main()
    print(file_id)
