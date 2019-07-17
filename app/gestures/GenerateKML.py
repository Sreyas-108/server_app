import os

import simplekml

from app.controller.FeedbackSender import FeedbackSender
from app.controller.ModuleType import ModuleType
from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


def generateGesture(data):
    """Generate KML file for Gesture [data]."""
    LogUtils.writeInfo("KML generation for Gesture.")
    try:
        kml = simplekml.Kml()
        pnt = kml.newpoint()
        pnt.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
        pnt.lookat.latitude = data.latitude
        pnt.lookat.longitude = data.longitude
        pnt.lookat.range = KMLUtils.convertZoomToRange(data.zoom)
        pnt.lookat.heading = data.bearing
        pnt.lookat.tilt = data.tilt
        kml.save(KMLUtils.getFilePath())
        os.startfile(KMLUtils.getFilePath())
    except Exception as e:
        LogUtils.writeWarning("KML generation for gesture failure : " + str(e))
        FeedbackSender.getInstance().sendMessage(ModuleType.GESTURE, "KML generation for gesture failure.")
