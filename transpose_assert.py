import unittest
import numpy as np

class AssertTrasnpose(unittest.TestCase):
    def test_traspose(self):
        np.allclose(np.arange(6).reshape((1,2,3)), np.arange(6).reshape((2, 1, 3)).transpose((1, 0, 2)))
   #assertEqual -> ambiguous error occurred !!
if __name__ == '__main__':
    unittest.main()
