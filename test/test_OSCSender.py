import socket
import unittest
from unittest.mock import patch

from app.controller.ModuleType import ModuleType
from app.controller.OSCSender import OSCSender


class OSCSenderTest(unittest.TestCase):
    """Tests for OSC sender."""

    @patch('app.controller.OSCSender.SimpleUDPClient')
    @patch('app.controller.OSCSender.ServerValidation')
    def test_Sender(self, mock_validator, mock_client):
        mock_validator.getInstance.return_value = mock_validator.return_value
        mock_validator.return_value.id_lg = 0
        mock_validator.return_value.port = 90
        mock_validator.return_value.ipaddress = socket.gethostbyname(socket.getfqdn())
        mock_validator.return_value.basePath = '/test'
        OSCSender.getInstance().sendMessage(ModuleType.EXIT, 'test')
        mock_validator.getInstance.assert_called_once()
        mock_client.return_value.send.assert_called_once()
