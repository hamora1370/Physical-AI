"""Regression checks for elementary forward kinematics."""
import importlib.util
import math
from pathlib import Path
import unittest

MODULE = Path(__file__).resolve().parents[1] / "exercises" / "01_robot_math" / "fk_2r.py"
spec = importlib.util.spec_from_file_location("fk_2r", MODULE)
fk_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fk_module)
fk_2r = fk_module.fk_2r


class FK2RTests(unittest.TestCase):
    def test_extended(self):
        x, y = fk_2r(0.3, 0.2, 0.0, 0.0)
        self.assertAlmostEqual(x, 0.5)
        self.assertAlmostEqual(y, 0.0)

    def test_vertical(self):
        x, y = fk_2r(0.3, 0.2, math.pi / 2, 0.0)
        self.assertAlmostEqual(x, 0.0, places=8)
        self.assertAlmostEqual(y, 0.5, places=8)

    def test_folded(self):
        x, y = fk_2r(0.3, 0.2, 0.0, math.pi)
        self.assertAlmostEqual(x, 0.1, places=8)
        self.assertAlmostEqual(y, 0.0, places=8)

    def test_invalid_links(self):
        with self.assertRaises(ValueError):
            fk_2r(0.0, 0.2, 0.0, 0.0)


if __name__ == "__main__":
    unittest.main()
