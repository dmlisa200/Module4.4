import unittest


class test_average_negative_input(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)


if __name__ == '__main__':
    unittest.main()
