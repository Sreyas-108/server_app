class DeployUtils:
    """Utilities for KML deployment."""

    @staticmethod
    def getURL(ip):
        """Get the default url for deploying KML files."""
        return "http://" + ip + ":8080/kml/manage/upload"
