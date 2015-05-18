from pymongo import MongoClient
from pprint import pprint

client  = MongoClient("mongodb://localhost:27017")
db = client.uda

def main():
	city = db.cities.update({"country_label": "Germany"}, 
					 {"$set": {"isoCountryCode": "DEU"}
					 }, multi=True)
	db.cities.save(city)

if __name__ == "__main__":
	main()