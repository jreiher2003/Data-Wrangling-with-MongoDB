from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.uda

def find():
	query = {"manufacturer_label" : "Toyota", 'class_label': 'Mid-size car'}
	projection = {"_id": 0, "name": 1}			  
	autos = db.autos.find(query, projection)
	for a in autos:
		pprint(a)

if __name__ == '__main__':
	find()