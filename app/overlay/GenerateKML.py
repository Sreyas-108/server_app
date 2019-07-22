import os

import simplekml

from app.controller.FeedbackSender import FeedbackSender
from app.controller.ModuleType import ModuleType
from app.models.OverlayItems import PlacemarkData
from app.models.OverlayItems import LineData
from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


def generateOverlay(data):
    """Generate KML file for Overlay [data]."""
    LogUtils.writeInfo("KML generation for Overlay.")
    try:
        kml = simplekml.Kml()
        for i in data.itemData:
            if isinstance(i, PlacemarkData):
                pnt = kml.newpoint(name="Default", description="Def", coords=[(i.longitude, i.latitude)])
                pnt.style.iconstyle.color = i.iconColor
                pnt.style.iconstyle.scale = i.iconSize
                pnt.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
                pnt.lookat.latitude = data.latitude
                pnt.lookat.longitude = data.longitude
                pnt.lookat.range = KMLUtils.convertZoomToRange(data.zoom)
                pnt.lookat.heading = data.bearing
                pnt.lookat.tilt = data.tilt
            elif isinstance(i, LineData):
                line = kml.newlinestring(name="Default2", description="Def2",
                                        coords=[(i.points[0].longitude, i.points[0].latitude), (i.points[1].longitude, i.points[1].latitude)])
                line.style.linestyle.color = i.color
                line.style.linestyle.width = i.width
        kml.save(KMLUtils.getFilePath())
        os.startfile(KMLUtils.getFilePath())
    except Exception as e:
        LogUtils.writeWarning("KML generation for overlay failure : " + str(e))
        FeedbackSender.getInstance().sendMessage(ModuleType.GESTURE, "KML generation for overlay failure.")
