import vgl

import unittest

class TestMatrix(unittest.TestCase):

    def test_mul_by_mat(self):
        m = vgl.mat2(1,2,0,1)
        n = vgl.mat2(3,1,1,1)
        self.assertEqual(m*n, vgl.mat2(5,3,1,1))

    def test_mul_by_mat(self):
        m = vgl.mat3(1,2,3,4,5,6,7,8,9)
        u = vgl.mat3(3,2,1)
        self.assertEqual(m*u, vgl.mat3(10, 28, 46))
        



if __name__ == '__main__':
    unittest.main()
