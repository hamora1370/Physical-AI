import math
import unittest

from scara_fk_practice import fk_scara_2r


class TestScaraFK(unittest.TestCase):

    def test_fully_extended(self):
        x, y = fk_scara_2r(0.0, 0.0)

        self.assertAlmostEqual(x, 0.24, places=9)
        self.assertAlmostEqual(y, 0.0, places=9)

    def test_vertical(self):
        x, y = fk_scara_2r(math.radians(90.0), 0.0)

        self.assertAlmostEqual(x, 0.0, places=9)
        self.assertAlmostEqual(y, 0.24, places=9)

    def test_folded(self):
        x, y = fk_scara_2r(0.0, math.radians(180.0))

        self.assertAlmostEqual(x, 0.02, places=9)
        self.assertAlmostEqual(y, 0.0, places=9)

    def test_nontrivial_angles(self):
        x, y = fk_scara_2r(math.radians(30.0), math.radians(60.0))

        self.assertAlmostEqual(x, 0.1125833, places=6)
        self.assertAlmostEqual(y, 0.175, places=6)

if __name__ == "__main__":
    unittest.main()
