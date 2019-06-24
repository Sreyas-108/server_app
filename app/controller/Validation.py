import socket


class ServerValidation:
    """Validation and server data."""

    __instance = None

    @staticmethod
    def getInstance():
        """Get the singleton instance of [ServerValidation]."""
        if ServerValidation.__instance is None:
            ServerValidation()
        return ServerValidation.__instance

    def __init__(self):
        if ServerValidation.__instance is not None:
            raise Exception("This class is a singleton.")
        else:
            ServerValidation.__instance = self
        self._id_lg = 12345
        self._basePath = "/lgcontroller"
        self._ipaddress = self._getIPAddress()
        self._port = self._getPort()

    def validateID(self, id_lg):
        """Validate ID parameter of the incoming OSC message."""
        return self._id_lg == id_lg

    @property
    def id_lg(self):
        return self._id_lg

    @property
    def basePath(self):
        return self._basePath

    @property
    def ipaddress(self):
        return self._ipaddress

    @property
    def port(self):
        return self._port

    def _getIPAddress(self):
        """Get IP address of the current network."""
        return socket.gethostbyname(socket.getfqdn())

    def _getPort(self):
        """Get port to be used from user. Default port is 3000."""
        print("Enter the socket to be used : ")
        try:
            return int(input())
        except:
            return 3000
