from threading import Thread

from app.controller.OSCServer import OSCServer
from app.controller.SlaveHandler import SlaveHandler
from app.controller.Validation import ServerValidation
from app.controller.FeedbackSender import FeedbackSender
from app.utils.LogUtils import LogUtils


def startApplication():
    """Start application."""
    LogUtils.writeInfo("Starting application...")
    SlaveHandler.getInstance()
    ServerValidation.getInstance()
    FeedbackSender.getInstance()
    server = OSCServer()
    sc_thread = Thread(target=server.server_start())
    sc_thread.start()
