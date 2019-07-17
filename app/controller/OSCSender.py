from pythonosc import osc_bundle_builder
from pythonosc import osc_message_builder
from pythonosc.udp_client import SimpleUDPClient

from app.controller.Validation import ServerValidation


class OSCSender:
    """OSC sender functionalities."""
    __instance = None
    __servervalidation = None

    @staticmethod
    def getInstance():
        """Get the singleton instance of [OSCSender]."""
        if OSCSender.__instance is None:
            OSCSender()
        return OSCSender.__instance

    def __init__(self):
        OSCSender.__instance = self
        self.__servervalidation = ServerValidation.getInstance()

    def sendMessage(self, mod_type, data, disp, ip=None):
        """Send OSC message with [data] to the given socket and ip address."""
        ip = ip or self.__servervalidation.ipaddress
        client = SimpleUDPClient(ip,
                                 self.__servervalidation.port + disp)

        bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
        msg = osc_message_builder.OscMessageBuilder(address=self.__servervalidation.basePath + mod_type.value[1])
        msg.add_arg(self.__servervalidation.id_lg)
        msg.add_arg(mod_type.value[0])
        msg.add_arg(data)
        bundle.add_content(msg.build())
        bundle = bundle.build()
        client.send(bundle)
