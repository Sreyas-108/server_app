from app.controller.OSCSender import OSCSender
import ipaddress


class FeedbackSender:
    """Feedback functionalities."""
    __instance = None
    __sender = None
    __ipAddress = ""

    @staticmethod
    def getInstance():
        """Get the singleton instance of [FeedbackSender]."""
        if FeedbackSender.__instance is None:
            FeedbackSender()
        return FeedbackSender.__instance

    def __init__(self):
        FeedbackSender.__instance = self
        self.__sender = OSCSender.getInstance()
        __ipAddress = self._getIP()

    def sendMessage(self, mod_type, data):
        """Send feedback as an OSC message with [data]."""
        print(data)
        self.__sender.sendMessage(mod_type, str(data), 1, self.__ipAddress)

    def _getIP(self):
        """Get IP address of controller application."""
        print("Enter IP of controller app : ")
        add = input()
        try:
            ipaddress.ip_address(add)
            return add
        except:
            return "127.0.0.1"
