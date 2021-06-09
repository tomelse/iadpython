# pylint: disable=invalid-name
# pylint: disable=bad-whitespace
# pylint: disable=no-self-use
# pylint: disable=too-many-locals

"""Tests for sphere object."""

import unittest
import numpy as np
import iadpython

class A_nothing_sandwich(unittest.TestCase):
    """Empty layer in air."""

    def test_01_object_creation(self):
        """Simple sphere creation."""
        s = iadpython.sphere.Sphere(200,20)
        np.testing.assert_allclose(s.d_sphere, 200, atol=1e-5)
        np.testing.assert_allclose(s.d_sample, 20, atol=1e-5)
        np.testing.assert_allclose(s.d_entrance, 0, atol=1e-5)
        np.testing.assert_allclose(s.d_detector, 0, atol=1e-5)

    def test_02_portsize(self):
        """Test setting ."""
        s = iadpython.sphere.Sphere(200,20)
        s.d_entrance = 10
        s.d_detector = 5
        s.d_sample = 18
        np.testing.assert_allclose(s._d_sphere, 200, atol=1e-5)
        np.testing.assert_allclose(s._d_sample, 18, atol=1e-5)
        np.testing.assert_allclose(s._d_entrance, 10, atol=1e-5)
        np.testing.assert_allclose(s._d_detector, 5, atol=1e-5)
        np.testing.assert_allclose(s.d_sphere, 200, atol=1e-5)
        np.testing.assert_allclose(s.d_sample, 18, atol=1e-5)
        np.testing.assert_allclose(s.d_entrance, 10, atol=1e-5)
        np.testing.assert_allclose(s.d_detector, 5, atol=1e-5)



if __name__ == '__main__':
    unittest.main()
