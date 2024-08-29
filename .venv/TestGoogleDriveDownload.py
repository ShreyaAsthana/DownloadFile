import unittest
from unittest.mock import patch, MagicMock
import os
import io
import sys
from TestDownload import authenticate, download_file, main

class TestGoogleDriveDownload(unittest.TestCase):

    @patch('TestDownload.service_account.Credentials.from_service_account_file')
    @patch('TestDownload.build')
    def test_authenticate_success(self, mock_build, mock_credentials):
        """Test successful authentication."""
        mock_credentials.return_value = MagicMock()
        mock_build.return_value = MagicMock()

        service = authenticate()

        mock_credentials.assert_called_once_with(
            '/Users/s0a0hk9/PycharmProjects/DownloadFile/.venv/client_secret.json',
            scopes=['https://www.googleapis.com/auth/drive']
        )
        mock_build.assert_called_once_with('drive', 'v3', credentials=mock_credentials.return_value)
        self.assertIsNotNone(service)

    @patch('TestDownload.service_account.Credentials.from_service_account_file')
    def test_authenticate_failure(self, mock_credentials):
        """Test authentication failure due to missing credentials file."""
        mock_credentials.side_effect = Exception("Credentials file not found.")

        with self.assertRaises(Exception) as context:
            authenticate()
        self.assertTrue("Credentials file not found." in str(context.exception))

    @patch('TestDownload.MediaIoBaseDownload.next_chunk')
    @patch('TestDownload.service.files')
    @patch('TestDownload.io.FileIO')
    def test_download_file_success(self, mock_file_io, mock_files, mock_next_chunk):
        """Test successful file download."""
        mock_request = MagicMock()
        mock_files.return_value.export_media.return_value = mock_request
        mock_file_io.return_value = MagicMock()
        mock_next_chunk.side_effect = [(MagicMock(progress=0.5), False), (MagicMock(progress=1.0), True)]

        service = MagicMock()
        file_id = "fake_file_id"
        output_folder = "test_folder"
        os.makedirs(output_folder, exist_ok=True)

        download_file(service, file_id, output_folder)

        mock_files.return_value.export_media.assert_called_once_with(
            fileId=file_id, mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        mock_file_io.assert_called_once_with(os.path.join(output_folder, file_id), 'wb')
        self.assertEqual(mock_next_chunk.call_count, 2)

        # Cleanup
        os.rmdir(output_folder)

    @patch('TestDownload.io.FileIO')
    def test_download_file_failure(self, mock_file_io):
        """Test file download failure due to API error."""
        mock_file_io.side_effect = Exception("API Error")

        service = MagicMock()
        file_id = "invalid_file_id"
        output_folder = "test_folder"
        os.makedirs(output_folder, exist_ok=True)

        with self.assertLogs(level='INFO') as log:
            download_file(service, file_id, output_folder)
            self.assertIn("Failed to download file", log.output[0])

        # Cleanup
        os.rmdir(output_folder)

    @patch('TestDownload.authenticate')
    @patch('TestDownload.download_file')
    @patch('TestDownload.os.path.exists')
    def test_main_success(self, mock_exists, mock_download_file, mock_authenticate):
        """Test main function with correct arguments."""
        mock_exists.return_value = True
        mock_authenticate.return_value = MagicMock()

        file_id = "fake_file_id"
        output_folder = "test_folder"

        main(file_id, output_folder)

        mock_exists.assert_called_once_with(output_folder)
        mock_authenticate.assert_called_once()
        mock_download_file.assert_called_once_with(mock_authenticate.return_value, file_id, output_folder)

    @patch('TestDownload.authenticate')
    @patch('TestDownload.download_file')
    @patch('TestDownload.os.path.exists')
    def test_main_no_output_folder(self, mock_exists, mock_download_file, mock_authenticate):
        """Test main function when output folder does not exist."""
        mock_exists.return_value = False
        mock_authenticate.return_value = MagicMock()

        file_id = "fake_file_id"
        output_folder = "fake_folder"

        with self.assertRaises(SystemExit):
            main(file_id, output_folder)

        mock_exists.assert_called_once_with(output_folder)
        mock_authenticate.assert_not_called()
        mock_download_file.assert_not_called()

    def test_main_invalid_arguments(self):
        """Test main function with invalid command line arguments."""
        with patch.object(sys, 'argv', ["TestDownload.py", "only_one_arg"]):
            with self.assertRaises(SystemExit):
                import TestDownload

    def test_non_docx_file_format(self):
        """Test by downloading any non docx file from google drive"""

    def test_downloading_valid_file_by_putting_network_issue(self):
        """Test by downloading any valid file by breaking network(internet connectivity) in between"""

    def test_download_file_which_does_not_exists_in_drive(self):
        """Test by downloading file which does not exists in google drive"""





if __name__ == '__main__':
    unittest.main()
