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
        elif jsonString['type'] == ('Polygon'):
            return PolygonData.fromJson(json.dumps(jsonString))
        elif jsonString['type'] == ('Image'):
            return ImageData.fromJson(json.dumps(jsonString))
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
    def title(self):
        return self._title

    @property
    def desc(self):
        return self._desc

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
            color = '00000000'
            if jsonDict['iconColor'] == 0:
                color = 'FF0000FF'
            elif jsonDict['iconColor'] == 120:
                color = 'FF00FF00'
            elif jsonDict['iconColor'] == 240:
                color = 'FFFF0000'
            data._iconColor = color
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
    def title(self):
        return self._title

    @property
    def desc(self):
        return self._desc

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
        """Get JSON string from Line data."""
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
        """Get Line data from [jsonString]."""
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
            color_argb = hex(jsonDict['color'])[2:]
            data._color = color_argb[0:2] + color_argb[6:8] + color_argb[4:6] + color_argb[2:4]
        return data


class PolygonData(OverlayItem):
    """Model class for Polygon data."""

    def __init__(self):
        self._id = ""
        self._points = []
        self._title = ""
        self._desc = ""
        self._width = 0
        self._color = 0.0
        self._strokeColor = 0.0

    @property
    def title(self):
        return self._title

    @property
    def desc(self):
        return self._desc

    @property
    def points(self):
        return self._points

    @property
    def width(self):
        return self._width

    @property
    def color(self):
        return self._color

    @property
    def strokeColor(self):
        return self._strokeColor

    def toJson(self):
        """Get JSON string from Polygon data."""
        return json.dumps({
            'id': self._id,
            'points': self._points,
            'title': self._title,
            'desc': self._desc,
            'width': self._width,
            'color': self._color,
            'strokeColor': self._strokeColor,
        })

    @classmethod
    def fromJson(cls, jsonString):
        """Get Polygon data from [jsonString]."""
        jsonDict = json.loads(jsonString)
        data = PolygonData()
        if 'id' in jsonDict:
            data._id = jsonDict['id']
        if 'points' in jsonDict:
            point = jsonDict['points']
            for i in point:
                data._points.append(PointsData.fromJson(json.dumps(i)))
            data._points.append(PointsData.fromJson(json.dumps(point[0])))
        if 'title' in jsonDict:
            data._title = jsonDict['title']
        if 'desc' in jsonDict:
            data._desc = jsonDict['desc']
        if 'width' in jsonDict:
            data._width = jsonDict['width']
        if 'color' in jsonDict:
            color_argb = hex(jsonDict['color'])[2:]
            data._color = color_argb[0:2] + color_argb[6:8] + color_argb[4:6] + color_argb[2:4]
        if 'strokeColor' in jsonDict:
            color_argb = hex(jsonDict['strokeColor'])[2:]
            data._strokeColor = color_argb[0:2] + color_argb[6:8] + color_argb[4:6] + color_argb[2:4]
        return data


class ImageData(OverlayItem):
    """Model class for Image data."""

    def __init__(self):
        self._id = ""
        self._latitude = 0.0
        self._longitude = 0.0
        self._zInd = 0.0
        self._title = ""
        self._desc = ""
        self._image = 0
        self._thumbnail = 0.0

    @property
    def title(self):
        return self._title

    @property
    def desc(self):
        return self._desc

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
    def image(self):
        return self._image

    @property
    def thumbnail(self):
        return self._thumbnail

    def toJson(self):
        """Get JSON string from Image data."""
        return json.dumps({
            'id': self._id,
            'point': self._latitude,
            'title': self._title,
            'desc': self._desc,
            'image': self._image,
            'thumbnail': self._thumbnail,
        })

    @classmethod
    def fromJson(cls, jsonString):
        """Get Image data from [jsonString]."""
        jsonDict = json.loads(jsonString)
        data = ImageData()
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
        if 'image' in jsonDict:
            data._image = jsonDict['image']
        if 'thumbnail' in jsonDict:
            data._thumbnail = jsonDict['thumbnail']
        return data
