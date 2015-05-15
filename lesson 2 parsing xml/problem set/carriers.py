#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI
# All your changes should be in the 'extract_carrier' function
# Also note that the html file is a stripped down version of what is actually on the website.

# Your task in this exercise is to get a list of all airlines. Exclude all of the combination
# values, like "All U.S. Carriers" from the data that you return.
# You should return a list of codes for the carriers.

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html)
        carrierlist = soup.find(id="CarrierList")
        for carrier in carrierlist.find_all('option'):
        	data.append(carrier['value'])
        data = [carrier for carrier in data if len(carrier) == 2]
    return data
# print extract_carriers(html_page)

def extract_airports(page):
	data = []
	soup = BeautifulSoup(open(page, 'r'))
	airportlist = soup.find(id='AirportList')
	for airports in airportlist.find_all('option'):
		data.append(airports['value'])
		# print data
	data = [airports for airports in data if not airports.startswith('Al')]
	return data
print extract_airports(html_page)

def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': airport,
                          'CarrierList': carrier,
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text
