import os

import simplekml

from app.controller.FeedbackSender import FeedbackSender
from app.controller.ModuleType import ModuleType
from app.flyto.FlyToOptions import FlyToOptions
from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


def generateFlyTo(data):
    """Generate KML file for fly to [data]."""
    LogUtils.writeInfo("KML generation for Fly To.")
    try:
        flyto = FlyToOptions(data.lower())
    except Exception as e:
        LogUtils.writeWarning("Wrong target location for Fly To received : " + str(e))
        FeedbackSender.getInstance().sendMessage(ModuleType.FLYTO, "Wrong target location for Fly To received.")
        return
    try:
        kml = simplekml.Kml()
        kml.hint = 'target=' + flyto.value
        kml.save(KMLUtils.getFilePath())
        os.startfile(KMLUtils.getFilePath())
    except Exception as e:
        LogUtils.writeWarning("KML generation for fly to failure : " + str(e))
        FeedbackSender.getInstance().sendMessage(ModuleType.GESTURE, "KML generation for fly to failure.")
