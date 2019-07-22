import json
from abc import ABC, abstractmethod


class OverlayItem(ABC):
    """Model class for Overlay items."""

    @abstractmethod
    def toJson(self):
        """Get JSON string from Overlay item."""
        pass

    @classmethod
    def fromJson(cls, jsonString):
        """Get Overlay items from [jsonString]."""
        if jsonString['type'] == ('Placemark'):
            return PlacemarkData.fromJson(json.dumps(jsonString))
        return None


class PlacemarkData(OverlayItem):
    """Model class for Placemark data."""

    def __init__(self):
        self._id = ""
        self._latitude = 0.0
        self._longitude = 0.0
        self._zInd = 0.0
        self._title = ""
        self._desc = ""
        self._iconSize = 0
        self._iconColor = 0.0

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def iconSize(self):
        return self._iconSize

    def toJson(self):
        """Get JSON string from Placemark data."""
        return json.dumps({
            'id': self._id,
            'type': 'Placemark',
            'latitude': self._latitude,
            'longitude': self._longitude,
        })

    @classmethod
    def fromJson(cls, jsonString):
        """Get Placemark data from [jsonString]."""
        jsonDict = json.loads(jsonString)
        data = PlacemarkData()
        if 'id' in jsonDict:
            data._id = jsonDict['id']
        if 'point' in jsonDict:
            point = jsonDict['point']
            jsonPoint = json.loads(json.dumps(point))
            data._latitude = jsonPoint['latitude']
            data._longitude = jsonPoint['longitude']
            data._zInd = jsonPoint['zInd']
        if 'title' in jsonDict:
            data._title = jsonDict['title']
        if 'desc' in jsonDict:
            data._desc = jsonDict['desc']
        if 'iconSize' in jsonDict:
            data._iconSize = jsonDict['iconSize']
        if 'iconColor' in jsonDict:
            data._iconColor = jsonDict['iconColor']
        return data
