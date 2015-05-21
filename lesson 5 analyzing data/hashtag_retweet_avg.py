from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.twitter

def hashtag_retweet_avg():
	result = db.tweets.aggregate([
			{"$unwind": "$entities.hashtags"},
			{"$group": {"_id": "$entities.hashtags.text", "retweet_avg": {"$avg": "$retweet_count"} } },
			{"$sort": {"retweet_avg": -1} }
		])
	return result

def unique_hashtags_by_user():
	result = db.tweets.aggregate([
			{"$unwind": "$entities.hashtags"},
			{"$group": {"_id": "$user.screen_name", "unique_hashtags": {"$addToSet": "$entities.hashtags.text"} } },
			{"$sort": {"retweet_avg": -1} }
		])
	return result


if __name__ == "__main__":
	# result = hashtag_retweet_avg()
	result = unique_hashtags_by_user()
	pprint(result)