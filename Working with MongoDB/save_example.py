from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.uda

def main():
	city = db.cities.find_one({"country_label": "Germany"})
	city["isoCountryCode"] = "DEU"
	db.cities.save(city)

if __name__ == "__main__":
	main()