import unittest
import libcplx
import math

class Testlibcplx(unittest.TestCase):

    def test_sumcplx(self):
        self.assertEqual(libcplx.sumcplx((2,3),(3,3)),(5,6))
        self.assertEqual(libcplx.sumcplx((-1,-1),(1,1)),(0,0))
        self.assertEqual(libcplx.sumcplx((2,-3),(3,3)),(5,0))


    def test_multcplx(self):
        self.assertEqual(libcplx.multcplx((2,3),(3,3)),(-3,15))
        self.assertEqual(libcplx.multcplx((-1,-1),(1,1)),(0,-2))
        self.assertEqual(libcplx.multcplx((2,-3),(3,3)),(15,-3))

    def test_restcplx(self):
        self.assertEqual(libcplx.restcplx((2,3),(3,3)),(-1,0))
        self.assertEqual(libcplx.restcplx((-1,-1),(1,1)),(-2,-2))
        self.assertEqual(libcplx.restcplx((2,-3),(3,3)),(-1,-6))

    def test_divcplx(self):
        self.assertEqual(libcplx.divcplx((2,3),(3,3)),(5/6,1/6))
        self.assertEqual(libcplx.divcplx((-1,-1),(1,1)),(-1,0))
        self.assertEqual(libcplx.divcplx((2,-3),(3,3)),(-1/6,-5/6))

    def test_modcplx(self):
        self.assertEqual(libcplx.modcplx((3,4)), 5)
        self.assertEqual(libcplx.modcplx((3,2)), 13**0.5)
        self.assertEqual(libcplx.modcplx((3,-4)), 5)
    
    def test_conjcplx(self):
        self.assertEqual(libcplx.conjcplx((3,4)), (3,-4))
        self.assertEqual(libcplx.conjcplx((3,2)), (3,-2))
        self.assertEqual(libcplx.conjcplx((3,-4)), (3,4))

    def test_fasecplx(self):
        self.assertEqual(libcplx.fasecplx((3,4)), 53.13010235415598)
        self.assertEqual(libcplx.fasecplx((3,2)), 33.690067525979785)
        self.assertEqual(libcplx.fasecplx((3,-4)), -53.13010235415598)
    
    def test_ptoccplx(self):
        self.assertEqual(libcplx.ptoccplx((3,4)), (3.0000000000000004, 3.9999999999999996))
        self.assertEqual(libcplx.ptoccplx((3,2)), (3.0, 1.9999999999999996))
        self.assertEqual(libcplx.ptoccplx((3,-4)), (3.0000000000000004, -3.9999999999999996))

if __name__ == '__main__':
    unittest.main()