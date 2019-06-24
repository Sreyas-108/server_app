import socket
import unittest
from unittest.mock import patch

from app.controller.OSCServer import OSCServer


class OSCServerTest(unittest.TestCase):
    """Tests for OSC server. """

    @patch('app.controller.OSCServer.ServerValidation')
    def test_Server(self, mock_validator):
        mock_validator.getInstance.return_value = mock_validator.return_value
        mock_validator.return_value.port = 90
        mock_validator.return_value.ipaddress = socket.gethostbyname(socket.getfqdn())
        mock_validator.return_value.basePath = '/test'
        OSCServer.getInstance()
        mock_validator.getInstance.assert_called_once()
