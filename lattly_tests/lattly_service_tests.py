__author__ = 'yanikafarrugia'
import unittest


class LattlyServiceTests(unittest.TestCase):
	def test(self):
		self.assertEqual(1, 1)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(LattlyServiceTests)
	unittest.TextTestRunner(verbosity = 2).run(suite)
