import unittest
import trebuchet


class TestTrebuchet(unittest.TestCase):
    def test_calibrate(self):
        calibration = trebuchet.calibrate()
        self.assertEqual(53386, calibration)

    def test_calibrate_again(self):
        calibration = trebuchet.calibrate_again()
        self.assertEqual(53312, calibration)


if __name__ == "__main__":
    unittest.main()
