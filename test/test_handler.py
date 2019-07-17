import logging
import unittest
from unittest.mock import patch

from app.controller.MessageHandler import handle
from app.controller.ModuleType import ModuleType


class HandlerTest(unittest.TestCase):
    """Tests for handler of the OSC Server."""

    @patch('app.controller.MessageHandler.ServerValidation')
    @patch('app.controller.MessageHandler.OSCServer.OSCServer')
    def test_exitModtype(self, mock_server, mock_validator):
        basePath = '/testpath'
        modtype = ModuleType.EXIT
        mock_validator.return_value.validateID.return_value = True
        mock_validator.return_value.basePath = basePath
        mock_validator.getInstance.return_value = mock_validator.return_value

        mock_server.getInstance.return_value = mock_server.return_value
        mock_server.return_value.server_end.return_value = 0

        handle(basePath + modtype.value[1], 0, modtype.value[0], 0)
        mock_validator.return_value.validateID.assert_called_once()
        mock_server.return_value.server_end.assert_called_once()

    @patch('app.controller.MessageHandler.ServerValidation')
    def test_invalidModType(self, mock_validator):
        mock_validator.return_value.validateID.return_value = True
        mock_validator.getInstance.return_value = mock_validator.return_value
        with self.assertLogs(logging.getLogger(), logging.WARNING):
            handle('', 0, 0, 0)
        mock_validator.return_value.validateID.assert_called_once()

    @patch('app.controller.MessageHandler.FeedbackSender')
    def test_invalidParams(self, mock_sender):
        with self.assertLogs(logging.getLogger(), logging.CRITICAL):
            mock_sender.return_value.sendMessage.return_value = 0
            mock_sender.getInstance.return_value = mock_sender.return_value
            handle(0)
            mock_sender.return_value.sendMessage.assert_called_once()
