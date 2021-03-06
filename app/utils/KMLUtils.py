import random
import string


class KMLUtils:
    """Utilities for KML processing."""

    @staticmethod
    def convertZoomToRange(zoom):
        """Converts zoom data obtained from Google map to Range value for KMl file."""
        qrange = 35200000 / (2 ** zoom)
        if qrange < 300:
            return 300
        return qrange

    @staticmethod
    def getFilePath():
        """Get the default path of storing KML files."""
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(12)) + ".kml"
