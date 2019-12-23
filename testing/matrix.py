import vgl

import unittest

class TestMatrix(unittest.TestCase):

    def test_mul(self):
        m = vgl.mat2(1,2,0,1)
        n = vgl.mat2(3,1,1,1)
        self.assertEqual(m*n, vgl.mat2(5,3,1,1))

if __name__ == '__main__':
    unittest.main()
