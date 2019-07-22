import json


class PointsData:
    """Model class for Point data."""

    def __init__(self):
        self._latitude = 0.0
        self._longitude = 0.0
        self._zInd = 0.0

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def zIndex(self):
        return self._zInd

    def toJson(self):
        """Get JSON string from Point data."""
        return json.dumps({
            'latitude': self._latitude,
            'longitude': self._longitude,
            'zInd': self._longitude,
        })

    @classmethod
    def fromJson(cls, jsonString):
        """Get Point data from [jsonString]."""
        jsonDict = json.loads(jsonString)
        data = PointsData()
        if 'latitude' in jsonDict:
            data._latitude = jsonDict['latitude']
        if 'longitude' in jsonDict:
            data._longitude = jsonDict['longitude']
        if 'zInd' in jsonDict:
            data._zInd = jsonDict['zInd']
        return data
