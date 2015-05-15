import os 
import csv
import pprint 

def parse_csv(df):
	data = []
	with open(df, 'rb') as f:
		r = csv.DictReader(f)
		for line in r:
			data.append(line)
	return data

pprint.pprint(parse_csv('beatles-diskography.csv'))