import unittest
import trebuchet
import cubes


class TestAdventOfCode(unittest.TestCase):
    def test_calibrate(self):
        result = trebuchet.calibrate()
        self.assertEqual(53386, result)

    def test_calibrate_again(self):
        result = trebuchet.calibrate_again()
        self.assertEqual(53312, result)

    def test_sum_possible(self):
        result = cubes.sum_possible()
        self.assertEqual(2204, result)

    def test_sum_powers(self):
        calibration = cubes.sum_powers()
        self.assertEqual(71036, calibration)


if __name__ == "__main__":
    unittest.main()
