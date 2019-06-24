from threading import Thread

from app.controller.OSCServer import OSCServer
from app.controller.Validation import ServerValidation
from app.utils.LogUtils import LogUtils


def startApplication():
    """Start application."""
    LogUtils.writeInfo("Starting application...")
    ServerValidation.getInstance()
    server = OSCServer()
    sc_thread = Thread(target=server.server_start())
    sc_thread.start()
