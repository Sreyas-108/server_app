from app.controller import OSCServer
from app.controller.FeedbackSender import FeedbackSender
from app.controller.ModuleType import ModuleType
from app.controller.Validation import ServerValidation
from app.flyto.GenerateKML import generateFlyTo
from app.gestures.GenerateKML import generateGesture
from app.models.KMLData import KMLData
from app.models.OverlayData import OverlayData
from app.models.TourData import TourData
from app.overlay.GenerateKML import generateOverlay
from app.poi.GenerateKML import generatePOI
from app.tours.GenerateKML import generateTour
from app.utils.LogUtils import LogUtils


def handle(self, *varargs):
    """Handler for OSC data. Initiates validation and action based on [varargs]."""
    if len(varargs) != 3:
        LogUtils.writeCritical("Parameter validation failure : Incorrect number of parameters sent in OSC message")
        FeedbackSender.getInstance().sendMessage(ModuleType.EXIT,
                                                 "Parameter validation failure : Incorrect number of parameters sent in OSC message")
        return
    id_lg = varargs[0]
    encoding = varargs[1]
    data = varargs[2]
    LogUtils.writeInfo("Query received." + str(self) + " " + str(id_lg) + " " + str(encoding) + " " + str(data))
    serverVal = ServerValidation.getInstance()
    if not (serverVal.validateID(id_lg)):
        LogUtils.writeWarning("Server validation failure : ")
        return
    try:
        mod_type = ModuleType((encoding, str(self)[len(serverVal.basePath):]))
    except Exception as e:
        LogUtils.writeWarning("Server validation failure : " + str(e))
        return

    OSCServer.OSCServer.getInstance().slaveinstance.sendMessage(mod_type, data)

    if mod_type is ModuleType.EXIT:
        OSCServer.OSCServer.getInstance().server_end()
    elif mod_type is ModuleType.GESTURE:
        kmldata = KMLData.fromJson(data)
        generateGesture(kmldata, serverVal.ipaddress)
    elif mod_type is ModuleType.FLYTO:
        generateFlyTo(data, serverVal.ipaddress)
    elif mod_type is ModuleType.POI:
        kmldata = KMLData.fromJson(data)
        generatePOI(kmldata, serverVal.ipaddress)
    elif mod_type is ModuleType.TOUR:
        tourdata = TourData.fromJson(data)
        generateTour(tourdata, serverVal.ipaddress)
    elif mod_type is ModuleType.OVERLAY:
        overlaydata = OverlayData.fromJson(data)
        generateOverlay(overlaydata, serverVal.ipaddress)
    else:
        LogUtils.writeWarning("Module type not handled failure.")
