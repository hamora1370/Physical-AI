"""Root-discoverable regression checks for the learner-authored SCARA-01 FK.

These mirror the original practice tests, which remain in exercises/ as learning
evidence. Invoke from repo root: python3 -m unittest discover -s tests -v
"""
import importlib.util
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "exercises" / "01_robot_math" / "scara_fk_practice.py"
spec = importlib.util.spec_from_file_location("scara_fk_practice", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
fk_scara_2r = module.fk_scara_2r


class ScaraLearnerFKTests(unittest.TestCase):
    def test_fully_extended(self):
        x, y = fk_scara_2r(0.0, 0.0)
        self.assertAlmostEqual(x, 0.24, places=9)
        self.assertAlmostEqual(y, 0.0, places=9)

    def test_vertical(self):
        x, y = fk_scara_2r(math.radians(90), 0.0)
        self.assertAlmostEqual(x, 0.0, places=9)
        self.assertAlmostEqual(y, 0.24, places=9)

    def test_folded(self):
        x, y = fk_scara_2r(0.0, math.radians(180))
        self.assertAlmostEqual(x, 0.02, places=9)
        self.assertAlmostEqual(y, 0.0, places=9)

    def test_nontrivial_angles(self):
        x, y = fk_scara_2r(math.radians(30), math.radians(60))
        self.assertAlmostEqual(x, 0.1125833, places=6)
        self.assertAlmostEqual(y, 0.175, places=6)


if __name__ == "__main__":
    unittest.main()
