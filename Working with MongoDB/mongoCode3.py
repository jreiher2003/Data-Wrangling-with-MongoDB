from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.uda

def find():
	autos = db.autos.find({"manufacturer_label": "Toyota"})
	for a in autos:
		pprint(a)

if __name__ == '__main__':
	find()