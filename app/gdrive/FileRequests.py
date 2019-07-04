import io
import os
from pathlib import Path

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials
from app.utils.KMLUtils import KMLUtils

from app.controller.ModuleType import ModuleType
from app.controller.OSCSender import OSCSender
from app.utils.LogUtils import LogUtils
from config.Config import Config


class FileRequests:
    """Google Drive functionalities required for the app."""

    service = None

    __instance = None

    @staticmethod
    def getInstance():
        """Get the singleton instance of [FileRequests]."""
        if FileRequests.__instance is None:
            FileRequests()
        return FileRequests.__instance

    def __init__(self):
        if FileRequests.__instance is not None:
            raise Exception("This class is a singleton.")
        else:
            self.service = self.authorizeUser()
            if self.service is None:
                FileRequests.__instance = None
            else:
                FileRequests.__instance = self

    def authorizeUser(self):
        """Authorize user for the service account."""
        try:
            fileName = Path(os.path.abspath(
                os.path.join(os.path.abspath(os.pardir), Config.GOOGLE_DRIVE_CREDENTIALS)))
            credentials = ServiceAccountCredentials.from_json_keyfile_name(fileName,
                                                                           scopes='https://www.googleapis.com/auth/drive')

            service = build('drive', 'v3', credentials=credentials)
            return service
        except Exception as e:
            LogUtils.writeWarning("Google Drive authorization failure : " + str(e))
            return None

    def downloadFile(self, fileID):
        """Download file from Google Drive for [fileID]."""
        try:
            request = self.service.files().get_media(fileId=fileID)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                done = downloader.next_chunk()
            fileName = KMLUtils.getFilePath()
            kmlfile = open(fileName, 'w+')
            kmlfile.write(fh.getvalue().decode("utf-8"))
            return True
        except Exception as e:
            print(str(e))
            LogUtils.writeWarning("Google Drive file download failure : " + str(e))
            OSCSender.getInstance().sendMessage(ModuleType.TOUR, "File download failure for tour.")
            return False

    def getAllFiles(self):
        """Print all the files accessible by the service account."""
        try:
            results = self.service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])

            if not items:
                print('No files found.')
            else:
                print('Files:')
                for item in items:
                    print(u'{0} ({1})'.format(item['name'], item['id']))
        except Exception as e:
            LogUtils.writeWarning("Get files from Google Drive failure : " + str(e))
