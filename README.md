# Google Drive File Downloader in Python

This repository contains a Python script for downloading files from Google Drive using the `gdown` library.

## Prerequisites

Ensure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Step 1: Install Required Packages

pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

##  Step 2: Ensure You Have the Correct Service Account JSON File
Generate a New Service Account Key File:

Go to the Google Cloud Console.
Navigate to IAM & Admin > Service Accounts.
Select the project where you want to create the service account.
Click Create Service Account.
Enter a name for the service account and optionally a description.
Click Create.
Assign appropriate roles (e.g., Project > Editor, or more specific roles as needed).
Click Continue.
Click Done.
Create a Key for the Service Account:

Click on the service account you just created.
Go to the Keys tab.
Click Add Key > Create New Key.
Choose JSON as the key type.
Click Create.
Save the downloaded JSON key file securely. This file should contain the necessary fields (client_email, token_uri, etc.).
Placce .json file in your work repo

### Step 3: Update TestDownload.py
Update "SERVICE_ACCOUNT_FILE" with downloaded .json file path

### Step 4: Find File ID
Example: https://drive.google.com/file/d/1abcDxyz/view?usp=sharing
Here, the file ID is 1abcDxyz.

### Step 5: Execute Code
 python3 .venv/TestDownload.py <file_id> <output_folder>


