from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.twitter

def user_mentions():
	result = db.tweets.aggregate([
			{"$unwind": "$entities.user_mentions"},
			{"$group": {"_id": "$user.screen_name", "count": {"$sum": 1} } },
			{"$sort": {"count": -1} },
			{"$limit": 1 }
		])
	return result

if __name__ == "__main__":
	result = user_mentions()
	pprint(result)