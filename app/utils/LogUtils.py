import logging
import os
from pathlib import Path


class LogUtils:
    """Utilities for Logging."""
    path = Path(os.path.abspath(os.path.join(os.path.abspath(os.pardir), '/logs')))
    """Path of the logs file."""
    @classmethod
    def setUpLogs(cls):
        """Create and set log file format."""
        if not cls.path.exists():
            os.mkdir(cls.path)
        logging.basicConfig(filename=str(cls.path) + '/test.log', filemode='a', level=logging.DEBUG,
                            format='%(asctime)s : %(name)s - %(levelname)s - %(message)s : [in %(pathname)s:%(lineno)d]')

    @staticmethod
    def writeWarning(data):
        """Write warning log of [data]. For any failure."""
        LogUtils.setUpLogs()
        logging.warning(str(data))

    @staticmethod
    def writeCritical(data):
        """Write critical log of [data]. For high priority error."""
        LogUtils.setUpLogs()
        logging.critical(str(data))

    @staticmethod
    def writeInfo(data):
        """Write info log of [data]. For step debugging."""
        LogUtils.setUpLogs()
        logging.info(str(data))
