import json


class KMLData:
    """Model class for KML data."""

    def __init__(self):
        self._title = ""
        self._desc = ""
        self._latitude = 0.0
        self._longitude = 0.0
        self._bearing = 0.0
        self._zoom = 0.0
        self._tilt = 0.0

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._desc

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def bearing(self):
        return self._bearing

    @property
    def zoom(self):
        return self._zoom

    @property
    def tilt(self):
        return self._tilt

    def toJson(self):
        """Get JSON string from KML data."""
        return json.dumps({
            'title': self._title,
            'desc': self._desc,
            'latitude': self._latitude,
            'longitude': self._longitude,
            'bearing': self._bearing,
            'zoom': self._zoom,
            'tilt': self._tilt,
        })

    @classmethod
    def fromJson(cls, jsonString):
        """Get KML data from [jsonString]."""
        jsonDict = json.loads(jsonString)
        data = KMLData()
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
        return data
