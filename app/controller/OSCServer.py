from pythonosc import dispatcher
from pythonosc import osc_server

from app.controller import MessageHandler
from app.controller.Validation import ServerValidation
from app.utils.LogUtils import LogUtils


class OSCServer:
    """OSCServer set-up functionalities."""
    __instance = None
    __servervalidation = None

    def __init__(self):
        OSCServer.__instance = self
        self.__servervalidation = ServerValidation.getInstance()
        disp = dispatcher.Dispatcher()
        disp.map(self.__servervalidation.basePath + "/*", MessageHandler.handle)
        self.server = osc_server.ThreadingOSCUDPServer(
            (self.__servervalidation.ipaddress, self.__servervalidation.port), disp)

    def server_start(self):
        """Start OSC server forever."""
        LogUtils.writeInfo("Starting server...")
        print("Serving on {}".format(self.server.server_address))
        self.server.serve_forever()

    def server_end(self):
        """Exit OSC server."""
        LogUtils.writeInfo("Shutting down server...")
        print("Closing server on {}".format(self.server.server_address))
        self.server.shutdown()

    @staticmethod
    def getInstance():
        """Get the singleton instance of [OSCServer]."""
        if OSCServer.__instance is None:
            OSCServer()
        return OSCServer.__instance
