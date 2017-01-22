__author__ = 'yanikafarrugia'


class Point:
	def __init__(self, latitude, longitude):
		self.set_latitude(latitude)
		self.set_longitude(longitude)

	def get_latitude(self):
		return self.__latitude

	def set_latitude(self, latitude):
		self.__latitude = latitude

	def get_longitude(self):
		return self.__longitude

	def set_longitude(self, longitude):
		self.__longitude = longitude
