__author__ = 'yanikafarrugia'
import unittest

import lattly_service.converter


class ConverterTests(unittest.TestCase):
	def test_degrees_to_radians(self):
		rad = lattly_service.converter.Converter.degrees_to_radians(120)
		self.assertEqual(rad, 2.0943951023931953)
		self.assertIsNotNone(rad)
		self.assertTrue(rad > 2)

	def test_radians_to_degrees(self):
		deg = lattly_service.converter.Converter.radians_to_degrees(1.57)
		self.assertIsNotNone(deg)
		self.assertTrue(deg < 90.0)
		self.assertTrue(deg > 89.9)
		self.assertEqual(deg, 89.954373835539243)

	def test_radians_to_cartesian(self):
		car = lattly_service.converter.Converter.radians_to_cartesian(0.73091096, -1.5294285)
		self.assertIsNotNone(car)
		self.assertTrue(car[0] > 0.03079231)
		self.assertTrue(car[1] < -0.74392960)
		self.assertTrue(car[2] > 0.66754818)

	def test_cartesian_to_radians(self):
		carty = [0.12824063, -0.75020731, 0.64125282]
		rad = lattly_service.converter.Converter.cartesian_to_radians(carty)
		self.assertIsNotNone(rad)
		self.assertTrue(rad[0] > 0.70015084)
		self.assertTrue(rad[1] < -1.40149245)


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(ConverterTests)
	unittest.TextTestRunner(verbosity = 2).run(suite)
