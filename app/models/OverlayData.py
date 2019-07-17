import json

from app.models.KMLData import KMLData
from app.models.OverlayItems import OverlayItem


class OverlayData(KMLData):
    """Model class for Overlay data."""

    def __init__(self):
        self._title = ""
        self._desc = ""
        self._latitude = 0.0
        self._longitude = 0.0
        self._bearing = 0.0
        self._zoom = 0.0
        self._tilt = 0.0
        self._itemData = []

    @property
    def itemData(self):
        return self._itemData

    def toJson(self):
        """Get JSON string from Overlay data."""
        return json.dumps({
            'title': self._title,
            'desc': self._desc,
            'latitude': self._latitude,
            'longitude': self._longitude,
            'bearing': self._bearing,
            'zoom': self._zoom,
            'tilt': self._tilt,
            'itemData': self._itemData,
        })

    @classmethod
    def fromJson(cls, jsonString):
        """Get Overlay data from [jsonString]."""
        jsonDict = json.loads(jsonString)
        data = OverlayData()
        if 'title' in jsonDict:
            data._title = jsonDict['title']
        if 'desc' in jsonDict:
            data._desc = jsonDict['desc']
        if 'latitude' in jsonDict:
            data._latitude = jsonDict['latitude']
        if 'longitude' in jsonDict:
            data._longitude = jsonDict['longitude']
        if 'bearing' in jsonDict:
            data._bearing = jsonDict['bearing']
        if 'zoom' in jsonDict:
            data._zoom = jsonDict['zoom']
        if 'tilt' in jsonDict:
            data._tilt = jsonDict['tilt']
        if 'itemData' in jsonDict:
            item = jsonDict['itemData']
            for i in item:
                data._itemData.append(OverlayItem.fromJson(i))
        return data
