__author__ = 'yanikafarrugia'


class Location:
	def __init__(self, location_id = None, description = None, latitude = 0, longitude = 0):
		self.__location_id = location_id
		self.__description = description
		self.__longitude = longitude
		self.__latitude = latitude

	@property
	def location_id(self):
		return self.__location_id

	@property
	def description(self):
		return self.__description

	@property
	def latitude(self):
		return self.__latitude

	@property
	def longitude(self):
		return self.__longitude
