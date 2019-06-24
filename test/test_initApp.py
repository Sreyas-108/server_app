import unittest
from unittest.mock import patch

from app.controller import server


class InitAppTest(unittest.TestCase):
    """ Tests app initialization. """

    @patch('app.controller.server.OSCServer')
    @patch('app.controller.server.Thread')
    @patch('app.controller.server.ServerValidation')
    def test_ServerStart(self, mock_server, mock_thread, mock_validator):
        mock_server.return_value.server_start.return_value = 0
        mock_thread.return_value.start.return_value = mock_server.return_value.server_start()
        mock_validator.return_value.getInstance.return_value = 0
        server.startApplication()
        mock_validator.assert_called_once()
        mock_thread.return_value.start.assert_called_once()
        mock_server.return_value.server_start.assert_called_once()
