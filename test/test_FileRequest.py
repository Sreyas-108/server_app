import unittest
from pathlib import Path
from unittest.mock import patch
from unittest.mock import Mock
from googleapiclient.http import HttpRequest
from googleapiclient.http import MediaIoBaseDownload
from app.gdrive.FileRequests import FileRequests
from app.utils.KMLUtils import KMLUtils


class FileRequestTest(unittest.TestCase):
    """Tests for Google Drive functionalities."""

    @patch('app.gdrive.FileRequests.ServiceAccountCredentials')
    @patch('app.gdrive.FileRequests.build')
    @patch('app.gdrive.FileRequests.MediaIoBaseDownload')
    def test_authorizeUserAndDownload(self, mock_downloader, mock_builder, mock_serviceAcc):
        mock_serviceAcc.from_json_keyfile_name.return_value = 0

        fr = FileRequests.getInstance()
        mock_serviceAcc.from_json_keyfile_name.assert_called_once()
        mock_builder.assert_called_once()
        mock_builder.assert_called_once_with('drive', 'v3', credentials=0)

        mock_builder.return_value.files.return_value.get_media.return_value = 0
        mock_downloader.return_value.next_chunk.return_value = True

        fr.downloadFile('fileID')
        mock_builder.return_value.files.return_value.get_media.assert_called_once()
        mock_downloader.return_value.next_chunk.assert_called_once_with()
        self.assertEqual(Path(KMLUtils.getFilePath()).exists(), True)
