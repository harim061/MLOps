import change
import unittest


class TestChange(unittest.TestCase):
    def test_get_c500(self):
        alg = change.Algorithm(5000, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 10)
        self.assertEqual(c100, 0)
        self.assertEqual(c50, 0)
        self.assertEqual(c10, 0)
    def test_get_c100(self):
        alg = change.Algorithm(200, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 0)
        self.assertEqual(c100, 2)
        self.assertEqual(c50, 0)
        self.assertEqual(c10, 0)
    def test_get_c50(self):
        alg = change.Algorithm(50, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 0)
        self.assertEqual(c100, 0)
        self.assertEqual(c50, 1)
        self.assertEqual(c10, 0)
    def test_get_c10(self):
        alg = change.Algorithm(40, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 0)
        self.assertEqual(c100, 0)
        self.assertEqual(c50, 0)
        self.assertEqual(c10, 4)
    def test_complex(self):
        alg = change.Algorithm(4290, coin_types={10, 50, 100, 500})
        c500, c100, c50, c10 = alg.calculate()
        self.assertEqual(c500, 8)
        self.assertEqual(c100, 2)
        self.assertEqual(c50, 1)
        self.assertEqual(c10, 4)
    def test_not_ideal(self):
        alg = change.Algorithm(120, coin_types={10, 60, 100})
        c100, c60, c10 = alg.calculate()
        with self.subTest("우리의 알고리즘"):
            self.assertEqual(c100, 1)
            self.assertEqual(c60, 0)
            self.assertEqual(c10, 2)
        """with self.subTest('이상적인 경우'):
            self.assertEqual(c100, 0)
            self.assertEqual(c60, 2)
            self.assertEqual(c10, 0)"""

if __name__ == "__main__":
    unittest.main()