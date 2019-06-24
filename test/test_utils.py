import logging
import random
import unittest

from app.utils.KMLUtils import KMLUtils
from app.utils.LogUtils import LogUtils


class UtilsTest(unittest.TestCase):
    """Tests for all utility functions."""

    def test_range(self):
        range = KMLUtils.convertZoomToRange(random.randint(1, 1000))
        self.assertGreater(range, 299)

    def test_pathExistence(self):
        LogUtils.setUpLogs()
        self.assertEqual(LogUtils.path.exists(), True)

    def test_logEntry(self):
        with self.assertLogs(logging.getLogger(), logging.INFO):
            LogUtils.writeInfo('Default test')
        with self.assertLogs(logging.getLogger(), logging.WARNING):
            LogUtils.writeWarning('Default test')
        with self.assertLogs(logging.getLogger(), logging.CRITICAL):
            LogUtils.writeCritical('Default test')
