__author__ = 'yanikafarrugia'

import sys
import logging

import lattly_service.converter

logger = logging.getLogger('lattly')


class MidPointFinder:
	def compute_weighted_average(cartesian_point, weights, total_weight):
		try:
			weighted_average = [0.0] * 3

			for point in cartesian_point:
				weighted_x = weighted_x + (cartesian_point[0] * weights[cartesian_point.index(point)])
				weighted_y = weighted_y + (cartesian_point[1] * weights[cartesian_point.index(point)])
				weighted_z = weighted_z + (cartesian_point[2] * weights[cartesian_point.index(point)])

			weighted_average[0] = weighted_x / total_weight
			weighted_average[1] = weighted_y / total_weight
			weighted_average[2] = weighted_z / total_weight

			return weighted_average
		except IOError as ioExc:
			logger.error("I/O error({0}): {1}".format(ioExc.errno, ioExc.strerror))
		except ValueError as valErr:
			logger.error("Could not compute weighted average. Exception: {0}".format(valErr.strerror))
		except:
			logger.error("Could not compute weighted average. Exception: {0}".format(sys.exc_info()[0]))

	def find_mid_point(points):
		try:
			total_weight = 0.0
			weights = []
			cartesian_points = []

			for point in points:
				rad_lat = lattly_service.converter.degrees_to_radians(point.get_latitude())
				rad_long = lattly_service.converter.degrees_to_radians(point.get_longitude())

				lattly_service.converter.radians_to_cartesians(rad_lat, rad_long)
		except IOError as ioExc:
			logger.error("I/O error({0}): {1}".format(ioExc.errno, ioExc.strerror))
		except ValueError as valErr:
			logger.error("Could not find mid point. Exception: {0}".format(valErr.strerror))
		except:
			logger.error("Could not find mid point. Exception: {0}".format(sys.exc_info()[0]))
			logger.error("Could not find mid point. Exception: {0}".format(sys.exc_info()[0]))
