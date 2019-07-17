from app.controller.OSCSender import OSCSender


class SlaveHandler:
    """Handles slave instances."""
    __instance = None
    __isMaster = True
    __sender = None

    @staticmethod
    def getInstance():
        """Get the singleton instance of [SlaveHandler]."""
        if SlaveHandler.__instance is None:
            SlaveHandler()
        return SlaveHandler.__instance

    def __init__(self):
        SlaveHandler.__instance = self
        self.__isMaster = self._isMaster() == 0
        if self.__isMaster is True:
            self.__numOfSlaves = self._getSlaves()
            self.__slaves = self._getIP()
            self.__sender = OSCSender.getInstance()

    def sendMessage(self, mod_type, data):
        """Send OSC message with [data] to the slave instances if it is a master machine."""
        if self.__isMaster is False:
            return
        for ip in self.__slaves:
            self.__sender.sendMessage(mod_type, data, 0, ip=ip)

    def _getSlaves(self):
        """Get number of slaves to be used from user. Default is 0."""
        print("Enter the number of slaves to be used : ")
        try:
            return int(input())
        except:
            return 0

    def _isMaster(self):
        """Get machine number from user. Default machine number is 0(master)."""
        print("Enter machine number (0 => master, >0 => slave) : ")
        try:
            return int(input())
        except:
            return 0

    def _getIP(self):
        """Get IP address of slaves to be used from user."""
        ip = []
        for i in range(self.__numOfSlaves):
            print("Enter IP address of " + str(i + 1) + " slave : ")
            try:
                ip.append(input())
            except:
                print('Invalid IP address. Please re-configure completely.')

        return ip
