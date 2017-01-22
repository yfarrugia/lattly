__author__ = 'yanikafarrugia'

import sys
import logging

import math

logger = logging.getLogger('lattly')


class Converter:
	def degrees_to_radians(degrees):
		try:
			rad = (degrees * (math.pi / 180.0))
			return rad
		except IOError as io_exc:
			logger.error("I/O error({0}): {1}".format(io_exc.errno, io_exc.strerror))
		except ValueError as val_err:
			logger.error("Could not convert degrees to radians. Exception: {0}".format(val_err))
		except:
			logger.error("Could not convert degrees to radians. Exception: {0}".format(sys.exc_info()[0]))

	def radians_to_degrees(radians):
		try:
			degrees = (radians * (180.0 / math.pi))
			return degrees
		except IOError as io_exc:
			logger.error("I/O error({0}): {1}".format(io_exc.errno, io_exc.strerror))
		except ValueError as val_err:
			logger.error("Could not convert radians to degrees. Exception: {0}".format(val_err))
		except:
			logger.error("Could not convert radians to degrees. Exception: {0}".format(sys.exc_info()[0]))

	def radians_to_cartesian(rad_lat, rad_long):
		try:
			cartesian = [0.00] * 3

			cartesian[0] = math.cos(rad_lat) * math.cos(rad_long)
			cartesian[1] = math.cos(rad_lat) * math.sin(rad_long)
			cartesian[2] = math.sin(rad_lat)
			return cartesian
		except IOError as ioExc:
			logger.error("I/O error({0}): {1}".format(ioExc.errno, ioExc.strerror))
		except ValueError as valErr:
			logger.error("Could not convert radians to cartesian. Exception: {0}".format(valErr.strerror))
		except:
			logger.error("Could not convert radians to cartesian. Exception: {0}".format(sys.exc_info()[0]))

	def cartesian_to_radians(cartesian):
		try:
			radians = [0.00] * 2

			longitude = math.atan2(cartesian[1], cartesian[0])
			hyp = math.sqrt((cartesian[0] * cartesian[0]) + (cartesian[1] * cartesian[1]))
			latitude = math.atan2(cartesian[2], hyp)

			radians[0] = latitude
			radians[1] = longitude
			return radians
		except IOError as ioExc:
			logger.error("I/O error({0}): {1}".format(ioExc.errno, ioExc.strerror))
		except ValueError as valErr:
			logger.error("Could not convert cartesian to radians. Exception: {0}".format(valErr.strerror))
		except:
			logger.error("Could not convert cartesian to radians. Exception: {0}".format(sys.exc_info()[0]))
