import logging
import unittest
from pathlib import Path

from app.flyto.FlyToOptions import FlyToOptions
from app.flyto.GenerateKML import generateFlyTo
from app.gestures.GenerateKML import generateGesture
from app.models.KMLData import KMLData
from app.models.TourData import TourData
from app.poi.GenerateKML import generatePOI
from app.tours.GenerateKML import generateTour
from app.utils.KMLUtils import KMLUtils


class GenerateKMLTest(unittest.TestCase):
    """Tests for generation of KML for all module types."""

    def test_POI(self):
        with self.assertLogs(logging.getLogger(), logging.INFO):
            generatePOI(KMLData())
            self.assertEqual(Path(KMLUtils.getFilePath()).exists(), True)

    def test_gestures(self):
        with self.assertLogs(logging.getLogger(), logging.INFO):
            generateGesture(KMLData())
            self.assertEqual(Path(KMLUtils.getFilePath()).exists(), True)

    def test_flyto(self):
        with self.assertLogs(logging.getLogger(), logging.INFO):
            generateFlyTo(FlyToOptions.MARS.value)
            self.assertEqual(Path(KMLUtils.getFilePath()).exists(), True)

    def test_tour(self):
        with self.assertLogs(logging.getLogger(), logging.INFO):
            generateTour(TourData())
            self.assertEqual(Path(KMLUtils.getFilePath()).exists(), True)
