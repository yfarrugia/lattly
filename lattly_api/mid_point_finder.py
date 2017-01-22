__author__ = 'yanikafarrugia'

import logging

from flask import Flask


# Initialize the Flask application
app = Flask(__name__)

logger = logging.getLogger('lattly')


@app.route('/')
def index():
	return "Hello, World!"

# Point FindCenterMidPoint(List<Point> points, Point midPoint);
# Point FindMidPoint(List<Point> points);
#     @app.route('/getMidPoint', methods=['GET'])
# @app.route('/getCenterMidPoint/<points>', methods = ['GET'])
# def getCenterMidPoint(points):
# 	pnts = []
# 	# data = '{"lat": "", "long": ""}'
# 	try:
# 		for pt in points:
# 			lattly_dto.point.Point.set_latitude(pt['lat'])
# 			lattly_dto.point.Point.set_longitude(pt['long'])
# 			pnts.append(pt)
# 		cnt = lattly_service.mid_point_finder.MidPointFinder(pnts)
# 		return "Return Center Mid Point JSON data" + str(cnt)
# 	except Exception as e:
# 		logger.error("message")




# class MidPointFinder():
#     def getMidPoint(self, points):
#         # mezzo_service.mid_point_finder.find_mid_point(points)
#         return "Return Mid Point JSON data"
#
#     @app.route("/getCenterMidPoint")
#     def getCenterMidPoint(self, points):
#         # mezzo_service.mid_point_finder.(points)
#         return "Return Center Mid Point JSON data"
#     # def find_mid_point(self, points):
#     #    return {'hello': 'world'}
#
#     # def find_center_mid_point(self, points, midPoint):
#     #    return {'hello': 'world'}


# api.add_resource(MidPointFinder, '/')

if __name__ == '__main__':
	app.run(debug = True)
