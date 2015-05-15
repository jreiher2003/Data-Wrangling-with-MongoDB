from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')

tesla_s = {
	"manufacturer" : "Tesla Motors",
	"class" : "full-size",
	"body style" : "5-door liftback",
	"production" : [2012,2013],
	"model years" : [2013],
	"layout" : ["Rear-motor", "rear-wheel drive"],
	"designer" : {
		"firstname" : "Franz",
		"surname" : "von Holhausen"
	},
	"assembly" : [
		{
			"country" : "United States",
			"city" : "Fremont", 
			"state" : "California",
		},
		{
			"country" : "The Netherlands",
			"city" : "Tilburg"
		}
	]
}

db = client.examples
db.autos.insert(tesla_s)	

for a in db.autos.find():
	pprint(a)