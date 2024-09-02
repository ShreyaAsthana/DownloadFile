# Google Drive File Downloader in Python

This repository contains a Python script for downloading files from Google Drive using the `gdown` library.

## Prerequisites

Ensure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Step 1: Install Required Packages

pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

##  Step 2: Ensure You Have the Correct Service Account JSON File
Generate a New Service Account Key File:

1. Go to the Google Cloud Console.
2. Navigate to IAM & Admin > Service Accounts.
3. Select the project where you want to create the service account.
4. Click Create Service Account.
5. Enter a name for the service account and optionally a description.
6. Click Create.
7. Assign appropriate roles (e.g., Project > Editor, or more specific roles as needed).
8. Click Continue.
9. Click Done.
10. Create a Key for the Service Account:

11. Click on the service account you just created.
12. Go to the Keys tab.
13. Click Add Key > Create New Key.
14. Choose JSON as the key type.
15. Click Create.
16. Save the downloaded JSON key file securely. This file should contain the necessary fields (client_email, token_uri, etc.).
17. Placce .json file in your work repo

### Step 3: Update TestDownload.py
Update "SERVICE_ACCOUNT_FILE" with downloaded .json file path

### Step 4: Find File ID
Example: https://drive.google.com/file/d/1abcDxyz/view?usp=sharing
Here, the file ID is 1abcDxyz.

### Step 5: Execute Code using command line
 python3 .venv/TestDownload.py <file_id> <output_folder>
python3 .venv/TestDownload.py --file_id <"file_id"> --output_folder <output_folder_path> --service_account_file_path <service_account_file_path>


