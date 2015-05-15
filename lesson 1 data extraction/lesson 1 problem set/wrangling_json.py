import json
import codecs
import requests
import pprint
import urllib2

BASE_URI = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/1?api-key=b2f92fb98088b256316d8584e1aaca61:13:70248560"

response = urllib2.urlopen(BASE_URI)
json_obj = json.load(response)
pprint.pprint(dir(json_obj))
pprint.pprint(json_obj.keys())
# pprint.pprint(json_obj.values())
pprint.pprint(json_obj.viewkeys())
pprint.pprint(json_obj['num_results'])
for result in json_obj['results']:
	print result.keys()