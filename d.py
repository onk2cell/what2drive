# first import all required Module  ocrtogoogledrive
import io
from PIL import Image
import re
import os
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bardapi import Bard
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import upload
import uploadimg
import json

os.environ["_BARD_API_KEY"] = "Enter Your Own Bard API key"


def get_file_path(folder_name):
    """Gets the file path for the newly created image in the specified folder."""
    new_file = os.listdir(folder_name)[-1]
    file_path = os.path.join(folder_name, new_file)
    return file_path


class Drive_OCR:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.credentials = "./credentials.json"
        self.pickle = "token.pickle"

    def main(self) -> str:
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.pickle):
            with open(self.pickle, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.pickle, 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)

        # For Uploading Image into Drive

        mime = 'application/vnd.google-apps.document'
        file_metadata = {'name': self.filename, 'mimeType': mime}
        file = service.files().create(
            body=file_metadata,
            media_body=MediaFileUpload(self.filename, mimetype=mime)
        ).execute()
        print('File ID: %s' % file.get('id'))

        # It will export drive image into Doc
        request = service.files().export_media(fileId=file.get('id'), mimeType="text/plain")

        # For Downloading Doc Image data by request
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

        # It will delete file from drive base on ID
        service.files().delete(fileId=file.get('id')).execute()

        # It will print data into terminal
        output = fh.getvalue().decode()

        # Assuming the file name is passed as the first command-line argument

        return output


if __name__ == '__main__':
    # Rest of your Python script to process the image
    folder_name = "C:\\Users\\onkar\\Desktop\\New folder\\upload"
    file_path = get_file_path(folder_name)
    print(f"The file path is: {file_path}")
    ob = Drive_OCR(file_path)
    image = Image.open(file_path)
    lo = str(ob.main())
    print(lo)
    message = f"{lo} hey can you please give me some suggestions for naming this txt to a txt   .txt from it and use underscore to join the txt and Please provide a in depth deatiled view of the key insights, important details, and valuable information contained in the text data and provide in a very deep and detailded info of txet "
    print(message)
    k = (Bard().get_answer(str(message)))
    print(k)
    la = str(k)
    txt_files = re.findall(r"([\w.-]+\.txt)", la)
    print(txt_files)
    output_path = f"{txt_files[1]}.jpg"
    output_name = f"{txt_files[1]}.jpg"
    image.save(output_path)
    img = uploadimg.Drive_OCI(output_name)
    file_id = img.main()
    print(file_id)
    p = output_name
    b = upload.Drive_OC(p)
    s = k['content'] + str(txt_files)
    print(b.main(s))

    print(f"Your file has been uploaded on gogole drive by {output_name}")
    print(k)
