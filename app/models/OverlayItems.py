import json
from abc import ABC, abstractmethod
from app.models.PointsData import PointsData

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
        elif jsonString['type'] == ('Line'):
            return LineData.fromJson(json.dumps(jsonString))
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
    def zIndex(self):
        return self._zInd

    @property
    def iconSize(self):
        return self._iconSize

    @property
    def iconColor(self):
        return self._iconColor

    def toJson(self):
        """Get JSON string from Placemark data."""
        return json.dumps({
            'id': self._id,
            'point': self._latitude,
            'title': self._title,
            'desc': self._desc,
            'iconSize': self._iconSize,
            'iconColor': self._iconColor,
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


class LineData(OverlayItem):
    """Model class for Line data."""

    def __init__(self):
        self._id = ""
        self._points = []
        self._title = ""
        self._desc = ""
        self._width = 0
        self._color = 0.0

    @property
    def points(self):
        return self._points

    @property
    def width(self):
        return self._width

    @property
    def color(self):
        return self._color

    def toJson(self):
        """Get JSON string from Placemark data."""
        return json.dumps({
            'id': self._id,
            'points': self._points,
            'title': self._title,
            'desc': self._desc,
            'width': self._width,
            'color': self._color,
        })

    @classmethod
    def fromJson(cls, jsonString):
        """Get Placemark data from [jsonString]."""
        jsonDict = json.loads(jsonString)
        data = LineData()
        if 'id' in jsonDict:
            data._id = jsonDict['id']
        if 'points' in jsonDict:
            point = jsonDict['points']
            for i in point:
                data._points.append(PointsData.fromJson(json.dumps(i)))
        if 'title' in jsonDict:
            data._title = jsonDict['title']
        if 'desc' in jsonDict:
            data._desc = jsonDict['desc']
        if 'width' in jsonDict:
            data._width = jsonDict['width']
        if 'color' in jsonDict:
            data._color = jsonDict['color']
        return data
