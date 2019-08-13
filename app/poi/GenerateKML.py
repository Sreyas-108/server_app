import requests
import simplekml

from app.controller.FeedbackSender import FeedbackSender
from app.controller.ModuleType import ModuleType
from app.utils.DeployUtils import DeployUtils
from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


def generatePOI(data, ip):
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
        multipart_form_data = {'kml': (KMLUtils.getFilePath(), open(KMLUtils.getFilePath(), 'r'))}
        requests.post(DeployUtils.getURL(ip), files=multipart_form_data)
    except Exception as e:
        LogUtils.writeWarning("KML generation for POI failure : " + str(e))
        FeedbackSender.getInstance().sendMessage(ModuleType.GESTURE, "KML generation for POI failure.")
