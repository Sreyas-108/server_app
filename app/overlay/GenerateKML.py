import requests
import simplekml

from app.controller.FeedbackSender import FeedbackSender
from app.controller.ModuleType import ModuleType
from app.models.OverlayItems import LineData
from app.models.OverlayItems import ImageData
from app.models.OverlayItems import PolygonData
from app.models.OverlayItems import PlacemarkData
from app.utils.DeployUtils import DeployUtils
from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


def generateOverlay(data, ip):
    """Generate KML file for Overlay [data]."""
    LogUtils.writeInfo("KML generation for Overlay.")
    try:
        kml = simplekml.Kml()
        for i in data.itemData:
            if isinstance(i, PlacemarkData):
                pnt = kml.newpoint(name=i.title, description=i.desc, coords=[(i.longitude, i.latitude, i.zIndex)])
                pnt.style.iconstyle.color = i.iconColor
                pnt.style.iconstyle.scale = i.iconSize
                pnt.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
                pnt.lookat.latitude = data.latitude
                pnt.lookat.longitude = data.longitude
                pnt.lookat.range = KMLUtils.convertZoomToRange(data.zoom)
                pnt.lookat.heading = data.bearing
                pnt.lookat.tilt = data.tilt
            elif isinstance(i, LineData):
                line = kml.newlinestring(name=i.title, description=i.desc,
                                         coords=[(i.points[0].longitude, i.points[0].latitude, i.points[0].zIndex),
                                                 (i.points[1].longitude, i.points[1].latitude, i.points[1].zIndex)])
                line.style.linestyle.color = i.color
                line.style.linestyle.width = i.width
                line.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
                line.lookat.latitude = data.latitude
                line.lookat.longitude = data.longitude
                line.lookat.range = KMLUtils.convertZoomToRange(data.zoom)
                line.lookat.heading = data.bearing
                line.lookat.tilt = data.tilt
            elif isinstance(i, PolygonData):
                poly = kml.newpolygon(name=i.title, description=i.desc)
                poly.style.linestyle.color = i.strokeColor
                poly.style.linestyle.width = i.width
                poly.style.polystyle.color = i.color
                boundary = []
                for j in i.points:
                    boundary.append((j.longitude, j.latitude, j.zIndex))
                poly.outerboundaryis = boundary
                poly.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
                poly.lookat.latitude = data.latitude
                poly.lookat.longitude = data.longitude
                poly.lookat.range = KMLUtils.convertZoomToRange(data.zoom)
                poly.lookat.heading = data.bearing
                poly.lookat.tilt = data.tilt
            elif isinstance(i, ImageData):
                photo = kml.newphotooverlay(name=i.title, description=i.desc)
                photo.point.coords = [(i.longitude, i.latitude, i.zIndex)]
                photo.style.iconstyle.icon.href = 'lg.png'
                photo.lookat.gxaltitudemode = simplekml.GxAltitudeMode.relativetoseafloor
                photo.lookat.latitude = data.latitude
                photo.lookat.longitude = data.longitude
                photo.lookat.range = KMLUtils.convertZoomToRange(data.zoom)
                photo.lookat.heading = data.bearing
                photo.lookat.tilt = data.tilt
                kml.addfile('lg.png')
        path = KMLUtils.getFilePath()
        kml.savekmz(path)
        multipart_form_data = {'kml': (path, open(path, 'r'))}
        requests.post(DeployUtils.getURL(ip), files=multipart_form_data)
    except Exception as e:
        LogUtils.writeWarning("KML generation for overlay failure : " + str(e))
        FeedbackSender.getInstance().sendMessage(ModuleType.GESTURE, "KML generation for overlay failure.")
