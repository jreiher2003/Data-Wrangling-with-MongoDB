from bs4 import BeautifulSoup as bs
import requests
import json
from pprint import pprint

html_page = 'airport_data.html'

def extract_data(page):
	data = {"eventvalidation": "",
			"viewstate": ""}

	soup = bs(open(html_page))
	ev = soup.find(id="__EVENTVALIDATION")
	vs = soup.find(id="__VIEWSTATE")
	data['eventvalidation'] = ev['value']
	data['viewstate'] = vs['value']
	return data
	
def make_request(data):
	eventvalidation = data["eventvalidation"]
	viewstate = data['viewstate']

	r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
					  data={'AirportList': "BOS",
							'CarrierList': 'VX',
							'Submit': 'Submit',
							'_EVENTTARGET': "",
							'_EVENTARGUMENT': "",
							'__EVENTVALIDATION': eventvalidation,
							'_VIEWSTATE': viewstate
							}
						)
	return r.text
	
data = extract_data(html_page)
make_request(data)