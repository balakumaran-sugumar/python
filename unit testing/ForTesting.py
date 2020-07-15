import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        capitalize = "python".capitalize()
        self.assertEqual(capitalize, "python")


if __name__ == '__main__':
    unittest.main()
