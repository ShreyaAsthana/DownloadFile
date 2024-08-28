import os
import sys
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Define scopes
SCOPES = ['https://www.googleapis.com/auth/drive']
export_mime_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'


def authenticate():
    """Authenticate the user and return a Google Drive API service instance."""
    creds = None
    # Path to the service account credentials file
    SERVICE_ACCOUNT_FILE = '/Users/s0a0hk9/PycharmProjects/DownloadFile/.venv/client_secret.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    return build('drive', 'v3', credentials=creds)


def download_file(service, file_id, output_folder):
    """Download a file from Google Drive given a file ID."""
    try:
        request = service.files().export_media(fileId=file_id, mimeType=export_mime_type)
        fh = io.FileIO(os.path.join(output_folder, file_id), 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")
        print(f"Downloaded file with ID {file_id} to {output_folder}")
    except Exception as e:
        print(f"Failed to download file: {str(e)}")


def main(file_id, output_folder):
    if not os.path.exists(output_folder):
        print(f"Output folder {output_folder} does not exist.")
        sys.exit(1)

    service = authenticate()
    download_file(service, file_id, output_folder)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download_drive_file.py <file_id> <output_folder>")
        sys.exit(1)

    file_id = sys.argv[1]
    output_folder = sys.argv[2]
    main(file_id, output_folder)
