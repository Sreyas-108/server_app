from app.controller.OSCSender import OSCSender


class FeedbackSender:
    """Feedback functionalities."""
    __instance = None
    __sender = None

    @staticmethod
    def getInstance():
        """Get the singleton instance of [FeedbackSender]."""
        if FeedbackSender.__instance is None:
            FeedbackSender()
        return FeedbackSender.__instance

    def __init__(self):
        FeedbackSender.__instance = self
        self.__sender = OSCSender.getInstance()

    def sendMessage(self, mod_type, data):
        """Send feedback as an OSC message with [data]."""
        self.__sender.sendMessage(mod_type, str(data), 100)
