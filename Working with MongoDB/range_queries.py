from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

db = client.uda

def find():
	# returns pop between 250k and 500k
	# query = {"populationTotal": {"$gt": 250000, "$lte": 500000}}

	# returns all city names that start with the letter X
	# query = {"name": {"$gt": "X", "$lte": "Y"}}

	# returns all cities with founding date between these
	# query = {"foundingDate": {"$gt": datetime(1800, 1, 1),
	# 						  "$lt": datetime(1937, 12, 31)
	# 						  }
	# 		}
	query = {"country_label" : {"$ne": "United States"}}

	cities = db.cities.find(query)

	num_cities = 0
	for c in cities:
		pprint(c)
		num_cities += 1
	print "number of cities matching: %d\n" % num_cities



if __name__ == "__main__":
	find()