import os

from app.controller.ModuleType import ModuleType
from app.controller.OSCSender import OSCSender
from app.gdrive.FileRequests import FileRequests
from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


def generateTour(data):
    """Generate KML file for tour [data]."""
    LogUtils.writeInfo("KML generation for tour.")
    try:
        fr = FileRequests.getInstance()
        if fr is not None:
            fr.downloadFile(data.fileID)
            os.startfile(KMLUtils.getFilePath())
        else:
            LogUtils.writeWarning("Authorization for drive access failure.")
    except Exception as e:
        LogUtils.writeWarning("KML generation for tour failure : " + str(e))
        OSCSender.getInstance().sendMessage(ModuleType.TOUR, "KML generation for tour failure.")
