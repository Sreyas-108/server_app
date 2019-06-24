import os

import simplekml

from app.controller.ModuleType import ModuleType
from app.controller.OSCSender import OSCSender
from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


def generatePOI(data):
    """Generate KML file for POI [data]."""
    LogUtils.writeInfo("KML generation for POI.")
    try:
        kml = simplekml.Kml()
        pnt = kml.newpoint(name=data.title, description=data.description, coords=[(data.longitude, data.latitude)])
        pnt.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
        pnt.lookat.latitude = data.latitude
        pnt.lookat.longitude = data.longitude
        pnt.lookat.range = KMLUtils.convertZoomToRange(data.zoom)
        pnt.lookat.heading = data.bearing
        pnt.lookat.tilt = data.tilt
        kml.save(KMLUtils.getFilePath())
        os.startfile(KMLUtils.getFilePath())
    except Exception as e:
        LogUtils.writeWarning("KML generation for POI failure : " + str(e))
        OSCSender.getInstance().sendMessage(ModuleType.GESTURE, "KML generation for POI failure.")
