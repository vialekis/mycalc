# import unittest
# import random
# import mycalc
#
# class MyCalcTest(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(mycalc.add(1, 2), 3)
#
#     @unittest.skipIf(random.random()<0.5, "пропускаем по рандому")
#     def test_sub(self):
#         self.assertEqual(mycalc.sub(4, 1), 2)
#
#     def test_mul(self):
#         self.assertEqual(mycalc.mul(3, 7), 21)
#
#     def test_div(self):
#         self.assertEqual(mycalc.div(16, 8), 2)
#
#     def test_sqrt(self):
#         self.assertAlmostEqual(
#             mycalc.sqrt(9),
#             3,
#             delta=0.000000001
#         )
#
# if __name__ == "__main__":
#     unittest.main()

import random
import unittest
import mycalc

class MyCalcTestIncrease(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mycalc.add(1, 2), 3)

    def test_mul(self):
        self.assertEqual(mycalc.mul(3, 7), 21)

    def test_div(self):
        self.assertEqual(mycalc.div(16, 0), 2)
        with self.assertRaises(ZeroDivisionError):
            mycalc.div(1, 0)


# class MyCalcTestDecrease(unittest.TestCase):
#     def test_sub(self):
#         self.assertEqual(mycalc.sub(4, 2), 2)
#
#     # def test_div(self):
#     #     self.assertEqual(mycalc.div(16, 8), 2)
#
#     def test_div(self):
#         self.assertEqual(mycalc.div(16, 8), 2)
#         with self.assertRaises(ZeroDivisionError):
#             mycalc.div(1, 0)
#

# @unittest.skip("Корни не нужны.")
# class MyCalcTestDecrease(unittest.TestCase):
#     def test_sqrt(self):
#         self.assertAlmostEqual(
#             mycalc.sqrt(9),
#             3,
#             delta=0.000000001
#         )

if __name__ == "__main__":
    unittest.main()