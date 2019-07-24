import requests

from app.controller.FeedbackSender import FeedbackSender
from app.controller.ModuleType import ModuleType
from app.gdrive.FileRequests import FileRequests
from app.utils.DeployUtils import DeployUtils
from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


def generateTour(data, ip):
    """Generate KML file for tour [data]."""
    LogUtils.writeInfo("KML generation for tour.")
    try:
        fr = FileRequests.getInstance()
        if fr is not None:
            fr.downloadFile(data.fileID)
            multipart_form_data = {'kml': (KMLUtils.getFilePath(), open(KMLUtils.getFilePath(), 'r'))}
            requests.post(DeployUtils.getURL(ip), files=multipart_form_data)
            # os.startfile(KMLUtils.getFilePath())
        else:
            LogUtils.writeWarning("Authorization for drive access failure.")
    except Exception as e:
        LogUtils.writeWarning("KML generation for tour failure : " + str(e))
        FeedbackSender.getInstance().sendMessage(ModuleType.TOUR, "KML generation for tour failure.")
